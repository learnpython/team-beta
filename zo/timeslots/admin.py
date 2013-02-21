from django.contrib import admin
from timeslots.models import TimeSlotDay, Timeslot, Appointment

admin.site.register(Timeslot)
admin.site.register(TimeSlotDay)
admin.site.register(Appointment)