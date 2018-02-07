from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.files_list, name='files_list'),
    url(r'^new/$', views.upload_new_file, name='upload_new_file'),
    url(r'^(?P<pk>\d+)/run/$', views.run_on_file, name='run_on_file'),
    url(r'^(?P<pk>\d+)/download/$', views.download_file, name='download_file'),
]
