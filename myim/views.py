from django.shortcuts import render

import requests


class pajak():

    def index(request):

        if request.method == ('POST'):
            mataUang = request.POST['mata_uang']
            hargaBarang = float(request.POST['masukanHarga'])
            linkAPI = requests.get(
                f'https://free.currconv.com/api/v7/convert?q={mataUang}&compact=ultra&apiKey=9006dcb72b6464e75d5d')
            linkAPI_RP = requests.get(
                'https://free.currconv.com/api/v7/convert?q=USD_IDR&compact=ultra&apiKey=9006dcb72b6464e75d5d')

            ambilMataUang = linkAPI.json()
            nilaiMataUang = float(ambilMataUang[mataUang])
            hitungAPI = linkAPI_RP.json()

            kursRP = float(hitungAPI['USD_IDR'])

            hasil_USD = hargaBarang * nilaiMataUang

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

                hasil = 'Rp. {:,.2f}'.format(total)

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


ini = pajak
ini.index
