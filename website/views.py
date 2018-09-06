from django.shortcuts import render, redirect
from website.models import Achievement, Calendar, Event, Gallery, Member, Project
from portalapp.models import ACEUserProfile


def index(request):
    events = Event.objects.all()[:3]
    members = ACEUserProfile.objects.filter(is_council=True)
    calendar = Calendar.objects.all()[:3]
    return render(request, template_name='index.html',
                  context={'members': members, 'events': events, 'calendar': calendar})


def members(request):
    members = Member.objects.all()
    return render(request, template_name='members.html', context={'members': members})


def events(request):
    events = Event.objects.all()
    return render(request, template_name='events.html', context={'events': events})


def gallery(request):
    gallery = Gallery.objects.all()
    return render(request, template_name='gallery.html', context={'gallery': gallery})


def projects(request):
    projects = Project.objects.all()
    return render(request, template_name='projects.html', context={'projects': projects})


def achievements(request):
    achievements = Achievement.objects.all()
    return render(request, template_name='achievements.html', context={'achievements': achievements})


def calendar(request):
    calendar = Calendar.objects.all()
    return render(request, template_name='calendar.html', context={'calendar': calendar})


# other stuff

def magazine(request):
    return redirect('https://bit.ly/ACEMag2018')


def view_404(request, exception):
    return redirect('/')
