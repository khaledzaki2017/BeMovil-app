from django.contrib import admin
from .models import WizardForm, PhoneOTP, Partner

admin.site.register(WizardForm)
admin.site.register(PhoneOTP)
admin.site.register(Partner)
