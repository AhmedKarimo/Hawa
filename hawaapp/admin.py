from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Phone, HawaUser, PeriodDate, Examination, OprateExamination, Prediction, Diagnos, RiskCalculator, OprateRisk
# Register your models here.
# admin.site.register(admin)
admin.site.register(HawaUser)
admin.site.register(OprateExamination)
admin.site.register(RiskCalculator)
admin.site.register(Phone)
admin.site.register(PeriodDate)
admin.site.register(Examination)
admin.site.register(Prediction)
admin.site.register(OprateRisk)
admin.site.register(Diagnos)
