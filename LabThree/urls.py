from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',


    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',          'myblog.views.show_post', name='home'),
    url(r'^myblog/$',   'myblog.views.show_post', name='home'),
    url(r'^myblog/(?P<postid>.*)/$',   'myblog.views.detail_post'),
    url(r'^editblog/(?P<postid>.*)/$',  'myblog.views.edit_post'),
    url(r'^addblog',  'myblog.views.add_post'),
    url(r'^deleteblog/(?P<postid>.*)/$',  'myblog.views.delete_post'),

)
