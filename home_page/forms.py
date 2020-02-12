from django import forms
from .models import Article
from django.forms import ModelForm
#from captcha.fields import CaptchaField

class ArticleForm(ModelForm):
#    captcha = CaptchaField()
    class Meta:
        model = Article
        fields = ('title', 'content', 'rubric')
