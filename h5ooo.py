class hesap:
    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2

    def carp(self):
        sonuc=self.sayi1*self.sayi2
        return sonuc

    def bol(self):
        sonuc=self.sayi1/self.sayi2
        return sonuc

    def topla(self):
        sonuc=self.sayi1+self.sayi2
        return sonuc

    def cıkar(self):
        sonuc=self.sayi1-self.sayi2
        return sonuc

    def yazdır(self):
        print("sayi1 =", self.sayi1)
        print("sayi2 =", self.sayi2)
        print("carpma =", self.carp())
        print("bolme=", self.bol())
        print("cıkarma =", self.cıkar())
        print("toplama =", self.topla())

A = hesap(5,3)
B = hesap(4,2)

feyza = hesap(A.sayi1,B.sayi2)
feyza.yazdır()

melisa =hesap(A.sayi2,B.sayi2)
melisa.yazdır()