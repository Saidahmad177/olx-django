from django import forms

from users.models import CustomUser


class RegisterForm(forms.ModelForm):
    phone_number = forms.IntegerField(
        min_value=100000000, max_value=999999999,
        error_messages={
            'required': "Bu maydonni to'ldirish talab qilinadi",
            "invalid": "Iltiomos to'g'ri raqam kiriting!",
            'unique': "Bu telefon raqami allaqachon mavjud!",
            'max_value': "Raqam 9tadan ko'p yoki kam bo'lmasligi kerak",
            'min_value': "Raqam 9tadan ko'p yoki kam bo'lmasligi kerak",
        },

    )

    username = forms.CharField(
        error_messages={
            'required': "Bu maydonni to'ldirish talab etiladi",
            'invalid': "Iltimos to'g'ri qiymat kiriting",
            'unique': "Bu Username allaqachon mavjud!",
        }
    )
    first_name = forms.CharField(
        error_messages={
            'required': "Bu maydonni to'ldirish talab etiladi"
        }
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'phone_number')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user


class ProfileForm(forms.ModelForm):
    username = forms.CharField(
        error_messages={
            'required': "Bu maydonni to'ldirish talab etiladi",
            'unique': 'Bunday username allaqachon mavjud!',
            'invalid': "Iltimos to'g'ri qiymat kiriting. "
                       "Faqat harflar, raqamlar va @/./+/-/_ belgilaridan iborat bo'lishi mumkin.",
        }
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email')
