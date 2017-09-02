from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$',views.index ),
    url(r'^login/$',views.login),
    url(r'^signup/',views.signup ),
    url(r'^introduction/',views.introduction ),
    url(r'^team/',views.team ),
    url(r'^download/',views.download ),
    url(r'^user/',views.user ),
    url(r'^contact/',views.contact ),
]
