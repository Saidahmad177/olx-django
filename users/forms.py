from django import forms

from users.models import CustomUser


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        error_messages={
            'required': "Bu maydonni to'ldirish talab etiladi",
            'invalid': "Iltimos to'g'ri qiymat kiriting",
            'unique': "Username allaqachon mavjud!",
        }
    )
    first_name = forms.CharField(
        error_messages={
            'required': "Bu maydonni to'ldirish talab etiladi"
        }
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user
