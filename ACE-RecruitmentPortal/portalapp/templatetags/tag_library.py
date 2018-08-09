from django import template

register = template.Library()


@register.filter()
def test_function(task, user):
    try:
        if task.get(name=user):
            return "Completed"
    except:
        return "Incomplete"


@register.filter()
def is_true(task, user):
    try:
        if task.get(name=user):
            print("True")
            return 1
    except:
        return 0
        print("False")
