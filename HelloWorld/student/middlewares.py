# coding:utf-8
import time

from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse


class TimeItMiddleware(MiddlewareMixin):

    #可以在这个函数中做一些校验，比如用户登录，或者HTTP中是否有认证头之类的验证
    #如果返回HttpResponse，那么接下来的处理方法只会执行process_response，其他的方法将不会被执行。
    #返回none，那么Django会继续执行其他的方法。
    def process_request(self, request):
        return

    #func是将要执行的view方法
    #返回None，那么Django会帮你执行view函数，从而得到最终的Response。
    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('index'):
            return None

        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('{:.2f}s'.format(costed))
        return response

    #只有在发生异常时，才会进入到这个方法
    #简单的理解为在将要调用的view中出现异常（就是在process_view的func函数中）或者返回的模板Response在render时发生的异常，会进入到这个方法中
    #可以选择处理异常，然后返回一个含有异常信息的HttpResponse，或者直接返回None，不处理，这种情况Django会使用自己的异常模板。
    def process_exception(self, request, exception):
        pass

    #针对带有模板的response的处理
    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        return response