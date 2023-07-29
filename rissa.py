import time
import os

if __name__ == "__main__":
    versi_ini ="1.0"
    
a = ("""
Tools ini dibuat hanya untuk Hp Xiaomi, Redmi, Poco yang spek nya kentang. agar bisa dijebol fitur flagship yang tersembunyi didalamnya.
hayang donate atau kamu bertanyea tanyea?
Whatsapp : 0895325810708

 """)
def tentang(a):
    for hyung in (a):
        print(hyung, end="", flush=True)
        time.sleep(0.03)
    
 
def rissa():
    while True:
        nanya = input("Pilih :")
        if nanya == "1":
            print("Tunggu sebentar..")
            time.sleep(2)
            os.system("am start --user 0 -n com.android.settings/com.android.settings.display.ScreenEnhanceEngineMemcActivity && clear")
            time.sleep(3)
            break
        if nanya == "2":
            print("Tunggu sebentar...")
        if nanya == "?":
            tentang(a)
            kepo = input("Direct ke wa owner?(y/g): ")
            if kepo == "y":
                os.system("")
            elif kepo =="g":
                os.system("clear")
                print(daftar)
            else:
                os.system("clear")
                print(daftar)
        else:
            print("Pilihan Tidak Tersedia")
            time.sleep(1)

daftar = """1.Aktifkan MEMC
2.Aktifkan Peningkatan Gambar 
3.Aktifkan Resolusi Super
?. About This Tools
0.Komunikasi dengan owner"""
def tzy():
    while True:
        print(daftar)
        rissa()
    
try:
    tzy()  
except EOFError:
    print("selesai")
   os.system("clear")
        print(daftar)
        rissa()
    
try:
    tzy()  
except EOFError:
    print("selesai")
