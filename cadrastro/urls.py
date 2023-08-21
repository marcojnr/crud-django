
from django.urls import path
from app_cad import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # rota, view responsavel e nome de referencia
    path('', views.home, name='home')
]
