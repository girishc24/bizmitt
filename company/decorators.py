from functools import wraps  # Import wraps from functools
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.http import HttpResponseForbidden

def group_required(group_name):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                group = Group.objects.get(name=group_name)
                if group in request.user.groups.all():
                    return view_func(request, *args, **kwargs)
                else:
                    # If user doesn't belong to the required group, redirect or raise an exception
                    return HttpResponseForbidden("You don't have permission to access this page.")
            else:
                # If user is not authenticated, redirect to login page
                return redirect('companylogin')
        return wrapper
    return decorator
