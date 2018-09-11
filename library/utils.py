from website.models import Agenda
from library.models import Attendance


def fetch_attendance(request):
    attendance = Attendance.objects.filter(attended__in=str(request.user.id))
    total = Agenda.objects.all().count()
    attended = [ag.agenda for ag in attendance]
    not_attended = Agenda.objects.exclude(id__in=[att.id for att in attended])

    return len(attendance), total, not_attended, attended