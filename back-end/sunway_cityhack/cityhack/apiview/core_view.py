from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import ws_helper as ws

SERVERS = {}

SERVERS[0] = ws.WebSocketServer(0)

@api_view
def init_ws(request):
    return Response({'port': 9080},status=200)

@api_view(['GET'])
def notify_message(request):
    """
    {
        "code": int
    }
    :param request:
    :return:
    """
    # code = request.data['code']
    code = 0
    if code == 0:
        SERVERS[0].send(json.dumps({'okText':'Notify police and ambulance',
                                    'problem': 'Hit and run',
                                    'message': 'Police and ambulance are notified',
                                    'icon': 'ti-check',
                                    'type': 'success'}))
    else:
        SERVERS[0].send(json.dumps({'okText':'Dispatch Ambulance',
                                    'problem': 'Accident',
                                    'message': 'Ambulance is dispatched',
                                    'icon': 'ti-check',
                                    'type': 'success'}))
    return HttpResponse('Message sent')

