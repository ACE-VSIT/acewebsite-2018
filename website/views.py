<<<<<<< HEAD
from django.shortcuts import render
def index(request):
	return render(request, 'website/index.html', {})

# Create your views nnshere.
=======
from django.shortcuts import render, redirect


def index(request):
    return render(request, template_name='index.html')


def magazine(request):
    return redirect('https://bit.ly/ACEMag2018')


def view_404(request, exception):
    return redirect('/')

>>>>>>> b11e8b8b121afc12bdc9fc35b3208d96b477c51c
