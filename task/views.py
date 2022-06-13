from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView

from tools.tools import Color
from tools.quadratic_equations import quadratic_eq
from .forms import InputIndexForm, InputABCForm


class ColorView(FormView):
    form_class = InputIndexForm
    template_name = 'test2.html'
    color = Color()

    def get_context_data(self, **kwargs):
        kwargs.update({
            'color': self.color.current_color,
            'color_len': self.color.current_len
        })
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if form.data.get('flag'):
            self.color.refresh()
        self.color.get_color(index=int(form.data['index']))
        return redirect('color')


class QuadraticEq(FormView):
    form_class = InputABCForm
    template_name = 'test1.html'

    def form_valid(self, form):
        answer = quadratic_eq(float(form.data['a']), float(form.data['b']), float(form.data['c']))
        if isinstance(answer, str):
            return JsonResponse({str('answer'): str('no roots')})
        temp_dict_to_return = {}
        for index, item in enumerate(answer):
            temp_dict_to_return[f'x{index + 1}'] = item
        return JsonResponse({str('answer'): temp_dict_to_return})
