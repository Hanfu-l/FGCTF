from functools import wraps
from django.http import HttpResponseForbidden

def IsTrueUser(view_func):
    @wraps(view_func)  # 使用 functools.wraps 修饰以保留原始函数的元数据
    def wrapper(request, *args, **kwargs):
        # 在视图函数之前执行的操作
        if some_condition:  # 这里可以根据需要添加条件
            return HttpResponseForbidden("Access denied")  # 返回一个拒绝访问的响应

        # 调用原始视图函数
        return view_func(request, *args, **kwargs)

    return wrapper

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        flag=request.user.is_superuser
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden(request.user.is_authenticated)
    return _wrapped_view




