from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^(?P<post_url>\w+)/$', views.post, name='post'),
)
