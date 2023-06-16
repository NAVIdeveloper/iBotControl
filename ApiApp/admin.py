from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(User)
admin.site.register(BotApp)

admin.site.register(Ability)
admin.site.register(StartStep)
admin.site.register(Info)

admin.site.register(Contact)

admin.site.register(QueryAnswer)

admin.site.register(Pricing)
admin.site.register(Doc)
admin.site.register(Command_Doc)
