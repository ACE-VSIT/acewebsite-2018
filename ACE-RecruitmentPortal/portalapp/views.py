from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .models import Tasks, ACEUserProfile


# Create your views here.

def ace_magazine(request):
    return redirect('https://bit.ly/VipsACE')


def ace_video(request):
    return redirect('http://bit.ly/DontBlinkACE')


def ace_website(request):
    return render(request, 'acewebsite/index.html')


def login(request):
    if request.user.is_authenticated:

        if not ACEUserProfile.objects.filter(name=request.user).exists():
            return redirect('/form')
        else:
            return redirect('/home')

    return render(request, 'portalapp/index.html')


@login_required(login_url='/')
def home(request):
    if not request.user.is_superuser and ACEUserProfile.objects.filter(name=request.user).exists():
        social = request.user.social_auth.get(provider='facebook')
        userid = social.uid
        first_name = social.extra_data['first_name']
        email_id = social.extra_data['email']

        src = "https://graph.facebook.com/" + str(userid) + "/picture?width=80&height=80"

        tasks = Tasks.objects.order_by('task_id')

        active_tasks = len(tasks)
        print(first_name)

        return render(request, 'portalapp/main.html',
                      {'fb_image_url': src, 'first_name': first_name, 'tasks': tasks, 'active_tasks': active_tasks})

    if request.user.is_superuser:
        print("Super User Logged In")

        social = request.user.social_auth.get(provider='facebook')
        userid = social.uid
        first_name = social.extra_data['first_name']
        email_id = social.extra_data['email']
        src = "https://graph.facebook.com/" + str(userid) + "/picture?width=80&height=80"

        tasks = Tasks.objects.order_by('task_id')

        active_tasks = len(tasks)
        print(first_name)

        return render(request, 'portalapp/main.html',
                      {'fb_image_url': src, 'first_name': first_name, 'tasks': tasks, 'active_tasks': active_tasks})

    return redirect('/form')


def logout(request):
    auth_logout(request)
    return redirect('/')


@login_required(login_url='/')
def submit_task(request):
    submission_url = request.POST['task']
    task_id = request.POST['task_id']
    print(submission_url, task_id)
    # get current user instance
    user = User.objects.get(username=request.user)

    # get ace profile of current user
    ace_profile_obj = ACEUserProfile.objects.filter(name=user)
    try:
        ace_profile_obj = ace_profile_obj[0]
        print("Inside TRY BLOCK")
    except:
        ace_profile_obj = None

    # get task instance for the selected task using task_id
    task_obj = Tasks.objects.get(task_id=task_id)

    # Associate selected task with "ACE user"
    task_obj.did_by.add(ace_profile_obj)

    # Now insert submission url and set task submitted to true for current user

    ace_profile_obj = ACEUserProfile(name=user)
    try:
        ace_profile_obj.submission_url = submission_url
        ace_profile_obj.task_submitted = True
        ace_profile_obj.task_id = task_obj
        ace_profile_obj.save()
        print("SAVED")
    except:
        print("You have already submitted this task")

    return redirect('/home')

    return render(request, 'portalapp/main.html')


@login_required(login_url='/')
def form_data(request):
    if not ACEUserProfile.objects.filter(name=request.user).exists():
        return render(request, 'portalapp/form.html')
    else:
        return redirect('/home')


@login_required(login_url='/')
def form_input(request):
    phone = request.GET.get('phone', True)
    enroll_number = request.GET.get('roll', True)
    course = request.GET.get('course', True)
    email_id = request.GET.get('email', True)
    section = request.GET.get('section', True)
    print(phone, enroll_number, course, email_id, section)

    user = User.objects.get(username=request.user)
    ace_user = ACEUserProfile(name=user, enroll_number=enroll_number, course=course, email_id=email_id, section=section,
                              phone_number=phone)
    ace_user.save()

    print("Success")

    return redirect('/home')


@login_required(login_url='/')
def serve_main_page(request):
    tasks = Tasks.objects.all()

    active_tasks = len(tasks)

    return render(request, 'portalapp/main.html',
                  {'fb_image_url': "image", 'first_name': "VIPS-ACE", 'tasks': tasks, 'active_tasks': active_tasks})
