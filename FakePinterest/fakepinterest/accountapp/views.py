from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.decorators import account_ownership_required


has_ownership = [account_ownership_required, login_required]


@login_required
def hello_world(request):
    if request.method == "post":

        temp = request.post.get('hello_world_input')

        new_hello_world = helloworld()
        new_hello_world.text = temp
        new_hello_world.save()

        return httpresponseredirect(reverse('accountapp:hello_world')) #reverse: 해당하는 경로를 다시 만들어줌
    else:
        hello_world_list = helloworld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

    """else: #로그인하지 않았을 때
        return HttpResponseRedirect(reverse('accountapp:login'))"""

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm #html의 {{ form }}으로 바로 만들어줌
    # 경로에 성공하면 어느 경로로 갈지 다시 지정해야 함
    # class에서는 reverse를 사용할 수 없음/class형 뷰에서 reverse_lazy 사용
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

#일반 function에 사용하는 decorator를 메소드에서 사용 가능하게 변환해주는 데코레이터
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
#@method_decorator(account_ownership_required, 'get')
#@method_decorator(account_ownership_required, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    """
    def get(self, *args, **kwargs):
        #pk에 해당하는 object를 가져옴 => pk에 해당하는 유저 객체가 request를 보내고 있는 유저와 같은지 확인
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()"""

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
    """
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden() #금지된 곳에 접근

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()"""
