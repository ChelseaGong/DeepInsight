from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$',views.index ),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/',views.signup ,name = 'signup'),
    url(r'^introduction/',views.introduction ),
    url(r'^team/',views.team ),
    url(r'^download/',views.download ),
    url(r'^user/',views.user ),
    url(r'^contact/',views.contact ),
    url(r'^login/forgot/',views.forgot ),
    url(r'^personal/$', views.personal),
    url(r'^personal/apply/', views.apply),
    url(r'^personal/change/', views.change),
]