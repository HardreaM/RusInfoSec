from .models import Article
from .models import Rubric
from .forms import ArticleForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse
from django.http import FileResponse
from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.dates import ArchiveIndexView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

def index(request):
    rubrics = Rubric.objects.all()
    bbs = Article.objects.all()
    paginator = Paginator(bbs, 7)
    if 'page' in request.GET:
    	page_num = request.GET['page']
    else:
    	page_num = 1
    page = paginator.get_page(page_num)
    context = {'rubrics': rubrics, 'page': page, 'bbs': page.object_list}
    return render(request, 'home_page/index.html', context)

class ArticleByRubricView(ListView):
	template_name = 'home_page/by_rubric.html'
	context_object_name = 'bbs'

	def get_queryset(self):
		return Article.objects.filter(rubric=self.kwargs['rubric_id'])

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['rubrics'] = Rubric.objects.all
		context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])

		return context

class ArticleAddView(LoginRequiredMixin,SuccessMessageMixin, FormView):
	template_name = 'home_page/add_article.html'
	form_class = ArticleForm
	#captcha = CaptchaField()
	success_message = 'Статья успешно добавлена'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['rubrics'] = Rubric.objects.all()
		return context

	def form_valid(self, form):
		form.save()
		return super(ArticleAddView, self).form_valid(form)

	def get_form(self, form_class=None):
		self.object = super().get_form(form_class)
		return self.object

	def get_success_url(self):
		return reverse('by_rubric',
			kwargs={'rubric_id': self.object.cleaned_data['rubric'].pk})

class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class ArticleEditView(LoginRequiredMixin, UpdateView):
	model = Article
	form_class = ArticleForm
	success_url = '/'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['rubrics'] = Rubric.objects.all()
		return context

	def get_success_url(self):
		return reverse('index')
	

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
	model = Article
	success_url = '/'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['rubrics'] = Rubric.objects.all()
		return context

	def get_success_url(self):
		return reverse('index')

class ArticleIndexView(ArchiveIndexView):
	madel = Article
	date_field = 'published'
	template_name = 'home_page/index.html'
	context_object_name = 'bbs'
	allow_empty = True
	
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['rubrics'] = Rubric.objects.all()
		return context
