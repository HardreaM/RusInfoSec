from django.contrib import admin
from django.urls import path
from django.urls import include
from home_page.views import index
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView

urlpatterns = [
    path('home_page/', include('home_page.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', PasswordChangeView.as_view(
        template_name='registration/change_password.html'), name='password_change'),
    path('accounts/password_change/done/', PasswordChangeDoneView.as_view(
        template_name='registration/password_changed.html'), name='password_change_done'),
    path('accounts/password_reset/', PasswordResetView.as_view(
        template_name='registration/reset_password.html',
        subject_template_name='registration/reset_subject.txt',
        email_template_name='registration/reset_email.html'),
        name='password_reset'),
    path('accounts/password_reset/done', PasswordResetDoneView.as_view(
        template_name='registration/email_sent.html'),
        name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
        template_name='registration/confirm_password.html'),
        name='password_reset_confirm'),
    path('accounts/reset/done/',
        PasswordResetCompleteView.as_view(
        template_name='registration/password_changed.html'),
        name='password_reset_complete'),
#    path('captcha/', include('captcha.urls')),
    path('social/', include('social_django.urls', namespace='social')),
]
