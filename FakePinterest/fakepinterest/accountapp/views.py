from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world')) #reverse: 해당하는 경로를 다시 만들어줌

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm #html의 {{ form }}으로 바로 만들어줌
    # 경로에 성공하면 어느 경로로 갈지 다시 지정해야 함
    # class에서는 reverse를 사용할 수 없음/class형 뷰에서 reverse_lazy 사용
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'