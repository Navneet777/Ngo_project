from django.contrib import admin

# Register your models here.
from .models import Children,Sponsor,Education


class ChildrenAdmin(admin.ModelAdmin):
    list_display = ['code','Child_Fname','Child_Lname','Date_of_birth','Name_of_sponsor','Join_date_of_diksha','Children_came_diksha','Need_of_child']

class SponsorAdmin(admin.ModelAdmin):
    list_display = ['Code_of_child','Fname','Sname','Nationality','Name_of_sponsor_kid','Sponsorship_for','Contact_Number','Email','Address']

class EducationAdmin(admin.ModelAdmin):
    list_display = ['code','Child_goes_to','School_Name','Class','Medium','Board','Type_of_school','College_Name','Course','University','Type_of_College']


admin.site.register(Children,ChildrenAdmin)
admin.site.register(Sponsor,SponsorAdmin)
admin.site.register(Education,EducationAdmin)
