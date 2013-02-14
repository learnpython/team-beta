from django.contrib import admin
from timeslots.models import Timeslot, Appointment

admin.site.register(Timeslot)
admin.site.register(Appointment)