def loading():
	ld=1
	while ld<=3:
		print('\x1bc');print('.')
		time.sleep(0.1)
		print('\x1bc');print('..')
		time.sleep(0.1)
		print('\x1bc');print('...')
		time.sleep(0.1)
		ld=ld+1
print('\x1bc')
import time
#ALAT
def k():
	print('kode : a. tambah; s. kali; l. lanjut')
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
print('HITUNGAN MITRA TOKOPEDIA\nby Hamdan26')
time.sleep(1)
print('\n\nSelamat datang di program kami ^_^')
time.sleep(2)
mn=1
while mn>0:
	print('\x1bc')
	print('\nAda yang bisa kami bantu?\n1. Menghitung Uang; 2. Statistik Jualan')
	menu=input('Pilihan anda : ')
	if menu=='1':
		#UANG MASUK
		loading()
		print('\x1bc')
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
					print('\x1bc')
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
							print('\x1bc')
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
		print('Maaf sedang dalam proses pengerjaan')
		time.sleep(1)
	else:
		mn=mn+1