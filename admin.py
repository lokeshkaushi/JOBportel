from django.contrib import admin
from .models import Job,Candidate,Registration,HrReg,Jobinfo
admin.site.register (HrReg)
admin.site.register (Job)
admin.site.register(Candidate)
admin.site.register(Registration)
admin.site.register (Jobinfo)


# Register your models here.
