import coreapi
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from cityhack import document

def declare_link(url, action, description):
    return coreapi.Link(url=url, action=action, description=description)

def getSchemaContent():
    _schemaContent = {}
    _schemaContent['Category A'] = {
        'url_a': declare_link('category_a/url_a', 'POST', str(document.url_a.__doc__)),
        'url_b': declare_link('category_a/url_b', 'POST', str(document.url_b.__doc__))
    }
    _schemaContent['Category B'] = {
        'url_c': declare_link('category_b/url_c', 'POST', str(document.url_c.__doc__)),
        'url_d': declare_link('category_b/url_d', 'POST', str(document.url_d.__doc__))
    }
    return _schemaContent


schemaContent = coreapi.Document(
    title='Traffic Intelligences API',
    url='swagger',
    content=getSchemaContent()
)

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def view(request):
    print schemaContent
    return Response(schemaContent, status=200)