from django.utils.timezone import localtime, now

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.db.models import F

from .models import Tasks, ACEUserProfile, Submissions
from ace.settings import SELECTION_START_DATE, SELECTION_END_DATE


def login(request):
    if request.user.is_authenticated:

        if not ACEUserProfile.objects.filter(name=request.user).exists():
            return redirect('/portal/form')
        else:
            return redirect('/portal/home')

    return render(request, 'portalapp/index.html')


@login_required(login_url='/')
def home(request):
    if not request.user.is_superuser and ACEUserProfile.objects.filter(name=request.user).exists():

        today = localtime(now())

        if today < SELECTION_START_DATE or today > SELECTION_END_DATE:
            return render(request, template_name='portalapp/timer.html')
        else:
            social = request.user.social_auth.get(provider='facebook')
            userid = social.uid
            first_name = social.extra_data['first_name']

            src = "https://graph.facebook.com/" + str(userid) + "/picture?width=80&height=80"

            tasks = Tasks.objects.order_by('task_id')
            submissions = Submissions.objects.filter(user=ACEUserProfile.objects.get(name=request.user)).values_list('task__task_id', flat=True)

            active_tasks = len(tasks)

            return render(request, 'portalapp/main.html',
                          {'fb_image_url': src, 'first_name': first_name, 'tasks': tasks,
                           'submissions': submissions, 'active_tasks': active_tasks})
    return redirect('/portal/form')


def logout(request):
    auth_logout(request)
    return redirect('/portal/')


@login_required(login_url='/')
def submit_task(request):
    submission_url = request.POST['task']
    task_id = request.POST['task_id']
    print(submission_url, task_id)
    # get current user instance
    user = User.objects.get(username=request.user)

    # get ace profile of current user
    ace_profile_obj = ACEUserProfile.objects.get(name=user)

    # get task instance for the selected task using task_id
    task_obj = Tasks.objects.get(task_id=task_id)

    # Now insert submission url and set task submitted to true for current user
    try:
        submission_obj = Submissions(user=ace_profile_obj, task=task_obj)
        submission_obj.submission_url = submission_url
        submission_obj.task_submitted = True
        submission_obj.save()
        task_obj.total_submissions = F('total_submissions') + 1
        task_obj.save()
    except:
        submission_obj = Submissions.objects.get(user=ace_profile_obj, task=task_obj)
        submission_obj.submission_url = submission_url
        submission_obj.save()

    return redirect('/portal/home')


@login_required(login_url='/')
def form_data(request):
    if not ACEUserProfile.objects.filter(name=request.user).exists():
        return render(request, 'portalapp/form.html')
    else:
        return redirect('/portal/home')


@login_required(login_url='/')
def form_input(request):
    phone = str(request.POST['phone']).strip()[-10:]
    enroll_number = request.POST['roll']
    course = request.POST['course']
    email_id = request.POST['email']
    section = str(request.POST['section'])[:-5]

    github = request.POST.get('github', None)
    linkedin = request.POST.get('linkedin', None)
    behance = request.POST.get('behance', None)
    website = request.POST.get('website', None)
    twitter = request.POST.get('twitter', None)
    print(phone, enroll_number, course, email_id, section)

    user = User.objects.get(username=request.user)
    ace_user = ACEUserProfile(name=user, enroll_number=enroll_number, course=course, email_id=email_id,
                              section=section, phone_number=phone, github=github, linkedin=linkedin,
                              behance=behance, website=website,
                              twitter=twitter)
    ace_user.save()

    print("Success")

    return redirect('/portal/home')


@login_required(login_url='/')
def serve_main_page(request):
    tasks = Tasks.objects.all().count()

    return render(request, 'portalapp/main.html',
                  {'fb_image_url': "image", 'first_name': "VIPS-ACE", 'tasks': tasks, 'active_tasks': tasks})
