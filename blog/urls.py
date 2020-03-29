from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),
	#path('', include('blog.urls')),
	path('admin/', admin.site.urls),
	path('account/', include('django.contrib.auth.urls')),
]