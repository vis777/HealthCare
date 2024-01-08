from django.contrib import admin
from Backend.models import ExpertDb,DiseaseDb,DatasetDB,HomeremedyDb
# Register your models here.
admin.site.register(ExpertDb)
admin.site.register(DatasetDB)
admin.site.register(DiseaseDb)
# admin.site.register(ReplyDb)
admin.site.register(HomeremedyDb)