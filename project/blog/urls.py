from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),


    path('blog/', views.blog, name='blog'),
    path('posts/<int:id>', views.post_detail, name ='post_detail'),


    path('contact/', views.contact, name='contact'),
    path('coffee/', views.coffee, name='coffee'),

    path('shop_detail/<int:id>', views.shop_detail, name='shop_detail'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
