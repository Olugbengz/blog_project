from django.urls import path, include
from rest_framework.authtoken import views
from .views import home


urlpatterns = [
	path('', home, name='home'),
	path('category/', include('blog_api.category.urls')),
	path('blog_post/', include('blog_api.blog_post.urls')),
	path('comment/', include('blog_api.comment.urls')),
]