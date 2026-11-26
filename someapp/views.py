from django.views.generic import ListView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Course, Request
from .forms import UserWithPhoneCreationForm, RequestForm

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'
    paginate_by = 2 

class MyRegistrationView(CreateView):
    form_class = UserWithPhoneCreationForm
    template_name = "registration.html"
    success_url = reverse_lazy('login') 

class ProfileView(LoginRequiredMixin, ListView):
    model = Request
    template_name = 'profile.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return Request.objects.filter(user=self.request.user).order_by('-created_at')

class CreateRequestView(LoginRequiredMixin, FormView):
    template_name = 'create_request.html'
    form_class = RequestForm
    success_url = reverse_lazy('profile') 

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)