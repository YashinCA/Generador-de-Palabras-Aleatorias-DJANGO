from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):
    return redirect('/random_word')


def random_word(request):
    if request.method == 'GET':
        request.session['contador'] = 0
        request.session['palabra'] = ""
        return render(request, 'app/index.html')

    if request.method == 'POST':
        request.session['contador'] += 1
        request.session['palabra'] = get_random_string(length=14)
        print(request.POST)
        context = {
            'palabra': get_random_string(length=14),
            'contador': request.session['contador']
        }
        return render(request, 'app/index.html', context)


def reset(request):
    request.session['contador'] = 0
    request.session['palabra'] = ""
    return redirect('/')
