from django.urls import path
from . import views
from .models import Kinodb, Rekinodb, Chanchitodb, Combodb, Chao1db, Chao2db, Chao3db


urlpatterns = [
    path('', views.index, name='index'),  # Aca despues el menú
    path('kino/', views.resultados, name='kino_index'),
    path('rekino/', views.resultados, name='rekino_index'),
    path('chanchito/', views.resultados, name='chanchito_index'),
    path('combo/', views.resultados, name='combo_index'),
    path('chao1/', views.resultados, name='chao1_index'),
    path('chao2/', views.resultados, name='chao2_index'),
    path('chao3/', views.resultados, name='chao3_index'),
    path('kino-admin/', views.resultados_admin, name='kino_admin'),
    path('rekino-admin/', views.resultados_admin, name='rekino_admin'),
    path('chanchito-admin/', views.resultados_admin, name='combo_admin'),
    path('chao1-admin/', views.resultados_admin, name='chao1_admin'),
    path('chao2-admin/', views.resultados_admin, name='chao2_admin'),
    path('chao3-admin/', views.resultados_admin, name='chao3_admin'),
    path('archivos/', views.upload_file, name='archivos_index'),
    path('estadisticas-kino/', views.estadisticas, name='estadisticas_kino_index'),
    path('estadisticas-rekino/', views.estadisticas, name='estadisticas_rekino_index'),
    path('estadisticas-chanchito/', views.estadisticas, name='estadisticas_chanchito_index'),
    path('estadisticas-combo/', views.estadisticas, name='estadisticas_combo_index'),
    path('estadisticas-chao1/', views.estadisticas, name='estadisticas_chao1_index'),
    path('estadisticas-chao2/', views.estadisticas, name='estadisticas_chao2_index'),
    path('estadisticas-chao3/', views.estadisticas, name='estadisticas_chao3_index'),
    path('coincidencias/',views.mostrar_coincidencias,name='coincidencias_index'),

    #Url de botones
    path('delete/<str:model_name>/<int:pk>/',
         views.delete_file, name='delete-file'),
    path('todatabase/<int:pk>/', views.agregar_a_db, name='agregar-a-db'),
    path('delete-row/<str:model_name>/<int:pk>/',
         views.delete_row, name='delete-row'),

]
