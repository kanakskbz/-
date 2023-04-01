import os,requests

R="\033[1;31m" # Red

G="\033[1;32m" # Green

idu=input('الايدي الخاص بيك : ')

fn = input("اسم ملف الايديات : ")

os.system('clear')

file=open(fn,'r')

while True:

    line=file.readline().split('\n')[0]

    id=line.split('\n')[0]

    url = "https://dev-osama74.pantheonsite.io/api/instaup-check.php?id="+id

    req = requests.get(url).json()

    coins=req['coins']

    if int(coins) <= 399:

    	print(R+f'[ ID ] => {id} | [ COINS ] {coins}  ')    if int(coins) >= 400:

        print(G+f'[ ID ] => {id} | [ COINS ] {coins}  ')

        try:

          r=requests.get(f'https://dev-osama74.pantheonsite.io/api/instaup-send.php?tid={id}&{idu}=&submit=submit ')

          print(G+"GOOD FOLLS ")

        except:

          print(R+"EROOR FOLLS ")

          

        
