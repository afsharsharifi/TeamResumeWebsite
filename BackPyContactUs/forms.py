from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام و نام خانوادگی', 'class': 'form-control'}),
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(
                150, 'نام و نام خانوادگی شما نمیتواند بیشتر از 150 کاراکتر باشد')
        ]
    )
    
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'شماره تلفن', 'class': 'form-control'}),
        label='شماره تلفن',
        validators=[
            validators.MaxLengthValidator(
                11, 'شماره تلفن  شما نمیتواند بیشتر از 11 کاراکتر باشد')
        ]
    )



    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'ایمیل', 'class': 'form-control'}),
        label='ایمیل',
        validators=[
            validators.MaxLengthValidator(
                100, 'ایمیل شما نمیتواند بیشتر از 100 کاراکتر باشد')
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'عنوان', 'class': 'form-control'}),
        label='عنوان',
        validators=[
            validators.MaxLengthValidator(
                200, 'عنوان پیام شما نمیتواند بیشتر از 200 کاراکتر باشد')
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'متن پیام', 'class': 'form-control'}),
        label='متن پیام'
    )
