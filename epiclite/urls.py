from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from epics import views
from epics.views import app_opened, public_epics, start_epic, join_epic, \
                        active_epics, leave_epic

router = routers.DefaultRouter()
router.register(r'epics', views.EpicViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'epiclite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^app/opened/$', app_opened, name='app-opened'),
    url(r'^public/epics/$', public_epics, name='public-epics'),
    url(r'^start/epic/$', start_epic, name='start-epic'),
    url(r'^join/epic/(?P<epic_num>[0-9A-Za-z]+)/$', join_epic, name='join-epic'),
    url(r'^active/epics/$', active_epics, name='active-epics'),
    url(r'^leave/epic/(?P<epic_id>[0-9]+)/$', leave_epic, name='leave-epic'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)
