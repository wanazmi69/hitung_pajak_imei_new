from django.shortcuts import render

import requests
import json



def index(request):



    if request.method == ('POST'):
        # mataUang = request.POST['mata_uang']
        # hargaBarang = float(request.POST['masukanHarga'])
        mataUang = request.POST.get('mata_uang')
        hargaBarang = request.POST.get('masukanHarga')
        url_convert = f'https://api.apilayer.com/exchangerates_data/convert?to=USD&from={mataUang}&amount=5'
        url_base = 'https://api.apilayer.com/exchangerates_data/convert?to=IDR&from=USD&amount=5'
        payload = {}
        header = {
            "apikey": "QEq5U0gxSpmDorxvUz9kPOH8pF3GVJnG"
        }
        linkAPI = requests.request('GET', url_convert, headers= header, data = payload)
        linkAPI_RP = requests.request('GET', url_base, headers= header, data = payload)

        convertRP = linkAPI_RP.json()
        convertBase = linkAPI.json()
        nilaiMataUang = float(convertBase["info"]["rate"])
        kursRP = float(convertRP["info"]["rate"])

        hasil_USD = float(hargaBarang) * nilaiMataUang

        if hasil_USD > 500:
            kepabenan = hasil_USD - 500
            pabean = kepabenan * kursRP  # konveri ke Rupiah

            beaMasuk = pabean * 10/100

            nilaiImpor = pabean + beaMasuk

            PPN = nilaiImpor * 10/100

            # di sini masukan loop tombol npwp
            if request.POST.getlist('ya'):
                PPh = nilaiImpor * 10/100
            else:
                PPh = nilaiImpor * 20/100

            total = beaMasuk + PPN + PPh

            hasil = 'Rp. {:0,.0f}'.format(total)

        else:
            kepabenan = 0
            hasil = "HPmu Bebas Pajak"

    else:
        mataUang = ""
        hasil = ""
        baca = ""

    context = {
        'iniHasilnya': hasil,
        'matauang': mataUang,
        'title': 'Kalkulator',
        'judul': 'IMEI',
        'npwp': 'Memiliki NPWP ',
        'subjudul': 'Kalkulator Hitung Pajak HP',
        'hasil': 'Pajak HPmu',
    }

    return render(request, 'index.html', context)



