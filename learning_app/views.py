from django.shortcuts import render


def index(request):

    name_mountain = 'Hello, Mountains!!!'
    context = {
        'message': name_mountain
    }
    return render(request, 'index.html', context=context)


def send_email(request):
    if request.method == 'POST':
        print(request.POST)
    context = {}
    return render(request, 'send-email.html', context=context)
