from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

from website.models import Achievement, Agenda, Event, Gallery, Project, Alumni, Mentor
from portalapp.models import ACEUserProfile


def index(request):
    events = Event.objects.all()[:3]
    members = ACEUserProfile.objects.filter(is_council=True)
    calendar = Agenda.objects.all()[:3]
    projects = Project.objects.all()[:3]
    return render(request, template_name='index.html',
                  context={'members': members, 'events': events, 'calendar': calendar, 'projects': projects})


def member(request):
    members = ACEUserProfile.objects.filter(is_member=True)
    return render(request, template_name='member.html', context={'members': members})


def mentor(request):
    mentors = Mentor.objects.all()
    return render(request, template_name='mentor.html', context={'mentor': mentors})


def alumni(request):
    alumnus = Alumni.objects.all()
    return render(request, template_name='alumni.html', context={'alumnus': alumnus})


def event(request):
    events = Event.objects.all()
    return render(request, template_name='events.html', context={'events': events})


def gallery(request):
    gallery = Gallery.objects.all()
    return render(request, template_name='gallery.html', context={'gallery': gallery})


def project(request):
    projects = Project.objects.all()
    return render(request, template_name='projects.html', context={'projects': projects})


def achievement(request):
    achievements = Achievement.objects.all()
    return render(request, template_name='achievement.html', context={'achievements': achievements})


def agenda(request):
    agendas = Agenda.objects.all()
    return render(request, template_name='calendar.html', context={'agendas': agendas})


def codeofconduct(request):
    return render(request, template_name='codeofconduct.html')


def selection(request):
    return render(request, template_name='selection.html')


# other stuff

def magazine(request):
    return redirect('https://bit.ly/ACEMag2018')


def view_404(request, exception):
    return redirect('/')


def logout(request):
    auth_logout(request)
    return redirect('/library/')
