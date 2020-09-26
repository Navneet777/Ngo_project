from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Children,Sponsor,Education
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'DashBoard/login1.html')

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
	data = Children.objects.all().order_by('-created_on')[:30]
	context = {'data': data}
	return render(request, 'DashBoard/home1.html' , context)


@login_required(login_url='login')
def addChildren(request):

	if request.method == "POST":
		Date_of_entry = request.POST["Date_of_entry"]
		Child_Fname = request.POST["Child_Fname"]
		Child_Lname = request.POST["Child_Lname"]
		Date_of_birth = request.POST["Date_of_birth"]
		Gender = request.POST["Gender"]
		Relegion = request.POST["Relegion"]
		Caste = request.POST["Caste"]
		Father_name = request.POST["Father_name"]
		Mother_name = request.POST["Mother_name"]
		Siblings = request.POST["Siblings"]
		Contact_Number = request.POST["Contact_Number"]
		Name_of_sponsor = request.POST["Name_of_sponsor"]
		Need_of_child = request.POST["Need_of_child"]
		Join_date_of_diksha = request.POST["Join_date_of_diksha"]
		Children_came_diksha = request.POST["Children_came_diksha"]


		children = Children(Date_of_entry=Date_of_entry , Child_Fname = Child_Fname , Child_Lname = Child_Lname , Date_of_birth = Date_of_birth , Gender = Gender , Relegion = Relegion , Caste = Caste , Father_name = Father_name , Mother_name = Mother_name , Siblings = Siblings , Contact_Number = Contact_Number , Name_of_sponsor = Name_of_sponsor ,Need_of_child = Need_of_child , Join_date_of_diksha= Join_date_of_diksha , Children_came_diksha = Children_came_diksha)
		children.save()
		rs = Children.objects.latest('created_on')
		print(rs)
		return redirect('home')
	return render(request,'DashBoard/addChildren.html')


@login_required
def ChildProfile(request,code):
	current_data = Children.objects.get(code=code)
	sponsor = Sponsor.objects.get(Code_of_child=str(code))
	education = Education.objects.get(code=str(code))
	return render(request,"DashBoard/profile1.html",{'data': current_data,'education':education,'sponsor':sponsor})

@login_required
def EditChildren(request,code):
	current_data = Children.objects.get(code=code)
	context = {'data': current_data}

	if request.method == "POST":
		Date_of_entry = request.POST["Date_of_entry"]
		Child_Fname = request.POST["Child_Fname"]
		Child_Lname = request.POST["Child_Lname"]
		Date_of_birth = request.POST["Date_of_birth"]
		Gender = request.POST["Gender"]
		Relegion = request.POST["Relegion"]
		Caste = request.POST["Caste"]
		Father_name = request.POST["Father_name"]
		Mother_name = request.POST["Mother_name"]
		Siblings = request.POST["Siblings"]
		Contact_Number = request.POST["Contact_Number"]
		Name_of_sponsor = request.POST["Name_of_sponsor"]
		Need_of_child = request.POST["Need_of_child"]
		Join_date_of_diksha = request.POST["Join_date_of_diksha"]
		Children_came_diksha = request.POST["Children_came_diksha"]


		children = Children(Date_of_entry=Date_of_entry , Child_Fname = Child_Fname , Child_Lname = Child_Lname , Date_of_birth = Date_of_birth , Gender = Gender , Relegion = Relegion , Caste = Caste , Father_name = Father_name , Mother_name = Mother_name , Siblings = Siblings , Contact_Number = Contact_Number , Name_of_sponsor = Name_of_sponsor ,Need_of_child = Need_of_child , Join_date_of_diksha= Join_date_of_diksha , Children_came_diksha = Children_came_diksha)
		children.save()
		return redirect('home')

	return render(request,"DashBoard/EditChildren.html" , context)


@login_required
def EducationProfile(request):
	if request.method == "POST":
		code = request.POST['code']
		Child_goes_to = request.POST['Child_goes_to']
		School_Name = request.POST['School_Name']
		Class = request.POST['Class']
		Medium = request.POST['Medium']
		Level_of_school = request.POST['Level_of_school']
		Board = request.POST['Board']
		Type_of_School = request.POST['Type_of_School']
		Child_studying_from = request.POST['Child_studying_from']
		Hostel = request.POST['Hostel']
		Hostel_Fees = request.POST['Hostel_Fees']
		College_Name = request.POST['College_Name']
		Course = request.POST['Course']
		# Scheme_of_course = request.POST['Scheme_of_course']
		Semester = request.POST['Semester']
		University = request.POST['University']
		Type_of_College = request.POST['Type_of_College']
		Accomodation = request.POST['Accomodation']
		Fees_for_accomodation = request.POST['Fees_for_accomodation']
		if Children.objects.filter(code=int(code)).exists():
			education = Education.objects.create(code=int(code),Child_goes_to=Child_goes_to,School_Name=School_Name,Class=Class,Medium=Medium,Level_of_school=Level_of_school,Board=Board,Type_of_school=Type_of_School,Child_studying_from=Child_studying_from,Hostel=Hostel,Hostel_Fees=Hostel_Fees,College_Name=College_Name,Course=Course,Semeste=Semester,University=University,Type_of_College=Type_of_College,Accomodation=Accomodation,Fees_for_accomodation=Fees_for_accomodation)
			education.save()
			messages = messages.info(request, 'Education Details Saved.')
			return render(request,'DashBoard/EducationProfile')
		else:
			messages.info(request, 'Incorrect Children code')
			print('Children code Dost Not Match')
	return render(request,"DashBoard/EducationProfile.html")

@login_required
def SponsorProfile(request):
	if request.method == "POST":
		code = request.POST['code']
		Sponsor_Fname = request.POST['Sponsor_Fname']
		Sponsor_Lname = request.POST['Sponsor_Lname']
		Nationality = request.POST['Nationality']
		Contact_Number = request.POST['Contact_Number']
		Email = request.POST['Email']
		Address = request.POST['Address']
		Sponsorship_for = request.POST['Sponsorship_for']
		Sponsor_start_date_of_payment = request.POST['Sponsor_start_date_of_payment']
		Name_of_sponsor_kid = request.POST['Name_of_sponsor_kids']
		Sponsor_met_the_children = request.POST['Sponsor_met_the_children']
		Scheme_of_donation = request.POST['Scheme_of_donation']
		Standing_monthly_order = request.POST['Standing_monthly_order']
		Standing_yearly_order = request.POST['Standing_Yearly_order']
		Bank_account = request.POST['Bank_account_in']
		If_Sponsor_stopped_paying = request.POST['If_Sponsor_stopped_paying']

		if Children.objects.filter(code=int(code)).exists():
			sponsor_create = Sponsor.objects.create(Code_of_child=int(code),Fname=Sponsor_Fname,Sname=Sponsor_Lname,Nationality=Nationality,Contact_Number=Contact_Number,Email=Email,Address=Address,Sponsorship_for=Sponsorship_for,Date_of_payment=Sponsor_start_date_of_payment,Name_of_sponsor_kid=Name_of_sponsor_kid,Sponsor_met_the_children=Sponsor_met_the_children,Standing_monthly_order=Standing_monthly_order,Standing_yearly_order=Standing_yearly_order,Bank_account=Bank_account,Sponsor_stopped_to_pay=If_Sponsor_stopped_paying)
			sponsor_create.save()
			print('sponsor add sucessfully')
		else:
			messages.info(request, 'Incorrect Children code..')
	return render(request,"DashBoard/SponsorProfile.html")

def Check(request):
	return render(request,"DashBoard/check.html")

def demo(request):
	return render(request,"DashBoard/di.html")
