import requests
import time
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.MAGENTA)
print """coded by sm1l3
:'######::'##::::'##::::'##:::'##::::::::'#######::
'##... ##: ###::'###::'####::: ##:::::::'##.... ##:
 ##:::..:: ####'####::.. ##::: ##:::::::..::::: ##:
. ######:: ## ### ##:::: ##::: ##::::::::'#######::
:..... ##: ##. #: ##:::: ##::: ##::::::::...... ##:
'##::: ##: ##:.:: ##:::: ##::: ##:::::::'##:::: ##:
. ######:: ##:::: ##::'######: ########:. #######::
:......:::..:::::..:::......::........:::.......:::
"""

print ("1 kisi")
print ("2 sirket")
soru = raw_input("--> ")
if soru == '2':
    
    sirket = raw_input("sirket adi-> ")
    domain = raw_input("domain adi-> ")
    print(Fore.RED)
    print "olasi mailler..."
    r = requests.get('https://api.hunter.io/v2/domain-search?domain='+domain+'&api_key=5f002f8296a14d73f4d249834aa195f08f691135')
    print(r.text)
    ara = "site:pastebin.com inurl:"+domain
    ara1 = "site:github.com inurl:"+domain
    ara2 = "site:linkedin.com inurl:"+sirket
    ara3 = "site:facebook.com inurl:"+sirket
    ara4= "site:instagram.com inurl:"+sirket
    ara5 = "site:linkedin.com intext:"+domain
    ara6 = "site:facebook.com intext:"+domain
    ara7= "site:instagram.com intext:"+domain
   
    print(Fore.RED)
    print "halka acik sirket verileri , kisiler github pastebin linkedin sosyal medya vb..."
    try: 
        from googlesearch import search 
    except ImportError:  
        print("google modulu kurulu degil") 
    
    for j in search(ara, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(10)

    time.sleep(60)
        
    for j in search(ara1, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(15)

    time.sleep(60)
    
    for j in search(ara2, tld="co.in", pause=4): 
        print(Fore.GREEN)
        print("[+] "+j) 
        time.sleep(25)

    time.sleep(60)
    
    for j in search(ara3, tld="co.in", pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)  
        time.sleep(25)

    time.sleep(60)

    for j in search(ara4, tld="co.in", pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(25)

    time.sleep(60)
    
    for j in search(ara5, tld="co.in", pause=4):
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(25)

    time.sleep(60)

    for j in search(ara6, tld="co.in", pause=4):
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(25)



    time.sleep(60)
    
    for j in search(ara7, tld="co.in", pause=4):
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(25)
     
    print(Fore.RED)
    print "olasi calisan mail adresleri (facebook ve instagram paylasimlarindan toplanir) ..."

    mail = "site:facebook.com inurl:"+sirket+"intext:@yahoo.com"
    mail1 = "site:facebook.com inurl:"+sirket+"intext:@gmail.com"
    mail2 = "site:facebook.com inurl:"+sirket+"intext:@hotmail.com"
    mail3 = "site:instagram.com inurl:"+sirket+"intext:@yahoo.com"
    mail4 = "site:instagram.com inurl:"+sirket+"intext:@gmail.com"
    mail5 = "site:instagram.com inurl:"+sirket+"intext:@hotmail.com"

    for j in search(mail, tld="co.in", pause=4):
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(25)
    
    time.sleep(60)

    for j in search(mail1, tld="co.in", pause=4):
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(25)

    time.sleep(60)

    for j in search(mail2, tld="co.in", pause=4):
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(25)

    time.sleep(60)

    for j in search(mail3, tld="co.in", pause=4):
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(25)

    time.sleep(60)

    for j in search(mail4, tld="co.in", pause=4):
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(25)

    time.sleep(60)

    for j in search(mail5, tld="co.in", pause=4):
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(25)


if soru == '1':
    isim = raw_input("isim giriniz -> ")
    lakap = raw_input("lakap giriniz -> ")
    print(Fore.RED)
    print "...keyword ('olasi kullanici adi') kullanmayacaksaniz bos gecin..."
    kw = raw_input("aramada kullanilicak keyword 1-> ")
    

    sm = "site:facebook.com inurl:"+isim+"intext:@yahoo.com"
    sm1 = "site:facebook.com inurl:"+isim+"intext:@gmail.com"
    sm2 = "site:facebook.com inurl:"+isim+"intext:@hotmail.com"
    sm3 = "site:instagram.com inurl:"+isim+"intext:@yahoo.com"
    sm4 = "site:instagram.com inurl:"+isim+"intext:@gmail.com"
    sm5 = "site:instagram.com inurl:"+isim+"intext:@hotmail.com"
    sm6 = "site:facebook.com inurl:"+isim
    sm7 = "site:facebook.com inurl:"+kw
    sm8 = "site:facebook.com inurl:"+lakap
    sm9 = "site:instagram.com inurl:"+lakap
    sm8 = "site:instagram.com inurl:"+kw
    sm10 = "site:instagram.com inurl:"+isim
    sm11 = "site:linkedin.com inurl:"+isim


    try: 
        from googlesearch import search 
    except ImportError:  
        print(Fore.RED)
        print("google modulu kurulu degil") 
    
    print(Fore.RED)
    print "olasi sosyal medya hesaplarinda paylasilan mailler toplaniyor...."

    for j in search(sm, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(10)

    time.sleep(60)

    for j in search(sm1, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(10)

    time.sleep(60)

    for j in search(sm2, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(10)

    
    time.sleep(60)

    for j in search(sm3, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(10)
    
    time.sleep(60)

    for j in search(sm4, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(10)

    time.sleep(60)

    for j in search(sm5, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(10)
    
    print "olasi sosyal medya hesaplari toplaniyor linkedin facebook instagram..."

    time.sleep(60)

    for j in search(sm6, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(10)


    time.sleep(60)

    for j in search(sm7, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(10)

    time.sleep(60)

    for j in search(sm8, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(10)


    time.sleep(60)

    for j in search(sm9, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(10)


    time.sleep(60)

    for j in search(sm10, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(10)

    time.sleep(60)

    for j in search(sm11, tld="co.in" , pause=4): 
        print(Fore.GREEN)
        print("[+] "+j)
        time.sleep(10)
