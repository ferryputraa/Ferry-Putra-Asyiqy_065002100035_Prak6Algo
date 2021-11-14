print("###################################################### ")
print(" ###	                                              ")
print(" ###  ##   #######   #########   #########   ###   ### ")
print(" #######  ###   ###   ###   ###   ###   ###  ###   ### ")
print(" ###  ##  ########    ###         ###         ######## ")
print(" ###      ###         ###         ###              ### ")
print("#####      #######    ###         ###        ########  ")

def menu():
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Bola")
    print("6. Exit")

def kubus():
    s = int(input("Masukkan rusuk : "))
    rumus = 6*(s**2)
    print("Luas permukaan kubus dengan rusuk",s,"adalah",(rumus))

def balok():
    p = int(input("Masukkan panjang : "))
    l = int(input("Masukkan lebar   : "))
    t = int(input("Masukkan tinggi  : "))
    rumus = 2*((p*l)+(p*t)+(l*t))
    print("Luas permukaan balok dengan panjang",p,",","lebar",l,",","tinggi",t,"adalah",(rumus))
    
def tabung():
    r = int(input("Masukkan jari-jari : "))
    t = int(input("Masukkan tingggi   : "))
    rumus = 2*22/7*r*(r+t)
    print("Luas permukaan tabung dengan jari-jari",r,",","tinggi",t,",","adalah",(rumus))

def kerucut():
    r = int(input("Masukkan jari-jari   : "))
    s = int(input("Masukkan garis lukis : "))
    rumus = 22/7*r*(r+s)
    print("Luas permukaan kerucut dengan jari-jari",r,",","garis lukis",s,",","adalah",(rumus))

def bola():
    r = int(input("Masukkan jari-jari : "))
    rumus = 4*22/7*(r**2)
    print("Luas permukaan bola dengan jari-jari",r,"adalah",(rumus))

loop = True
while(loop):
    print("")
    print("KALKULATOR LUAS PERMUKAAN BANGUN RUANG")
    menu()
    pilih = input("Pilih menu yang tersedia : ")
    if pilih == "1":
        kubus()
    elif pilih == "2":
        balok()
    elif pilih == "3":
        tabung()
    elif pilih == "4":
        kerucut()
    elif pilih == "5":
        bola()
    elif pilih == "6":
        print("TERIMA KASIH!")
        exit()
    else:
        print("Pilihan tidak tersedia")
