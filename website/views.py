from django.shortcuts import render

def home_page_view(request):
	return render(request, "website/home.html")

def about_page_view(request):
	return render(request, "website/about.html")

def info_page_view(request):
	return render(request, "website/info.html")
