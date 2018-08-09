from django.shortcuts import render, redirect


def index(request):
    return render(request, template_name='index.html')


def magazine(request):
    return redirect('https://bit.ly/ACEMag2018')


def view_404(request):
    return redirect('https://vipsace.org')
