from django.http import HttpResponseForbidden

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You don't have permission to access.")
    return _wrapped_view
