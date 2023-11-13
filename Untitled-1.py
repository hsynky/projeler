#sans oyunu

#kural tanıtım


baslangic_puani = 1000
import random
import time

print("    ")
print("\033[93m" +"* oyunda şuanda sana 1000 puan verilmiş halde başladın ")
print("                              ")
time.sleep(2)
print("\033[93m" +"* sende belirli riskler alıp her turda değişen ve rastgele belirlenmiş olan sayısı bilmen gerek")
print("      ")
time.sleep(3)
print("\033[93m" +"* eğer bilirsen riske attıgın tutar kadar puanına eklenir kaybedersen ise yine o miktar kadar puanın ekisilir")
print("      ")
time.sleep(3)
print("\033[93m" +"* ayrıca 2000 puana ulaşırsan oyunu kazanırsın ancak 0 puanın altına inersen kaybedersin ")
print("* tam 0 olursa ise sana artıya geçmen için bir şans daha verilir ")
print("      ")
time.sleep(7)
print("\033[93m" +"* ekranda çıkan mesajlar seni eğlendirmek yada gaza getirmek için yapılmıştır lütfen alınma :) "+ "\033[0m")
print("    ")
time.sleep(4)

risk_miktari= int(input("\033[91m"+" ne kadar risk istersin 500,250,200,100 "+"\033[0m"))

#eğer girilen sayı uyğun değilse 
if risk_miktari not in [100, 250, 500, 200]:
    sayi_0 = random.randint(1, 3) # 1 ile 3 arasında bir sayı tut o sayı yı değikene ata
    if sayi_0 == 1: # sayı 1 ie bunu yazdır
        print(" ") 
        print("\033[91m"+"1 ile 3 arasında dedik zaten senin gibi biri bunu yapar "+"\033[0m") 

        time.sleep(3)   
    elif sayi_0 == 2: # sayı 2 ise bunu yazdır 
        print(" ")
        print ("\033[91m"+"hem buu oynamaya geliyorsun hemde denilen sayıları giremiyorsun ne yapmaya geldin "+"\033[0m")
        time.sleep(3)
    elif sayi_0 == 3: # sayı 3 ise bunu yazdır 
        print(" ")
        print ("\033[91m"+" ya aklım almıyor be kardeşim çok basit yahu sadece yazan sayılar başka yok "+"\033[0m")
        time.sleep(3)
        rastgele_sayi = random.randint(1, 3)

# girilen sayı doğru ise 
while risk_miktari in [100, 250, 500, 200]: 

    if risk_miktari not in [100, 250, 500, 200]:
        sayi_1 = random.randint(1, 3) # 1 ile 3 arasında bir sayı tut o sayı yı değikene ata
        if sayi_1 == 1: # sayı 1 ie bunu yazdır 
            print(" ")
            print ("\033[91m"+"1 ile 3 arasında dedik zaten sen yaparsın bunu "+"\033[0m")    
        elif sayi_1 == 2: # sayı 2 ise bunu yazdır 
            print(" ")
            print ("\033[91m"+"hem bunu oynamaya geliyorsun hemde denilen sayıları giremiyorsun ya "+"\033[0m")
        elif sayi_1 == 3: # sayı 3 ise bunu yazdır 
            print(" ")
            print ("\033[91m"+" ya aklım almıyor be kardeşim çok basit yahu sadece yazan sayılar başka yok "+"\033[0m")
            rastgele_sayi = random.randint(1, 3)

    rastgele_sayi = random.randint(1, 3) # rastgele bir sayıyı değişkene ata
    secilen_sayı= int(input("\033[91m"+"lütfen bir sayı gir ve 0 ile 3 arasında olsun "+ "\033[0m")) # kullanıcıdan rastgele sayı için tahmin al

    if baslangic_puani < 0 : # eğer puanın 0 ın altında ise oyun bitsin 
        print(" ")
        print("\033[91m"+" game over kardeğim iflas "+"\033[0m")
        print(" ")
        break

    if secilen_sayı == rastgele_sayi : # kullanıcının tahmini doğru ise 
        baslangic_puani += risk_miktari # kullanıcın alığı riski başlangıç puanına ekle 
        sayi_2 = random.randint(1, 3) # rast gele bir sayı tut ve tutuğun sayıya göre cevap yazdır 
        if sayi_2 == 1:
            print(" ")
            print (f"{baslangic_puani} puan kazandın helal lan kedi olalı bir fare tuttun") 
            print(" ")
        elif sayi_2 == 2:
            print(" ")
            print (f"vay be kardeşim bildi bak bir gözlerim yaşardı artık puanın {baslangic_puani}")
            print(" ")
        risk_miktari= int(input(" ne kadar risk istersin 500,250,200,100..."))
        rastgele_sayi = random.randint(1, 3)
     
        print(" ")
        secilen_sayı= int(input("lütfen bir sayı gir ve 0 ile 3 arasında olsun "))

    if baslangic_puani >= 2000 : # eğer puan 2 binin üstünde ise 
        print(" ")
        print("\033[1m\033[34m oyunu kazandın reiss tebrik ederim kasa tam takır kuru bakır amk  ") # yazdır 
        break # ve bitir 

    if baslangic_puani  <= 0 : #puan 0 on altında ise 
        sayi_3 = random.randint(1, 3)
        if sayi_3 == 1:
            print(" ")
            print(" ya işte böyle kalırsın ben her zaman kazanırım ")
        if sayi_3 == 2:
            print (" ")
            print(" benim adım serdar tezcan  ")
            time.sleep(2)
            print("dolandırıcılar kralıyım")


        if sayi_3 == 3 : 
            print(" ")
            print("he canım hee bak kazandın şuan hatta şuan para geldi 1 saniyesi var hatta ")
            time.sleep(4)
            print(" ")
            print(" ya bi git cidden bekledin mi ulan ")
            time.sleep(5)
            print("oha lan cidden mii")

        break 

    elif secilen_sayı != rastgele_sayi: 
        sayi_4= 1
        sayi_4 = random.randint(1, 4)
        baslangic_puani -= risk_miktari
        if sayi_4== 1 :
            print(" ")
            print ("\033[1m\033[34mbilemedin bilemedin ben kazandım bu gidişle sonun iyi değil senin ")
            print(" ")
            print (f"{baslangic_puani} nınız kaldı  ")
            print(" ")
            print ("iyi kullan dikkat et ")
            print(" ")
        if sayi_4==2 :
            print(" ")
            print("yav anlat hele nasıl oluyor bu kadar şansızken hayat  ")
            time.sleep(2)
            print(f"bu arada {baslangic_puani} kadar puanın kaldı haberin olsun  ")
            print(" ")
        if sayi_4== 3:
            print(" ")
            print(f"{baslangic_puani} bir şey diyemiyorum artık sana ")
            time.sleep( 2)
            print(" sonuçta buda bir başarı  ")


    risk_miktari=int(input("ne kadar risk istersiniz 500,250,200,100..."))

    rastgele_sayi = random.randint(1, 3)

