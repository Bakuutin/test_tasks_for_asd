from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include

from .views import LoginView, LogoutView, StorageView, FileUploadView, DeleteFilenameView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^social/', include('social_django.urls', namespace='social')),

    url(r'^$', login_required(StorageView.as_view()), name='storage'),
    url(r'^upload/$', login_required(FileUploadView.as_view()), name='upload'),
    url(r'^delete/(?P<pk>[0-9]+)/$', login_required(DeleteFilenameView.as_view()), name='delete'),
]
