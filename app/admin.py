from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Habitacion)
admin.site.register(Cliente)
admin.site.register(Reserva)
