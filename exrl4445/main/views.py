from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import ExtraArgumentForm
from .models import Arguments


def input_form(request):
    arguments = ['name']
    extra_arguments = request.GET.get('extra', [])

    if extra_arguments:
        extra_arguments = extra_arguments.split()
        arguments.extend(extra_arguments)

    if request.method == 'POST':
        extra_arg_form = ExtraArgumentForm(request.POST)

        if extra_arg_form.is_valid():
            extra_arguments.append(extra_arg_form.cleaned_data['extra'])
            return redirect(f'/?extra={"+".join(extra_arguments)}')

    else:
        extra_arg_form = ExtraArgumentForm()

    return render(request, 'main/input_form.html', {'arguments': arguments, 'extra_arg_form': extra_arg_form})


def add_arguments_to_db(request):
    arguments = {key: value for key, value in request.POST.items() if key != 'csrfmiddlewaretoken'}
    # arguments = {}
    # for key, value in request.POST.items():
    #     if key == 'csrfmiddlewaretoken':
    #         continue
    #     arguments |= {key: value}
    args = Arguments(arguments=arguments)
    args.save()
    return redirect('input_form')


class ArgumentsList(ListView):
    model = Arguments
    # template_name = 'main/arguments_list'
    context_object_name = 'arguments'

    def get_queryset(self):
        return Arguments.objects.all()
