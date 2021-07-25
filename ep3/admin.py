from django.contrib import admin
from .models import paciente, exame, amostra, Paciente_Exame_Amostra

class RelationInLine(admin.TabularInline):
    model = Paciente_Exame_Amostra
    extra = 1

class AmostraRelation(admin.ModelAdmin):
    inlines = (RelationInLine,)

admin.site.register(paciente)
admin.site.register(exame)
admin.site.register(amostra, AmostraRelation)
admin.site.register(Paciente_Exame_Amostra)