from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from library.models import Assignment, Resources, Categories
from portalapp.models import ACEUserProfile

from library.utils import fetch_attendance


def index(request):
    if request.user.is_authenticated:
        try:
            profile = ACEUserProfile.objects.get(name=request.user)
        except ACEUserProfile.DoesNotExist:
            profile = None
        if not profile:
            return redirect('/portal')
        if profile.is_member:
            count, total, not_attended, attended = fetch_attendance(request)
            membership = ACEUserProfile.objects.get(name=request.user).get_membership()
            return render(request, template_name='library/home.html', context={'total': total, 'count': count,
                                                                               'not_attended': not_attended,
                                                                               'attended': attended, 'membership': membership})

    return render(request, 'library/index.html')


@login_required(login_url='/')
def resources(request):
    categories = Categories.objects.all()
    membership = ACEUserProfile.objects.get(name=request.user).get_membership()
    return render(request, 'library/resource.html',
                  {'categories': categories, 'count': len(categories), 'membership': membership})


@login_required(login_url='/')
def assignment(request):
    assignments = Assignment.objects.all()
    membership = ACEUserProfile.objects.get(name=request.user).get_membership()
    return render(request, 'library/assignments.html', {'assignments': assignments, 'membership': membership})


@login_required(login_url='/')
def resource_details(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    resources = Resources.objects.filter(category=category)

    name = str(request.user.first_name) + " " + str(request.user.last_name)
    membership = ACEUserProfile.objects.get(name=request.user).get_membership()
    return render(request, 'library/resource_detail.html',
                  {'resources': resources, 'category': category,
                   'membership': membership})
