from django.contrib import admin

from .models import Finch, Flight, Cage

admin.site.register(Finch)
admin.site.register(Flight)
admin.site.register(Cage)
