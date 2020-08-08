def loading():
	ld=1
	while ld<=2:
		print('\x1bc');print('.')
		time.sleep(0.05)
		print('\x1bc');print('..')
		time.sleep(0.05)
		print('\x1bc');print('...')
		time.sleep(0.05)
		print('\x1bc')
		ld=ld+1
print('\x1bc')
import time
#ALAT
def k():
	print('\nkode :\na. tambah\ns. kali\nl. lanjut\nPilihan anda : ')
def res():
	print('\x1bc')
	print('Uang masuk sejumlah ',masuk)
def res1():
	print('\x1bc')
	print('Total saldo sejumlah ',tosal)
def res2():
	print('\x1bc')
	print('Sisa saldo sejumlah ',sisal)
#MENU AWAL
print('ASISTEN MITRA TOKOPEDIA\nby Hamdan26\n\nGMAIL : hamdanduaenamprog@gmail.com')
time.sleep(1)
print('\x1bc');print('\n\nSelamat datang di program kami ^_^')
time.sleep(2)
mn=1
while mn>0:
	print('\x1bc')
	print('=====================================MENU UTAMA\nAda yang bisa kami bantu?\n\nkode :\n1. Menghitung keuntungan\n2. Menghitung Persentase keuntungan')
	menu=input('Pilihan anda : ')
	if menu=='1':
		#MENU PERTAMA
		#UANG MASUK
		loading()
		awal=1
		while awal>0:
			masuk=int(input('MASUKKAN UANG MASUK\n'))
			k()
			hit=1
			while hit>0:
				pencet=input('')
				if pencet=='a':
					masuk1=int(input())
					masuk=masuk+masuk1
					res()
					hit=hit+1
					k()
				elif pencet=='s':
					masuk1=int(input())
					masuk=masuk*masuk1
					res()
					hit=hit+1
					k()
				elif pencet=='l':
					loading()
					#TOTAL SALDO
					tosal=int(input('MASUKKAN TOTAL SALDO\n'))
					k()
					hit2=1
					while hit2>0:
						pencet=input('')
						if pencet=='a':
							tosal1=int(input())
							tosal=tosal+tosal1
							res1()
							hit2=hit2+1
							k()
						elif pencet=='s':
							tosal1=int(input())
							tosal=tosal*tosal1
							res1()
							hit2=hit2+1
							k()
						elif pencet=='l':
							loading()
							#SISA SALDO
							sisal= int(input('MASUKKAN SISA SALDO\n'))
							k()
							hit3=1
							while hit3>0:
								pencet=input('')
								if pencet=='a':
									sisal1=int(input())
									sisal=sisal+sisal1
									res2()
									hit3=hit3+1
									k()
								elif pencet=='s':
									sisal1=int(input())
									sisal=sisal*sisal1
									res2()
									hit3=hit3+1
									k()
								elif pencet=='l':
									loading()
									#OPERASI HITUNG
									print('\x1bc')
									print('\nJADI,\nUang masuk = ',masuk,'\nTotal saldo = ',tosal,'\nSisa saldo = ',sisal)
									print('\nMAKA,\nPendapatan = ', masuk,'\nPengeluaran = ', tosal-sisal,'\nUntung = ', masuk-(tosal-sisal),'\n')
									#AKHIRI/ULANGI SESI
									aoru=1
									while aoru>0:
										aus=input('Akhiri atau ulangi sesi?\nKode : n. Kembali ke menu awal; m. Akhiri')
										if aus=='n':
											print('\x1bc')
											aoru=-1
										elif aus=='m':
											quit()
										else:
											aoru=aoru+1
									else:
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
		mn=-1
	else:
		mn=mn+1
#MENU KEDUA
tanyawaktu=int(input('Sudah berapa bulan anda menjadi Mitra Tokopedia ?\nJawab : '))
var1=float(input('Keuntungan pada bulan pertama : '))
var2=float(input('Keuntungan pada bulan kemarin : '))
var3=float(input('Keuntungan pada bulan sekarang : '))
var4=((var3/var1))*100-100
var5=((var3/var2))*100-100
loading()
print('MAKA,\nKenaikan untung terhadap bulan pertama : ',var4,' %')
print('MAKA,\nKenaikan untung terhadap bulan kemarin  : ',var5, ' %')