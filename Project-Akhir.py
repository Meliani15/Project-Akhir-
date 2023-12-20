import os
import datetime

os.system('cls')

print("*"*50)
print("*** PROGRAM PENCATAT KEUANGAN SEDERHANA ***")
print("*"*50)
print()

max_pass = 3
limit = 0
pengeluaran = []
pemasukan = []

while limit < max_pass:
  login = input('Masukkan Password: ')
  if login == '123':
    print('Selamat Anda Login!')  
    break
  else:
    limit += 1 
    print(f'Kesempatan tersisa {max_pass-limit}')
  if limit == max_pass:
    print('Akun Terblokir')
    exit()
      
while True:
  now = datetime.datetime.now()
  print(now.strftime("%A, %d %B %Y %H:%M:%S"))
  print()
  
  print("\nMenu:")
  print("1. Catatan Pengeluaran")
  print("2. Catatan Pemasukan") 
  print("3. Tampilkan Laporan")
  print("4. Keluar")
  
  menu = input("Pilih menu (1-4): ")
  
  if menu == '1':
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    pengeluaran.append(jumlah)
  elif menu == '2':
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    pemasukan.append(jumlah)
  elif menu == '3':
    total_pengeluaran = sum(pengeluaran)
    total_pemasukan = sum(pemasukan)  
    print(f"\nTotal Pengeluaran: {total_pengeluaran}")
    print(f"Total Pemasukan: {total_pemasukan}")
    
    selisih = total_pemasukan - total_pengeluaran
    print(f"Selisih Pemasukan dan Pengeluaran: {selisih}")
    
    if total_pengeluaran > total_pemasukan:
      print() 
      print("-----------------------------------------------")
      print(" PENGELUARAN LEBIH BESAR DARI PEMASUKAN! ")    
      print("-----------------------------------------------")
      print("Jangan Boros! Belajar Lebih Hemat Lagi Ya:)")
      print()
      
    elif total_pengeluaran < total_pemasukan:
      print()
      print("-----------------------------------------------") 
      print(" PENGELUARAN LEBIH KECIL DARI PEMASUKAN! ")
      print("-----------------------------------------------")
      print("Kamu Sudah Sangat Pintar Dalam Mengatur Keuangan:)")
      print()
    
    elif total_pengeluaran == total_pemasukan:
      print() 
      print("----------------------------------------------")
      print(" PENGELUARAN DAN PEMASUKAN SAMA BESAR! ")    
      print("----------------------------------------------")
      print("Tingkatkan Lagi Pola Hematnya:)")  
      print()
      
    saldo = total_pemasukan - total_pengeluaran  
    print(f"Saldo Anda: Rp.{saldo:,}")
        
  elif menu == '4':
    break
  
  else:
    print("Menu tidak tersedia. Silakan pilih menu 1-4.")
      
print("\nProgram selesai")