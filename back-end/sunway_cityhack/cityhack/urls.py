from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from cityhack import apiview, swagger_doc

urlpatterns = {
    url(r'^init_ws$', apiview.init_ws),
    url(r'^notify_message$', apiview.notify_message),
    url(r'^swagger$', swagger_doc.view)
}

urlpatterns = format_suffix_patterns(urlpatterns)