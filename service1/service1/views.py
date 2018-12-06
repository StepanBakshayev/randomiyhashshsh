from django import forms
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, redirect

from .models import Function


def main(request):
	function_query = Function.objects.all()
	paginator = Paginator(function_query, 25)
	page = request.GET.get('page')
	functions = paginator.get_page(page)
	return render(request, 'main.html', {'functions': functions})


class AddForm(forms.Form):
	type = forms.ChoiceField(
		choices=tuple((member.value, member.value) for member in Function.Type),
		widget=forms.RadioSelect)
	interval = forms.IntegerField(min_value=1)
	dt = forms.IntegerField(min_value=1)


def add(request):
	form = AddForm(data=request.POST or None)
	if form.is_valid():
		with transaction.atomic():
			Function.objects.create(**form.cleaned_data)
		return redirect('main')

	return render(request, 'add.html', {'form': form})
