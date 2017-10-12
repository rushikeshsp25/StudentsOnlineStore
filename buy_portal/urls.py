from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='buy_portal'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_user/$', views.login_user, name='login_user'),
     url(r'^logout_user/$', views.logout_user, name='logout_user'),
     url(r'^create_new_user/$', views.create_new_user, name='create_new_user'),
     url(r'^sell/$', views.sell, name='sell'),
     url(r'^advertise/$', views.advertise, name='advertise'),
     url(r'^requirement/$', views.requirement, name='requirement'),
     url(r'^item_detail/(?P<item_id>[0-9]+)$', views.item_detail, name='item_detail'),
    url(r'^adv_detail/(?P<adv_id>[0-9]+)$', views.adv_detail, name='adv_detail'),
    url(r'^my_activity/$', views.my_activity, name='my_activity'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)