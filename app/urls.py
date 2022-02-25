from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('',views.indexView.as_view()),
    path('habitacion',views.HabitacionView.as_view(),name='habitacion'),
    path('habitacion/<int:habitacion_id>',views.HabitacionDetailView.as_view(),name='habitacion'),
    path('cliente',views.ClienteView.as_view(),name='cliente'),
    path('cliente/<int:cliente_id>',views.ClienteDetailView.as_view(),name='cliente'),
    path('reserva',views.ReservaView.as_view(),name='reserva'),
    path('reserva/<int:reserva_id>',views.ReservaDetailView.as_view(),name='reserva')
]