from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# path("どんなパスが来るか",動かす関数, 名前 ) トップページへいくので最初は空文字
app_name = "diary"
urlpatterns = [
  path("", views.index, name="index"),
  path("page/create/", views.page_create, name="page_create"),  
  path("pages/", views.page_list, name="page_list"),
  path("pages/<uuid:id>/", views.page_detail, name="page_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

