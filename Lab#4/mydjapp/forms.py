# -*- coding: utf-8 -*-
from models import Category, Post
from django import forms
class AddCategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''

    class Meta:
        model = Category
        fields = ['title']
        exclude = None


class AddLotProductsForm(forms.Form):

    txt = forms.CharField(widget = forms.Textarea(attrs={'cols': 50, 'rows': 16}), label="", help_text="")