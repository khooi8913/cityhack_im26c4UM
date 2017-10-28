import socket
import threading

from gevent.pool import Pool
from gevent.pywsgi import WSGIServer as _WSGIServer
from ws4py import format_addresses
from ws4py.server.geventserver import WebSocketWSGIHandler
from ws4py.server.wsgiutils import WebSocketWSGIApplication
from ws4py.websocket import WebSocket

SERVERS = {}
HOST = '0.0.0.0'

class GEventWebSocketPool(Pool):
    def track(self, websocket):
        print("Managing websocket %s" % format_addresses(websocket))
        return self.spawn(websocket.run)

    def clear(self):
        print("Terminating server and all connected websockets")
        for greenlet in list(self):
            try:
                websocket = greenlet._run.im_self
                if websocket:
                    websocket.close(1001, 'Server is shutting down')
            except:
                pass
            finally:
                self.discard(greenlet)


class WSGIServer(_WSGIServer):
    handler_class = WebSocketWSGIHandler

    def __init__(self, *args, **kwargs):
        _WSGIServer.__init__(self, *args, **kwargs)
        self.pool = GEventWebSocketPool()

    def stop(self, *args, **kwargs):
        self.pool.clear()
        _WSGIServer.stop(self, *args, **kwargs)


def WebSocketHandler(thread_id):
    class _WebSocket(WebSocket):
        def __init__(self, sock, protocols=None, extensions=None, environ=None, heartbeat_freq=None):
            super(_WebSocket, self).__init__(sock, protocols, extensions, environ, heartbeat_freq)
            SERVERS[thread_id]['sockets'].append(self)

        def opened(self):
            super(_WebSocket, self).opened()

        def closed(self, code, reason=None):
            super(_WebSocket, self).closed(code, reason)
            print('Socket is closed due to: {}'.format(reason))

        def unhandled_error(self, error):
            super(_WebSocket, self).unhandled_error(error)

        def received_message(self, message):
            super(_WebSocket, self).received_message(message)

    return _WebSocket


class WebSocketServer(object):
    def __init__(self, thread_id):
        self.thread_id = thread_id
        # self.ws_url = 'ws://{}'.format(settings.HOST)
        self.server = WSGIServer((HOST, 9080),
                                 WebSocketWSGIApplication(handler_cls=WebSocketHandler(thread_id)))
        SERVERS[thread_id] = {
            'server': self.server,
            'sockets': []
        }
        self.host = self.server.server_host
        self.port = self.server.server_port

        def start_server():
            self.server.serve_forever()

        self.server_thread = threading.Thread(target=start_server)
        self.server_thread.start()

    def send(self, message):
        if len(SERVERS[self.thread_id]['sockets']) != 0:
            closed_client = 0
            print('Sending message to {} client(s)...'.format(len(SERVERS[self.thread_id]['sockets'])))
            for sock in list(SERVERS[self.thread_id]['sockets']):
                try:
                    sock.send(message)
                except BaseException as e:
                    sock.close(reason=str(e))
                    SERVERS[self.thread_id]['sockets'].remove(sock)
                    closed_client += 1
                    continue
            if closed_client != 0:
                print('Closed {} client(s)...'.format(closed_client))
            print('Done...')
        else:
            print('No client is connecting')

    def close(self):
        if not self.server.closed:
            for sock in SERVERS[self.thread_id]['sockets']:
                try:
                    sock.send('end')
                except:
                    sock.close(reason='Broken pipe')
                    SERVERS[self.thread_id]['sockets'].remove(sock)
                    continue
            self.server.stop()