from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'index.html')

def add_expenses(request):
	return render(request, 'add_expenses.html')