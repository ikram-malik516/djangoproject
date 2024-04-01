from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def formsubmit(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		age = request.POST.get('age')
		gender = request.POST.get('gender')
		interstList = request.POST.getlist('interests')
		country = request.POST.get('country')
		context = {'name':name, 'email':email, 'age':age, 'gender':gender, 'intersts':interstList, 'country':country }
		return render(request, 'response.html', context)

	else:
		return render(request, 'form_submit.html')


def greeting(request):
	return HttpResponse("Hello world......!")

def contactus(request):
	return HttpResponse("03XXXXXXXXX")

def index(request):
	return HttpResponse("<h1 style = 'color:purple'>welcome to my website...!</h1>")

def test123(request):
	return render(request, 'test.html')

def index(request):
	return render(request, 'index.html')

def news(request):
	return render(request, 'news.html')

def contact(request):
	return render(request, 'contact.html')

def about(request):
	return render(request, 'about.html')

def register(request):
	if request.method == 'POST':
		Sname = request.POST.get('uname')
		Semail = request.POST.get('email')
		Spassw = request.POST.get('pass')
		Srepass = request.POST.get('repass')

		context = {'uname': Sname, 'email' : Semail, 'color' : ['red', 'green', 'blue']}

		return render(request, 'index.html', context)
