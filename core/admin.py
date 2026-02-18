from django.contrib import admin
from .models import Donor, Recipient, Hospital


admin.site.register(Donor)
admin.site.register(Recipient)
admin.site.register(Hospital)

