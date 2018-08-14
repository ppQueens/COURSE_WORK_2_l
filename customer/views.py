from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .forms import NewUserValidation
from .token import TokenGenerator
from .models import Customer
from django.db import transaction
from django.views.decorators.http import require_POST
account_activation_token = TokenGenerator()


@require_POST
def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username and username.isdigit():
        username, *_ = Customer.objects.filter(phone=int(username)).values_list("customer__username",flat=True)

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/new_test/", {"user": user})

    return render(request, "main.html")



def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/new_test/")
    return render(request, "reg_form.html")

#
@transaction.atomic()
def register(request):
    print(request.POST)
    form = NewUserValidation(request.POST)

    if form.is_valid():
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username=email,
                                        email=email,
                                        password=password)
        user.is_active = False
        customer = Customer(customer=user,customer_type=1,fl_name=username)
        user.save()
        customer.save()

        current_site = get_current_site(request)
        mail_subject = 'Activate your blog account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        # to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[email]
        )
        email.send()
        return HttpResponse('Please confirm your email address to complete the registration.'
                            '<script>\
                              window.setTimeout(function(){\
                                window.location.href = "/log_reg";\
                              }, 3000);\
                            </script>')
    return render(request,'reg_form.html', locals())


    # return render(request, '')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        # login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.<script>\
                          window.setTimeout(function(){\
                            window.location.href = "/log_reg";\
                          }, 3000);\
                        </script>')
    else:
        return HttpResponse('Activation link is invalid!')
