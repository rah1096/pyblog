from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^add_post/', views.add_post, name='add_post'),
    url(r'^(?P<post_url>\w+)/$', views.post, name='post'),
)
