from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        # user를 안 넣는 이유는 다른 user의 프로필에 접근할 수 있기 때문
        fields = ['image', 'nickname', 'message']