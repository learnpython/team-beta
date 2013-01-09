# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from profile.models import UserProfile


class MyUserCreateForm(UserCreationForm):
    # email = forms.EmailField(label="Email")
    # fullname = forms.CharField(label="Имя, Фамилия")

    class Meta:
        model = User
        fields = ("username",
                # "fullname",
                "email",
                "password1",
                "password2",
                )


class MyUserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ("mobile",
            "mobile_code",
            "user_contr",
            )


class MyUserForm(ModelForm):

    class Meta:
        model = User
        fields = ("first_name",
            "last_name",
            "email",
            )

# class ContragentForm(ModelForm):

#     class Meta:
#         model = Contragent
#         fields = ("contr_name",
#             "contr_phone",
#             "contr_detail",
#             "contr_region",
#             "contr_city",
#             "contr_city_code",
#             "contr_street",
#             "contr_building",
#             "contr_zipcode",
#             )
