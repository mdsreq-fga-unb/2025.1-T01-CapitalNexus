from django.contrib import admin
from .models import Membro, Nucleo, Cargo, MembroNucleo

admin.site.register(Membro)
admin.site.register(Nucleo)
admin.site.register(Cargo)
admin.site.register(MembroNucleo)
