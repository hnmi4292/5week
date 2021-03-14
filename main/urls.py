from django.contrib import admin
from django.urls import path
from main.views import index, blog, posting, new_post, remove_post, sellblog, sell_posting, new_get, remove_get
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from main.views import GetViewSet, ProductViewSet


router = routers.DefaultRouter()
router.register('main', GetViewSet, ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/', posting, name='posting'),
    path('blog/new_post/', new_post),
    path('blog/<int:pk>/remove/', remove_post),
    path('sellblog/', sellblog, name='sellblog'),
    path('sellblog/<int:pk>/', sell_posting, name='sell_posting'),
    path('sellblog/new_get/', new_get),
    path('sellblog/<int:pk>/remove/', remove_get),
    url(r'^', include(router.urls)),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
