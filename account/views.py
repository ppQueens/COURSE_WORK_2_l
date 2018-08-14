from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_POST

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .util import TokenGenerator
from django.db import transaction
from django.views.decorators.http import require_POST
from customer.models import Customer
from django.contrib.auth.hashers import make_password

account_activation_token = TokenGenerator()


@require_POST
def user_login(request):
    print(request.POST)
    # if request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid():
        clean = form.cleaned_data
        user = authenticate(request, username=clean["username"], password=clean["password"])

        if user is not None:
            if user.is_active:
                login(request, user)
                customer = Customer.objects.filter(customer=user).get()
                return render(request, "account/user_anon.html", {"user": user})
            else:
                return HttpResponse("Disabled account", content_type='text')

        else:
            return HttpResponse("Неверный логин или пароль", content_type='text')
            # return HttpResponse("")


def user_logout(request):
    print(request.GET)

    logout(request)
    return render(request, "account/user_anon.html", {"user": None})


@transaction.atomic()
def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(username=user_form.cleaned_data["email"],
                                                email=user_form.cleaned_data["email"], is_active=False,
                                                password=make_password(user_form.cleaned_data["password"]))

            customer = Customer(customer=new_user, customer_type=1, fl_name=request.POST.get("full_name"),
                                phone=user_form.clean_phone_number())
            new_user.save()
            customer.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('account/acc_active_email.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)).decode("ascii"),
                'token': account_activation_token.make_token(new_user),
            })

            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration.'
                                '<script>\
                                  window.setTimeout(function(){\
                                    window.location.href = "/new_test";\
                                  }, 3000);\
                                </script>')
    else:
        user_form = UserRegistrationForm()

    print(user_form.errors)
    return render(request, 'account/register.html', {"form": user_form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        return HttpResponse('Thank you for your email confirmation. Now you can login your account.<script>\
                          window.setTimeout(function(){\
                            window.location.href = "/new_test";\
                          }, 3000);\
                        </script>')
    else:
        return HttpResponse('Activation link is invalid!')
