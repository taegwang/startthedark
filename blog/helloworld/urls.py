from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^me/([\w]+)/([\w]+)/([\w]+)/', 'helloworld.views.me'),
	url(r'^$','helloworld.views.hello'), 
	url(r'^admin/', include(admin.site.urls)),
)
