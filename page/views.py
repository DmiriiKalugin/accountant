from django.shortcuts import render
from .models import *

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SendForm
from accountant.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


def index(request):
    default_contact = DefaultContact.objects.all()
    contact = Contact.objects.all()
    service = Services.objects.all()

    # если метод GET, вернем форму
    if request.method == 'GET':
        form = SendForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = SendForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']
            try:
                send_mail(f'Сообщение от {email}', f'Новая заявка с сайта nip66.ru: \n'
                                                   f' Имя: {name} \n'
                                                   f' Номер телефона: {number} \n'
                                                   f' Сообщение: {message}',
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(
        request,
        'index.html',
        {
            'service': service,
            'default': default_contact,
            'contact': contact,
            'form': form
        }
    )


def success_view(request):
    return render(request, 'success.html')