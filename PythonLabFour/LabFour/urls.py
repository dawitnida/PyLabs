from django.conf.urls import patterns, include, url
from django.contrib import admin
from myblog.views import *


admin.autodiscover()

urlpatterns = patterns('',


    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',          'myblog.views.show_post', name='home'),
    url(r'^myblog/$',   'myblog.views.show_post', name='home'),
    url(r'^myblog/(?P<postid>.*)/$',   'myblog.views.detail_post', {}, name='detail'),
    url(r'^editblog/(?P<postid>.*)/$',  'myblog.views.edit_post', {}, name='edit_post'),
    url(r'^addblog',  'myblog.views.add_post', name='add_blog'),
    url(r'^deleteblog/(?P<postid>.*)/$',  'myblog.views.delete_post', name='delete_post'),
    url(r'^login/$', login_user, name = 'login'),
    url(r'^createuser/$', create_user, name = 'createuser'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                      {'next_page': '/myblog/'}),
    url(r'^api/myblog/$', 'myblog.views.apiblog'),

)
