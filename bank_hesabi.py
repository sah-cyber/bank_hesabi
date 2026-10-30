# BankHesabi adlı class yarat.
#
# Tələblər:
#
# İstifadəçinin balansı olsun (başlanğıcda 1000 AZN).
#
# pul_yatir() metodu balansı artırsın.
#
# pul_cixar() metodu balansı azaltsın.
#
# Balansdan artıq pul çıxarmaq mümkün olmasın.
#
# balans_goster() metodu cari balansı göstərsin.
#
# İstifadəçi 0 və ya mənfi məbləğ daxil edə bilməsin.

class BankHesabi:

    def __init__(self, pul=1000):
        self.pul = pul
        print(f"Xow gelmisiniz Sizin balansiniz {self.pul} AZN dir ")





    def pul_yatir(self):
        while True:

            self.pul_yukle = int(input("Zehmet olmasa balansiniza pul yukleyin: "))

            if self.pul_yukle and int(self.pul_yukle) > 0:
                print(f"Twk edirik siz balansiniza {self.pul_yukle} AZN yuklediniz")
                print(f'Sizin balansiniz {self.pul + int(self.pul_yukle)} Azn edir')

                self.balans = int(self.pul_yukle)+int(self.pul)
                print(f"Sizin balansiniz {self.balans}")

                return True
            else:
                print("Xeta!")

    def pul_cixar(self):
        while True:
            self.pul_cixar = int(input('Siz nece azn pul cixarmaq isteyirsiz? '))

            if (self.pul_cixar.is_integer() and self.pul_cixar > 0
                    and self.pul_cixar <= self.balans):
                self.balans -= self.pul_cixar

                print(f"Siz {self.pul_cixar} mebleginde pul cixariz sizin yeni balansiniz {self.balans}")
                return True
            else:
                print("Xeta duzgun secim edin")

    def balansi_goster(self):

        print(f"Sizin yeni balansiniz {self.balans}")





basla = BankHesabi()

basla.pul_yatir()
basla.pul_cixar()
basla.balansi_goster()