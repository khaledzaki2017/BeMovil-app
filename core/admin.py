from django.contrib import admin
from .models import WizardFormJuridica, phoneModel, Partner, WizardFormNatural, Email, User

admin.site.register(WizardFormJuridica)
admin.site.register(WizardFormNatural)

admin.site.register(phoneModel)
admin.site.register(Partner)
admin.site.register(User)
admin.site.register(Email)
