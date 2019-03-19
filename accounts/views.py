from time import timezone

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from requests import Response
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser

from accounts.models import User, UserProfile
from accounts.serializers import CreateUserSerializer, LoginUserSerializer
from articles.models import Article
from articles.serializers import ArticleSerializer, UserProfileSerializer, UserSerializer
from .forms import RegistrationForm, ContactForm


def Homepage(request):
    context = {}
    # if request.user.is_authenticated:
    #     site_article_list = Article.objects.filter(topic__members=request.user).order_by('-created_at')
    # else:
    #     site_article_list = Article.objects.all().order_by('-created_at')
    #
    # context['site_article_list'] = site_article_list
    form_class = ContactForm
    context['form'] = form_class


    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        }
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" + '',
            ['youremail@gmail.com'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('home')

    return render(request, 'home.html', context)

def article_list(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user_id = request.user.id
            articles = Article.objects.filter(topic__members=user_id).order_by('-created_at')
            serializer = ArticleSerializer(articles, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            articles =  Article.objects.all().order_by('-created_at')
            serializer = ArticleSerializer(articles, many=True)
            return JsonResponse(serializer.data, safe=False)

# def js_topic_list(request):
#     if request.method == 'GET':
#         topics = Topic.objects.all()
#         yourdata =[]
#         for topic in topics:
#             topic_id = topic.id
#             topic_name = topic.topic_name
#             members = topic.members.filter(topic=topic_id)
#             articles = Article.objects.filter(topic_id=topic_id).count()
#             yourdata.append(
#                 {"id":topic_id,
#                  "topic_name":topic_name,
#                  "articles":articles,
#                 "members":members})
#         serializer=[]
#         for data_thing in yourdata:
#             serializer.append(TopicSerializer(data_thing).data)
#     return Response(serializer)


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
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password')

    slug_field = 'username'


    def form_valid(self, form):
        profile_page = form.save(commit=False)
        profile_page.username = self.request.username
        profile_page.first_name = self.request.first_name
        profile_page.last_name = self.request.last_name
        profile_page.updated_at = timezone.now()
        profile_page.save()
        return redirect('user_profile', slug=profile_page.user.username)


def get_user_profile(request, username):
    context = {}
    profile = User.objects.get(username=username)
    context['profile'] = profile

    user_article_list = Article.objects.filter(created_by_id=profile.id).order_by('-created_at')
    context['user_article_list'] = user_article_list

    return render(request, 'accounts/user_profile.html', context)

from articles.serializers import ContactSerializer
@csrf_exempt
def js_contact(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class UserViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return User.objects.all()

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def get_current(self, request):
        current_user = User.objects.filter(user_id=request)
        serializer = UserSerializer(current_user)
        return Response(serializer.data)

    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()

from rest_framework import permissions, generics
from rest_framework.response import Response

from knox.models import AuthToken


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user