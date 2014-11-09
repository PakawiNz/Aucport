from django.shortcuts import render
import datetime

def main(request):
	member = {
		'fname':"Annie",
		'lname':"Chain",
		'email':"annie@email.com",
		'password':"password",
		'dname':"annieeee",
		'bd':'01/01/1999',
		'address':"bangkok",
		'country':"Thailand",

	}
	context = {
		'title':'Edit Profile',
		'member':member
	}
	return render(request,'member/editprofile.html', context)