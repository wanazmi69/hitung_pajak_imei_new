from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'fProfile': 'img/profil.png',
        'title': 'Profilku',
        'judul': 'IMEI',
        'nama': 'Wan Azmi',
        'negara': 'Indonesia',
        'tinggal': 'Osaka - Jepang',

        'iconIG': 'img/media/ig.png'

    }

    return render(request, 'profil/index.html', context)
