#meminta jawaban user
import random
import msvcrt
import os

def transisi_dan_klik():
    msvcrt.getch()
    os.system('cls')

print("\n-----------------------------")
print("| Welcome to my application |")
print("-----------------------------")
transisi_dan_klik()

print("\n---------------------")
print("| What's your name ? |")
print("----------------------\n")
nama_pemain = input("Your name here: ")
transisi_dan_klik()

print("\n-------------------------------------------")
print("|       Hai {} what's up :)     |".format(nama_pemain))
print("-------------------------------------------\n")

transisi_dan_klik()

kelas_tanya=[] 


driver = 0
analytic = 0
expressive=0
amiable=0

def nomor_pertanyaan():
    nomor_keluar = random.randint(1,10)
    return nomor_keluar

def daftar_pertanyaan(nomor_dari_pertanyaan):
    var = nomor_dari_pertanyaan
    if var == 1:
        print("\n1. Jika saya memiliki keputusan yang penting untuk dibuat, maka...")
        print("   [a] Saya akan memikirkannya sepenuhnya sebelum memutuskan")
        print("   [b] Saya akan menggunakan insting saya untuk memutuskan")
        print("   [c] Saya akan memikirkan pengaruhnya terhadap orang lain terlebih dulu")
        print("   [d] Saya akan menjalankan keputusan dari opini orang yang saya hormati\n")
    elif var == 2:
        print("\n2. Jika orang lain melakukan kesalahan, maka..")
        print("   [a] Saya akan menawarkan bantuan jika saya memang bisa membantu")
        print("   [b] Saya akan membiarkannya, karena saya pikir itu adalah privasinya")
        print("   [c] Saya akan memikirkannya sepenuhnya sebelum memutuskan")
        print("   [d] Saya akan merasa tidak tega dan berharap semoga apa yang dia alami segera berakhir\n")
    elif var == 3:
        print("\n3. Rumah atau ruang kerjaku biasanya terdapat benda seperti..")
        print("   [a] Foto keluarga dan beberapa barang berkesan yang dipajang ")
        print("   [b] Poster yang menginspirasi, penghargaan, dan lukisan seni")
        print("   [c] Projek mendatang atau list tugas yang akan dikerjakan segera")
        print("   [d] Hanya kalendar saja\n")
    elif var == 4:
        print("\n4. Ketika berbicara dengan orang secara langsung, saya biasanya...")
        print("   [a] Melihat matanya agar fokus dengan apa yang dibicarakan ")
        print("   [b] Melihat matanya dan sesekali melihat ke bawah")
        print("   [c] Melihat ke sekeliling ruangan saja")
        print("   [d] Mencoba mempertahankan melihat matanya, namun lebih banyak melihat ke hal yang lain\n")
    elif var == 5:
        print("\n5. Ketika berbicara dengan orang di telefon, maka...")
        print("   [a] Saya akan menjaga fokus percakapan sesuai dengan tujuan utama")
        print("   [b] Saya akan melakukan chatting terlebih dulu sebelum meminta telefon secara langsung")
        print("   [c] Saya tidak akan terburu-buru mematikan telefon dan tidak masalah jika chatting membahas tentang apapun")
        print("   [d] Saya akan menjaga percakapan seperti yang diminta\n")
    elif var == 6:
        print("\n6. Ketika saya menghadiri rapat kerja, maka...")
        print("   [a] Saya akan duduk dan mempertimbangkan berpikir dahulu sebelum mengajukan opini")
        print("   [b] Saya akan mengutarakan semua pendapat saya agar semuanya tahu apa yang saya harapkan")
        print("   [c] Saya akan mengutarakan opini dengan bersemangat juga yakin, namun saya juga menjadi pendengar yang baik")
        print("   [d] Saya akan setuju saja dengan pendapat orang lain\n")
    elif var == 7:
        print("\n7. Jika saya sedang mempunyai masalah dengan orang, maka...")
        print("   [a] Saya akan mencoba menyelesaikannya dengan cara yang baik")
        print("   [b] Saya akan tetap tenang, dan mencoba memahami masalah tersebut")
        print("   [c] Saya akan mencoba menghindari pembicaraan yang akan memicu masalah tersebut")
        print("   [d] Saya akan menghadapinya sehingga masalah bisa cepat selesai dengan cara apapun\n")
    elif var == 8:
        print("\n8. Ketika saya ingin berpendapat lain dengan pendapat orang lain, biasanya...")
        print("   [a] Saya akan mendengar opini mereka terlebih dahulu kemudian menyampaikan pendapat saya dengan tegas")
        print("   [b] Saya akan berusahan menyuarakan pendapat saya dengan meyakinkan itu semua agar orang lain paham \n       dengan apa yang saya ingin")
        print("   [c] Saya akan mencoba membujuk, bernegoisasi, atau mempengaruhi pendapat orang lain tanpa memaksakannya")
        print("   [d] Saya akan menjelaskan secara masuk akal dan jelas terkait apa yang saya ingin\n")
    elif var == 9:
        print("\n9. Ketika saya berbicara di sebuah kelompok kerja, biasanya...")
        print("   [a] Saya sangat pandai melawak dan menarik perhatian orang lain")
        print("   [b] Saya akan sangat jelas dan simpel")
        print("   [c] Saya berbicara jarang sekali dan sedikit")
        print("   [d] Saya akan secara langsung tanpa ragu bersuara dan bernada sedikit keras\n")
    elif var == 10:
        print("\n10. Saya membuat target atau tujuan dalam hidup, dengan cara...")
        print("   [a] Yang saya pikir realistis kalau saya bisa mencapainya")
        print("   [b] Yang saya pikir akan menantang dan membanggakan jika saya dapat mencapainya")
        print("   [c] Yang saya bisa capai sebagian yang saya bisa dari tujuan yang lebih besar")
        print("   [d] Yang saya nyaman jika saya bisa meraihnya\n")
    

def akumulasi_jawaban(nomor_pertanyaan, jawaban_abc):
    driver_condition =""
    analytic_condition =""
    expressive_condition=""
    amiable_condition=""

    if nomor_pertanyaan == 1:
        if jawaban_abc == "a":
            analytic_condition = "analytic"
            return analytic_condition
        elif jawaban_abc == "b":
            driver_condition = "driver"
            return driver_condition
        elif jawaban_abc == "c":
            amiable_condition = "amiable"
            return amiable_condition
        else:
            expressive_condition = "expressive"
            return expressive_condition
    elif nomor_pertanyaan == 2:
        if jawaban_abc == "a":
            amiable_condition = "amiable"
            return amiable_condition
        elif jawaban_abc == "b":
            analytic_condition = "analytic"
            return analytic_condition
        elif jawaban_abc == "c":
            expressive_condition = "expressive"
            return expressive_condition
        else:
            driver_condition = "driver"
            return driver_condition
    elif nomor_pertanyaan == 3:
        if jawaban_abc == "a":
            amiable_condition = "amiable"
            return amiable_condition
        elif jawaban_abc == "b":
            expressive_condition = "expressive"
            return expressive_condition
        elif jawaban_abc == "c":
            analytic_condition = "analytic"
            return analytic_condition
        else:
            driver_condition = "driver"
            return driver_condition
    elif nomor_pertanyaan == 4:
        if jawaban_abc == "a":
            driver_condition = "driver"
            return driver_condition
        elif jawaban_abc == "b":
            amiable_condition = "amiable"
            return amiable_condition
        elif jawaban_abc == "c":
            analytic_condition = "analytic"
            return analytic_condition
        else:
            expressive_condition = "expressive"
            return expressive_condition
    elif nomor_pertanyaan == 5:
        if jawaban_abc == "a":
            driver_condition = "driver"
            return driver_condition
        elif jawaban_abc == "b":
            expressive_condition = "expressive"
            return expressive_condition
        elif jawaban_abc == "c":
            amiable_condition = "amiable"
            return amiable_condition
        else:
            analytic_condition = "analytic"
            return analytic_condition
    elif nomor_pertanyaan == 6:
        if jawaban_abc == "a":
            analytic_condition = "analytic"
            return analytic_condition
        elif jawaban_abc == "b":
            driver_condition = "driver"
            return driver_condition
        elif jawaban_abc == "c":
            expressive_condition = "expressive"
            return expressive_condition
        else:
            amiable_condition = "amiable"
            return amiable_condition
    elif nomor_pertanyaan == 7:
        if jawaban_abc == "a":
            expressive_condition = "expressive"
            return expressive_condition
        elif jawaban_abc == "b":
            amiable_condition = "amiable"
            return amiable_condition
        elif jawaban_abc == "c":
            analytic_condition = "analytic"
            return analytic_condition
        else:
            driver_condition = "driver"
            return driver_condition
    elif nomor_pertanyaan == 8:
        if jawaban_abc == "a":
            amiable_condition = "amiable"
            return amiable_condition
        elif jawaban_abc == "b":
            driver_condition = "driver"
            return driver_condition
        elif jawaban_abc == "c":
            expressive_condition = "expressive"
            return expressive_condition
        else:
            analytic_condition = "analytic"
            return analytic_condition
    elif nomor_pertanyaan == 9:
        if jawaban_abc == "a":
            expressive_condition = "expressive"
            return expressive_condition
        elif jawaban_abc == "b":
            analytic_condition = "analytic"
            return analytic_condition
        elif jawaban_abc == "c":
            amiable_condition = "amiable"
            return amiable_condition
        else:
            driver_condition = "driver"
            return driver_condition
    elif nomor_pertanyaan == 10:
        if jawaban_abc == "a":
            analytic_condition = "analytic"
            return analytic_condition
        elif jawaban_abc == "b":
            expressive_condition = "expressive"
            return expressive_condition
        elif jawaban_abc == "c":
            driver_condition = "driver"
            return driver_condition
        else:
            amiable_condition = "amiable"
            return amiable_condition
jalan = 0
while jalan < 10:
    simpan_nomor_pertanyaan = nomor_pertanyaan()
    if simpan_nomor_pertanyaan in kelas_tanya:
        continue
    elif simpan_nomor_pertanyaan not in kelas_tanya:
        sini = simpan_nomor_pertanyaan
        kelas_tanya.append(sini)
        daftar_pertanyaan(simpan_nomor_pertanyaan)
        jawaban_dari_pertanyaan_user = input("   Masukkan jawabanmu\n   #pilih_a|b|c|d\n   : ")
        if jawaban_dari_pertanyaan_user =="a" or jawaban_dari_pertanyaan_user == "b" or jawaban_dari_pertanyaan_user == "c" or jawaban_dari_pertanyaan_user == "d":
            hasil_string = akumulasi_jawaban(sini, jawaban_dari_pertanyaan_user)
            if hasil_string == "analytic":
                analytic+=1
            elif hasil_string == "driver":
                driver+=1
            elif hasil_string == "amiable":
                amiable+=1
            else:
                expressive+=1
        else:
            del kelas_tanya[-1]
            os.system('cls')
            print("\n-----------------------------------------------------------------------------------")
            print("| Jawaban yang kamu masukkan tidak terdeteksi, silahkan melanjutkan pertanyaan lain |")
            print("-------------------------------------------------------------------------------------")
            msvcrt.getch()
            os.system('cls')
            continue
    
        os.system('cls')
    #print("dri: {}, exp: {}, ami: {}, analy: {}".format(driver, expressive, amiable, analytic))
    jalan = jalan+1


print("DRIVER     : {}".format(driver))
print("EXPRESSIVE : {}".format(expressive))
print("AMIABLE    : {}".format(amiable))
print("ANALYTIC   : {}".format(analytic))

#memberi jeda agar tidak langsung keluar jendela
msvcrt.getch()
