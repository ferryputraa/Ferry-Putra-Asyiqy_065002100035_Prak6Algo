def jarak_tempuh(v0,t,a) :
    s=(v0*t+(1/2)*a*(t**2))
    print("kecepatan awal =",v0,",","waktu =",t,",","percepatan =",a,",","jarak tempuhnya adalah = ",s)
    return s

print("MENGHITUNG JARAK TEMPUH GLBB")
v0=int(input("kecepatan awal\t : "))
t=int(input("waktu\t\t : "))
a=int(input("percepatan\t : "))
jarak_tempuh(v0,t,a)
