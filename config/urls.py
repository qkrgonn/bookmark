from django.contrib import admin
from django.urls import path, include
from bookmark import views

urlpatterns = [
    path('', views.home, name='bookmark'),  # '/' 경로에 대한 처리 추가
    path('bookmark/', include('bookmark.urls')),
    path('admin/', admin.site.urls),
]