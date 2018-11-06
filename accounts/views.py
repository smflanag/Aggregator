from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, UpdateView
from django.views.generic.detail import SingleObjectMixin

from accounts.models import User, UserProfile
from articles.models import Article
from .forms import RegistrationForm

def Homepage(request):
    context = {}
    if request.user.is_authenticated:
        site_article_list = Article.objects.filter(topic__members=request.user).order_by('-created_at')
    else:
        site_article_list = Article.objects.all().order_by('-created_at')

    context['site_article_list'] = site_article_list
    return render(request, 'home.html', context)


class LoggedInView(LoginRequiredMixin,TemplateView):
    template_name = 'users_only.html'
    def get(self, request):
        return self.render_to_response({})

    def logout_view(request, *args, ** kwargs):
        from django.utils import timezone
        user = request.User
        profile = user.get_profile()
        profile.last_logout = timezone.now()
        profile.save()
        logout(request, *args, **kwargs)

def SignUp(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

class UpdateProfile(UpdateView,LoginRequiredMixin):



    template_name = 'accounts/user_update.html'
    model = UserProfile
    # fields = ('bio', 'location', 'birthdate')
    # context_object_name = 'userprofile'
    slug_field = UserProfile.user
    #
    def get_redirect_url(self,*args,**kwargs):
        return reverse('accounts:user_profile',kwargs={'slug':self.kwargs.get('UserProfile.user')})

    #
    #
    #
    # def form_valid(self, form):
    #     post = form.save(commit=False)
    #     post.updated_by = self.request.user
    #     post.updated_at = timezone.now()
    #     post.save()
    #     return redirect('topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)


def get_user_profile(request, username):
    context = {}
    profile = User.objects.get(username=username)
    context['profile'] = profile

    user_article_list = Article.objects.filter(created_by_id=profile.id).order_by('-created_at')
    context['user_article_list'] = user_article_list

    return render(request, 'accounts/user_profile.html', context)


