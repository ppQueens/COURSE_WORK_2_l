from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode




def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/new_test/", {"user": ""})


def all_(q_lst):
    return set.intersection(*map(lambda x: set(*x), q_lst))


def cat_proc_view(request):
    pass



def handler404(request,exception, template_name='404.html'):
    response = render_to_response(template_name, {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


