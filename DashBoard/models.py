from django.db import models

# Create your models here.

class Children(models.Model):
	code = models.AutoField(primary_key=True)
	Date_of_entry = models.DateField(max_length=8)
	Child_Fname = models.CharField(max_length=200, null=True)
	Child_Lname = models.CharField(max_length=200, null=True)
	Date_of_birth = models.DateField(max_length=8)
	Gender = models.CharField(max_length=200, null=True)
	Relegion = models.CharField(max_length=200, null=True)
	Caste = models.CharField(max_length=200, null=True)
	Father_name =  models.CharField(max_length=200, null=True)
	Mother_name = models.CharField(max_length=200, null=True)
	Siblings = models.IntegerField(null=True)
	Contact_Number = models.IntegerField(blank=True, null=True)
	Name_of_sponsor = models.CharField(max_length=200, null=True)
	Need_of_child = models.CharField(max_length=200, null=True)
	Join_date_of_diksha = models.DateField(max_length=8)
	Children_came_diksha = models.CharField(max_length=200, null=True)
	created_on = models.DateTimeField(auto_now_add=True,null=True)
	def __str__(self):
		return self.Child_Fname


class Education(models.Model):
	code = models.CharField(max_length=255,unique=True,null=True,blank=True)
	Child_goes_to = models.CharField(max_length=200, null=True)
	School_Name = models.CharField(max_length=200, null=True)
	Class = models.CharField(max_length=200, null=True)
	Medium = models.CharField(max_length=200, null=True)
	Level_of_school = models.CharField(max_length=200, null=True)
	Board = models.CharField(max_length=200, null=True)
	Type_of_school = models.CharField(max_length=200, null=True)
	Child_studying_from = models.CharField(max_length=200, null=True)
	Hostel = models.CharField(max_length=200, null=True)
	Hostel_Fees = models.CharField(max_length=200, null=True)
	College_Name = models.CharField(max_length=200, null=True)
	Course = models.CharField(max_length=200, null=True)
	Scheme_of_course = models.CharField(max_length=200, null=True)
	Semeste = models.CharField(max_length=200, null=True)
	University = models.CharField(max_length=200, null=True)
	Type_of_College = models.CharField(max_length=200, null=True)
	Accomodation = models.CharField(max_length=200, null=True)
	Fees_for_accomodation = models.CharField(max_length=200, null=True)
	created_on = models.DateTimeField(auto_now_add=True,null=True)
	def __str__(self):
		return self.Child_goes_to

class Sponsor(models.Model):
	Code_of_child = models.CharField(max_length=255,unique=True,null=True,blank=True)
	Fname = models.CharField(max_length=120 , null=True)
	Sname = models.CharField(max_length=120 , null=True)
	Nationality = models.CharField(max_length=120 , null=True)
	Contact_Number = models.CharField(max_length=120 , null=True)
	Email = models.CharField(max_length=120 , null=True)
	Address = models.CharField(max_length=120 , null=True)
	Sponsorship_for = models.CharField(max_length=120 , null=True)
	Date_of_payment = models.CharField(max_length=120 , null=True)
	Name_of_sponsor_kid = models.CharField(max_length=120 , null=True)
	Sponsor_met_the_children = models.CharField(max_length=120 , null=True)
	Plan_to_meet = models.CharField(max_length=120 , null=True)
	Which_date = models.CharField(max_length=120 , null=True)
	Standing_monthly_order = models.CharField(max_length=120 , null=True)
	Standing_yearly_order = models.CharField(max_length=120 , null=True)
	Bank_account = models.CharField(max_length=120 , null=True)
	Sponsor_stopped_to_pay = models.CharField(max_length=120 , null=True)
	Which_date = models.CharField(max_length=120 , null=True)
	Reason = models.CharField(max_length=120 , null=True)
	created_on = models.DateTimeField(auto_now_add=True,null=True)
	def __str__(self):
		return self.Fname
