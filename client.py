import xmlrpc.client
import getpass
import os
import time

SERVER_IP = 'localhost'
SERVER_PORT = '8000'
server = xmlrpc.client.ServerProxy(
    'http://{ip}:{port}'.format(ip=SERVER_IP, port=SERVER_PORT)
)


def menu_awal():
    os.system('cls')
    print("SELAMAT DATANG DI \nKUIS ONLINE BAHASA INGGRIS")
    print("MENU")
    print("1. Login Admin")
    print("2. Login User")
    print("3. Exit")


def menu_admin():
    os.system('cls')
    print('1. Upload Soal')
    print('2. Lihat Soal')
    print('3. Delete Soal')
    print('4. Nanti aja ah')


def menu_user():
    os.system('cls')
    print('1. Mulai Kuis')
    print('2. Lihat Nilai')
    print('3. Lihat Jawaban')


while True:
    menu_awal()
    pilihan = eval(input('Masukan pilihan :'))
    if pilihan == 1:
        os.system('cls')
        adm_user = input('Username :')
        adm_pass = getpass.getpass('Password :')
        valid_admin = server.login_admin(adm_user, adm_pass)
        if valid_admin:
            print('Berhasil login sebagai admin')
            time.sleep(0.5)
            menu_admin()
            pilihan = eval(input('Masukan pilihan :'))
            if pilihan == 1:
                nama_file = input('Masukan nama file (format .csv)')
                print('uploading...')
                lines = [line.rstrip('\n') for line in open(nama_file)]
                for i in range(len(lines)):
                    server.upload_soal(lines[i])
                menu_admin()
                pilihan = eval(input('Masukan pilihan :'))
            elif pilihan == 2:
                soal = server.lihat_soal()
                for i in range(len(soal)):
                    print(soal[i], '\n')
                print('setelah soal')
                # time.sleep(2)
            elif pilihan == 3:
                server.delete_soal()

        else:
            print('Salah password/username')
            time.sleep(0.5)
            os.system('cls')
    if pilihan == 2:
        os.system('cls')
        usr_user = input('Username :')
        usr_pass = getpass.getpass('Password :')
        valid_user = server.login_user(usr_user, usr_pass)
        if valid_user:
            print('Berhasil login sebagai user')
            time.sleep(0.5)
            os.system('cls')
            menu_user()
        else:
            print('Salah password/username')
            time.sleep(0.5)
            os.system('cls')