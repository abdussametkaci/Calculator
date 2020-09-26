from tkinter import *
from tkinter import messagebox

class Hesap(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("200x123")
        self.minsize(200, 123)
        self.maxsize(200, 123)
        self.title("Hesap Makinesi")

        
        self.entry = Entry(width = 33)
        self.entry.grid(row = 0,
                        column = 0,
                        columnspan = 5)
        
        self.button1 = Button(text = "1",
                              command = self.bir)
        self.button1.grid(row = 1,
                          column = 0,
                          sticky = "we")

        self.button2 = Button(text = "2",
                              command = self.iki)
        self.button2.grid(row = 1,
                          column = 1,
                          sticky = "we")

        self.button3 = Button(text = "3",
                              command = self.üç)
        self.button3.grid(row = 1,
                          column = 2,
                          sticky = "we")

        self.button_sil = Button(text = "sil",
                                 command = self.sil)
        self.button_sil.grid(row = 1,
                             column = 3,
                             sticky = "we",
                             columnspan = 2)

        self.button4 = Button(text = "4",
                              command = self.dört)
        self.button4.grid(row = 2,
                          column = 0,
                          sticky = "we")
        
        self.button5 = Button(text = "5",
                              command = self.beş)
        self.button5.grid(row = 2,
                          column = 1,
                          sticky = "we")
        
        self.button6 = Button(text = "6",
                              command = self.altı)
        self.button6.grid(row = 2,
                          column = 2,
                           sticky = "we")

        self.button_çarpı = Button(text = "x",
                                   command = self.çarp)
        self.button_çarpı.grid(row = 2,
                               column = 3,
                               sticky = "we")

        self.button_bölü = Button(text = "/",
                                  command = self.böl)
        self.button_bölü.grid(row = 2,
                              column = 4,
                              sticky = "we")

        self.button7 = Button(text = "7",
                              command = self.yedi)
        self.button7.grid(row = 3,
                          column = 0,
                          sticky = "we")

        self.button8 = Button(text = "8",
                              command = self.sekiz)
        self.button8.grid(row = 3,
                          column = 1,
                          sticky = "we")


        self.button9 = Button(text = "9",
                              command = self.dokuz)
        self.button9.grid(row = 3,
                          column = 2,
                          sticky = "we")

        self.button_toplam = Button(text = "+",
                                    command = self.topla)
        self.button_toplam.grid(row = 3,
                                column = 3,
                                sticky = "we")

        self.button_çıkarma = Button(text = "-",
                                     command = self.çıkar)
        self.button_çıkarma.grid(row = 3,
                                 column = 4,
                                 sticky = "we")

        self.button0 = Button(text = "0",
                              command = self.sıfır)
        self.button0.grid(row = 4,
                          column = 0,
                          sticky = "we")

        self.button00 = Button(text = "00",
                               command = self.çift_sıfır)
        self.button00.grid(row = 4,
                           column = 1,
                           sticky = "we")

        self.button_nokta = Button(text = ".",
                                   command = self.nokta)
        self.button_nokta.grid(row = 4,
                               column = 2,
                               sticky = "we")


        self.button_eşittir = Button(text = "=",
                                     command = self.eşittir)
        self.button_eşittir.grid(row = 4,
                                 column = 3,
                                 sticky = "we")

        self.button_kök = Button(text = "r",
                                 command = self.kök)
        self.button_kök.grid(row = 4,
                             column = 4,
                             sticky = "we")

        self.bind("<Return>", self.eşittir)


    def sıfır(self):
        self.entry.insert("end", 0)

    def çift_sıfır(self):
        self.entry.insert("end", 0)
        self.entry.insert("end", 0)

    def nokta(self):
        self.entry.insert("end", ".")

    def bir(self):
        self.entry.insert("end", 1)

    def iki(self):
        self.entry.insert("end", 2)

    def üç(self):
        self.entry.insert("end", 3)

    def dört(self):
        self.entry.insert("end", 4)

    def beş(self):
        self.entry.insert("end", 5)

    def altı(self):
        self.entry.insert("end", 6)

    def yedi(self):
        self.entry.insert("end", 7)

    def sekiz(self):
        self.entry.insert("end", 8)

    def dokuz(self):
        self.entry.insert("end", 9)

    def sil(self):
        self.entry.delete(0, "end")

    def çarp(self):
        self.entry.insert("end", "*")

    def böl(self):
        self.entry.insert("end", "/")

    def topla(self):
        self.entry.insert("end", "+")

    def çıkar(self):
        self.entry.insert("end", "-")

    def eşittir(self, event = None):
        self.veri = self.entry.get()
        if not self.veri:
            self.hata = messagebox.showerror("Hata!",
                                             "Lütfen herhangi bir şey gir!")
        
        harfler = "abcçdefgğhıijklmoöprsştuüvyzxqw"
        for i in harfler:
            if i in self.veri: 
                self.mesaj = messagebox.showerror("Hata",
                                                  "Lütfen sadece düğmeleri kullanın!",
                                                   detail = "(uygulmadaki butonlar)",
                                                   type = "okcancel")
                if self.mesaj == "ok":
                    self.entry.delete(0, "end")
                    break

                elif self.mesaj == "cancel":
                    self.destroy()
                    break
                

        else:
            self.hesap = eval(self.veri)
            self.entry.delete(0, "end")
            self.entry.insert("end", self.hesap)


    def kök(self):
        self.entry.insert("end", "**0.5")


pencere = Hesap()      
mainloop()
#hesap_makinem uygulamasındaki kodlardır
#hesap makinesinin bitmiş halidir
#bind fonksiyonu Hesap adlı sınıfın içinde kullanmayı başardım
#bunu da Tk sınıfını miras alınca bind fonksiyonunu
#self'e bağlı birşekilde kullandım
#normalde Tk sınıfını örnekleyip, o örneklediğiniz adla bind'ı kullanıyorduk
#UYARI=!!! Hesap makinesine hiçbir veri girilmeyip enter'a basılnca
#arka planda hata veriyor ancak uygulama düzgün çalışıyor !!!

#ayrıca sadece sayı girilmesi için hata mesajları oluşturdum.
