# -*- coding: utf-8 -*-
from django import forms
from project.core.models import Need


class NeedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NeedForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'placeholder': 'Ваше Имя', 'class': 'form-control floating-label'}

        self.fields['phone'].widget.attrs = {
            'placeholder': 'Ваш телефон',
            'class': 'form-control floating-label'}

        self.fields['email'].widget.attrs = {
            'placeholder': 'Ваша почта',
            'class': 'form-control floating-label'}

        self.fields['text'].widget.attrs = {
            'placeholder': 'Опишите Вашу нужду',
            'class': 'form-control floating-label'}

    class Meta:
        model = Need


class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'placeholder': 'Ваше Имя', 'class': 'form-control floating-label'}

        self.fields['phone'].widget.attrs = {
            'placeholder': 'Ваш телефон (не обязательно)',
            'class': 'form-control floating-label'}

        self.fields['text'].widget.attrs = {
            'placeholder': 'Ваше Вопрос',
            'class': 'form-control floating-label'}

    name = forms.CharField(widget=forms.TextInput)
    phone = forms.CharField(widget=forms.TextInput, required=False)
    text = forms.CharField(widget=forms.Textarea)
