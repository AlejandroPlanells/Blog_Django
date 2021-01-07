from django.urls import path
from . import views

app_name = 'Blog_app'

urlpatterns = [
    # post views
    path('', views.lista_post, name='lista_post'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.detalles_post, name='detalles_post'),

]