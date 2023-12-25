import pandas as pd
from datetime import datetime

def tanggal():
    time_stamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    listtanggal.append(time_stamp)
def tujuan():
    print('1. Bank \n2. Pembayaran \n3. Top up E-Wallet')
    jenistransaksi=input('Masukan Jenis Transaksi: ')
    if jenistransaksi == '1':
        print('\n1. Sesama Bank \n2. Beda Bank')
        tipetransaksi=input('Masukan jenis pembayaran:')
        if tipetransaksi == '1':
            print('\n1. BRI \n2. BNI')
            tujuan=input('Masukan Tujuan: ')
            if tujuan == '1':
                listtujuan.append('BRI')
                print('\n1. Setoran Tunai \n2. Tarik Tunai')
                jenispembayaran=input('Masukan jenis pembayaran: ')
                if jenispembayaran == '1':
                    listjenis.append('Setoran tunai')
                if jenispembayaran == '2':
                    listjenis.append('Tarik tunai')
            if tujuan == '2':
                listtujuan.append('BNI')
                print('\n1. Setoran Tunai \n2. Tarik Tunai')
                jenispembayaran=input('Masukan jenis pembayaran: ')
                if jenispembayaran == '1':
                    listjenis.append('Setoran tunai')
                if jenispembayaran == '2':
                    listjenis.append('Tarik tunai')
        if tipetransaksi == '2':
            print('\n1. BCA \n2. Mandiri \n3. BSI \n4. Bank Lainnya')
            tujuan=input('Masukan Tujuan: ')
            if tujuan == '1':
                listtujuan.append('BCA')
                print('\n1. Setoran Tunai \n2. Tarik Tunai')
                jenispembayaran=input('Masukan jenis pembayaran: ')
                if jenispembayaran == '1':
                    listjenis.append('Setoran tunai')
                if jenispembayaran == '2':
                    listjenis.append('Tarik tunai')
            if tujuan == '2':
                listtujuan.append('Mandiri')
                print('\n1. Setoran Tunai \n2. Tarik Tunai')
                jenispembayaran=input('Masukan jenis pembayaran: ')
                if jenispembayaran == '1':
                    listjenis.append('Setoran tunai')
                if jenispembayaran == '2':
                    listjenis.append('Tarik tunai')
            if tujuan == '3':
                listtujuan.append('BSI')
                print('\n1. Setoran Tunai \n2. Tarik Tunai')
                jenispembayaran=input('Masukan jenis pembayaran: ')
                if jenispembayaran == '1':
                    listjenis.append('Setoran tunai')
                if jenispembayaran == '2':
                    listjenis.append('Tarik tunai')
            if tujuan == '4':
                listtujuan.append('Bank Lainnya')
                print('\n1. Setoran Tunai \n2. Tarik Tunai')
                jenispembayaran=input('Masukan jenis pembayaran: ')
                if jenispembayaran == '1':
                    listjenis.append('Setoran tunai')
                if jenispembayaran == '2':
                    listjenis.append('Tarik tunai')
    if jenistransaksi == '2':
        print('\n1. PLN \n2. Token \n3. Pulsa \n4. Kartu Kredit \n5. Pinjol \n6. Others')
        tujuan=input('Masukan Tujuan: ')
        if tujuan == '1':
            listtujuan.append('PLN')
            listjenis.append('Setoran tunai')
        if tujuan == '2':
            listtujuan.append('Token')
            listjenis.append('Setoran tunai')
        if tujuan == '3':
            listtujuan.append('Pulsa')
            listjenis.append('Setoran tunai')
        if tujuan == '4':
            listtujuan.append('Kartu Kredit')
            print('\n1. Setoran Tunai \n2. Tarik Tunai')
            jenispembayaran=input('Masukan jenis pembayaran: ')
            if jenispembayaran == '1':
                listjenis.append('Setoran tunai')
            if jenispembayaran == '2':
                listjenis.append('Tarik tunai')
        if tujuan == '5':
            listtujuan.append('Pinjol')
            listjenis.append('Setoran tunai')
        if tujuan == '6':
            listtujuan.append('Others')
            listjenis.append('Setoran tunai')
    if jenistransaksi == '3':
        print('\n1. GoPay \n2. OVO \n3. DANA \n4. SPay \n5. Link Aja \n6. Others')
        tujuan=input('Masukan Tujuan: ')
        if tujuan == '1':
            listtujuan.append('GoPay')
            listjenis.append('Setoran tunai')
        if tujuan == '2':
            listtujuan.append('OVO')
            listjenis.append('Setoran tunai')
        if tujuan == '3':
            listtujuan.append('DANA')
            listjenis.append('Setoran tunai')
        if tujuan == '4':
            listtujuan.append('SPay')
            listjenis.append('Setoran tunai')
        elif tujuan == '5':
            listtujuan.append('Link Aja')
            listjenis.append('Setoran tunai')
        elif tujuan == '6':
            listtujuan.append('Others')
            listjenis.append('Setoran tunai')
def norek():
    norek=input('\nMasukan nomer rekening tujuan: ')
    listnorek.append(norek)
def nama():
    nama=input('Masukan nama penerima: ')
    listnama.append(nama)
def total():
    totalkirim=int(input('Masukan jumlah pengiriman: '))
    listtotal.append(totalkirim)
    if totalkirim < 500000:
        listadmin.append(3000)
    elif totalkirim >= 500000 and totalkirim < 1000000:
        listadmin.append(6000)
    elif totalkirim >= 1000000 and totalkirim < 2000000:
        listadmin.append(10000)
    elif totalkirim >= 2000000 and totalkirim < 10000000:
        listadmin.append(30000)
    elif totalkirim >= 10000000 and totalkirim < 20000000:
        listadmin.append(40000)
    elif totalkirim >= 20000000 and totalkirim < 50000000:
        listadmin.append(50000)
    elif totalkirim >= 50000000 and totalkirim < 100000000:
        listadmin.append(100000)
        
listtanggal=[]    
listtujuan=[]
listjenis=[]
listnorek=[]
listnama=[]
listtotal=[]
listadmin=[]

datatransfer={'Tanggal' : listtanggal, 'Bank' : listtujuan, 'Jenis pembayaran' : listjenis, 'Nomer Rekening' : listnorek, 'Nama Penerima' : listnama, 'Jumlah Pengiriman' : listtotal, 'Biaya Admin' : listadmin,}

while True:
    print('\n=====> PROGRAM INPUT DATA TRANSFER <=====')
    tanggal()
    tujuan()
    norek()
    nama()
    total()
    lagi=input('\nMasih ingin melanjutkan (y atau t): ')
    if lagi == 't' or lagi == 'T':
        break

df=pd.DataFrame.from_dict(datatransfer)
writer=pd.ExcelWriter('datatransfer.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Transfer', index=False)
writer.save()