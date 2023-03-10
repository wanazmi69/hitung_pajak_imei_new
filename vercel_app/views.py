from django.shortcuts import render

import requests
import json



def index(request):





    # print(int(jsondata['kurs']['USD']))
    # print(url_base.json())
    # url_rp = 'https://scraping.getundangan-pernikahan.space/api/kurs?amount=1&from=usd&to=idr'
    # response_url_convert_to_rp = requests.get(url_rp)
    # convertRP = response_url_convert_to_rp.json()
    # print(convertRP['kurs'])

    if request.method == ('POST'):
        mataUang = request.POST.get('mata_uang')
        hargaBarang = request.POST.get('masukanHarga')


        # url_rp = 'https://kurs.getundangan-pernikahan.space/api/kurs?amount=1&from=usd&to=idr'

        url_rp = 'https://kurs-scraping.vercel.app/api/kurs?amount=1&to=idr&from=usd'

      
        url_convert = f'https://kurs-scraping.vercel.app/api/kurs?amount=1&to=usd&from={mataUang}'
        response_url_convert_to_rp = requests.get(url_rp)
        response_url_base = requests.get(url_convert)

        convertRP = response_url_convert_to_rp.json()
        convertUSD = response_url_base.json()

    
        kursRP = float(convertRP['kurs2']) # url_rp
        print(kursRP)
        nilaiMataUang = float(convertUSD['kurs2']) #url_convert

        hasil_USD = int(hargaBarang) * nilaiMataUang

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
            # hasil = 'Rp. ', total
      

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



