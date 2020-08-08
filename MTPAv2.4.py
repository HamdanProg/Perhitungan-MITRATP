def uak(x,y,z):
	x=1
	while x>0:
		y=input('Kode : n. Kembali ke menu awal; m. Keluar\nPilihan anda : ')
		if y=='n':
			print('\x1bc')
			loading()
			x=-1
		elif y=='m':
			quit()
		else:
			print('\x1bc')
			z()
			x=x+1

def loading():
	ld=1
	while ld<=50:
		print('\x1bc');print('='*ld);time.sleep(0.004)
		ld=ld+1
		print('\x1bc')
#IMPORT
print('\x1bc')
import time
import math
#ALAT
def k():
	print('\nkode :\na. tambah\ns. kali\nl. lanjut\nPilihan anda : ')
def res():
	print('\x1bc')
	print('Uang masuk sejumlah Rp',masuk)
def res1():
	print('\x1bc')
	print('Total saldo sejumlah Rp',tosal)
def res2():
	print('\x1bc')
	print('Sisa saldo sejumlah Rp',sisal)
#MENU AWAL
print('\x1bc');print('S        ###              ###');print('E      #     #          #     #');print('L     #  #    #        #  #    #');print('A      #     #          #     #');print('M       #####            #####');print('A');print('T       ');print('           #################');print('D          #               #');print('A           #             #');print('T             ##       ##');print('A               #######');print('N');print('G')
time.sleep(0.6)
print('\x1bc');print('M        ###');print('E      #     #            ###      #');print('T     #  #    #         #     #  #');print('A      #     #                     #');print('A       #####');print('A');print('       ');print('           #################');print('           #               #');print('A           #             #');print('              ##       ##');print('A               #######');print('');print('G')
time.sleep(0.2)
print('\x1bc');print('M        ###              ###');print('I      #     #          #     #');print('T     #  #    #        #  #    #');print('R      #     #          #     #');print('A       #####            #####');print('');print('       ');print('           #################');print('           #               #');print('            #             #');print('              ##       ##');print('                #######');print('');print('')
time.sleep(0.6)
print('\x1bc');print('MITRA TOKOPEDIA ASISTANT\nmetode penghitungan semi otomatis untuk mitra')
time.sleep(2.5)
mn=1
while mn>0:
	print('\x1bc')
	print('^<^ : MENU UTAMA\n\nAda yang bisa kami bantu?\n\nkode :\n1. Menghitung keuntungan\n2. Statistik keuntungan\n3. Intruksi penggunaan\n4. Tentang pembuat\n5. Keluar')
	menu=input('Pilihan anda : ')
	if menu=='1':
#MENU PERTAMA
		#UANG MASUK
		loading()
		awal=1
		while awal>0:
			masuk=int(input('MASUKKAN UANG MASUK\nRp'))
			k()
			hit=1
			while hit>0:
				pencet=input('')
				if pencet=='a':
					masuk1=int(input('Rp'))
					masuk=masuk+masuk1
					res()
					hit=hit+1
					k()
				elif pencet=='s':
					masuk1=int(input('Rp'))
					masuk=masuk*masuk1
					res()
					hit=hit+1
					k()
				elif pencet=='l':
					loading()
					#TOTAL SALDO
					tosal=int(input('MASUKKAN TOTAL SALDO\nRp'))
					k()
					hit2=1
					while hit2>0:
						pencet=input('')
						if pencet=='a':
							tosal1=int(input('Rp'))
							tosal=tosal+tosal1
							res1()
							hit2=hit2+1
							k()
						elif pencet=='s':
							tosal1=int(input('Rp'))
							tosal=tosal*tosal1
							res1()
							hit2=hit2+1
							k()
						elif pencet=='l':
							loading()
							#SISA SALDO
							sisal= int(input('MASUKKAN SISA SALDO\nRp'))
							k()
							hit3=1
							while hit3>0:
								pencet=input('')
								if pencet=='a':
									sisal1=int(input('Rp'))
									sisal=sisal+sisal1
									res2()
									hit3=hit3+1
									k()
								elif pencet=='s':
									sisal1=int(input('Rp'))
									sisal=sisal*sisal1
									res2()
									hit3=hit3+1
									k()
								elif pencet=='l':
									loading()
									#OPERASI HITUNG
									def oph():
										print('\x1bc')
										print('\nJADI,\nUang masuk = Rp',masuk,'\nTotal saldo = Rp',tosal,'\nSisa saldo = Rp',sisal)
										print('\nMAKA,\nPendapatan = Rp', masuk,'\nPengeluaran = Rp', tosal-sisal,'\nUntung = Rp', masuk-(tosal-sisal),'\n\n*Silahkan catat di buku catatan\n')
									oph()
									#AKHIRI/ULANGI SESI
									uak(1,2,oph)
									hit3=-1
								else:
									res2()
									k()
									hit3=hit3+1
							else:
								hit2=-1
						else:
							res1()
							k()
							hit2=hit2+1
					else:
						hit=-1
				else:
					res()
					k()
					hit=hit+1
			else:
				awal=-1
		else:
			mn=mn+1
	elif menu=='2':
		loading()
#MENU KEDUA
		var1=float(input('Keuntungan pada bulan pertama : Rp'))
		var2=float(input('Keuntungan pada bulan kemarin : Rp'))
		var3=float(input('Keuntungan pada bulan sekarang : Rp'))
		nilaimx=max(var1,var2,var3)
		var4=((var3/var1))*100-100
		var5=((var3/var2))*100-100
		loading()
		def aou2():
			print('MAKA,\nKenaikan untung terhadap bulan pertama : ',var4,' %')
			print('Kenaikan untung terhadap bulan kemarin : ',var5, ' %')
			sttvar1=round((var1/nilaimx)*50)
			sttvar2=round((var2/nilaimx)*50)
			sttvar3=round((var3/nilaimx)*50)
			print('Untung bulan pertama : \n'+']'*sttvar1,'\n')
			print('Untung bulan kemarin : \n'+']'*sttvar2,'\n')
			print('Untung bulan sekarang : \n'+']'*sttvar3,'\n')
			print('\n*Silahkan catat di buku catatan\n')
		aou2()
		#AKHIRI/ULANGI SESI
		uak(3,4,aou2)
		mn=mn+1
#MENU KETIGA
	elif menu=='3':
		loading()
		def aou3():
			print('^<^ : INTRUKSI PENGGUNAAN\n');print('Hanya masukkan angka pada saat memasukkan nilai uang\nJika dilanggar : akan muncul EROR\n\nHanya masukkan kode yang ada di dalam list kode\nJika dilanggar : perintah tidak akan tersampaikan')
		aou3()
		#AKHIRI/ULANGI SESI
		print('\n'*6)
		uak(5,6,aou3)
		mn=mn+1
#MENU KEEMPAT
	elif menu=='4':
		loading()
		def aou4():
			print('^<^ : TENTANG PEMBUAT\n');print('Gmail    : hamdanduaenamprog@gmail.com\n\nGithub   : HamdanProg\n\nFacebook : Bang Hamdan')
		aou4()
		#AKHIRI/ULANGI SESI
		print('\n'*6)
		uak(7,8,aou4)
		mn=mn+1
#MENU KELIMA
	elif menu=='5':
		quit()
#ELSE
	else:
		mn=mn+1