from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse, reverse_lazy
from products.models import Basket
from users.models import User
from django.contrib.auth.views import LoginView
from common.views import TitleMixin


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):  # страница регистрации
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = "Вы успешно зарегестрировались!"
    title = 'Store - Регистрация'


class UserProfileView(TitleMixin, UpdateView):  # формируем профиль пользователя
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('user:profile', args=(self.object.id))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context
