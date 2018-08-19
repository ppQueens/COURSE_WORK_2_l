from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm, PersonalInfoChange
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
from django.contrib.auth.decorators import login_required
from customer.models import Customer
from django.contrib.auth.hashers import make_password
from order.models import Order
from django.db.models import Q
from comment.models import Comment

account_activation_token = TokenGenerator()


# @require_POST

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/new_test")
    if request.method == "POST":
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
    if request.GET.get("login") == "bar":
        popover_place = '<div role="button" class="from-server d-block" data-toggle="popover" data-placement="right"></div>'
        return render(request, "account/login_form.html", locals())
    return render(request, "account/login_page.html", {})


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


@login_required(login_url="/account/login")
def user_profile(request):
    return render(request, "profile.html", locals())


@login_required(login_url="/account/login")
def user_order_history(request):
    orders = Order.objects.filter(customer__customer_id=request.user.id)

    return render(request, "order_history.html", locals())


@login_required(login_url="/account/login")
def user_comment_history(request):
    comments = Comment.objects.filter(Q(phone_email=request.user.email) | Q(phone_email=request.user.customer.phone))
    one_item__oneOrMore_comment = dict()

    for comment in comments:
        if not one_item__oneOrMore_comment.get(comment.item):
            one_item__oneOrMore_comment[comment.item] = [comment]
        else:
            one_item__oneOrMore_comment[comment.item].append(comment)

    print(one_item__oneOrMore_comment)
    return render(request, "comment_history.html", locals())


@login_required(login_url="/account/login")
def user_pesonal_info(request):
    print(make_password('mariadontberude'))
    if request.method == "POST":
        change_form = PersonalInfoChange(request.POST, user=request.user)
        if change_form.is_valid():
            update_user = request.user
            update_user.email = change_form.cleaned_data["email"]
            print(change_form.cleaned_data["phone"])
            update_user.customer.phone = change_form.cleaned_data["phone"]
            if change_form.cleaned_data["new_pass"]:
                update_user.password = make_password(change_form.cleaned_data["new_pass"])
            update_user.customer.save()
            update_user.save()
            # if not change_form.cleaned_data["new_pass"]:
            #     logout(request)
            return HttpResponseRedirect("/account/profile/personal_info")
            # return render(request,"personal_info.html",locals())


    else:
        change_form = PersonalInfoChange()
    user = request.user
    print(change_form.errors)
    return render(request, "personal_info.html", locals())
