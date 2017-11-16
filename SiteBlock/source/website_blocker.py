import time
from datetime import datetime as dt

host_temp = "..\hosts"
hosts_path="C:\Windows\System32\drivers\etc\hosts"

host = hosts_path

redirect="127.0.0.1"

website_list=["www.facebook.com","facebook.com"]
website_list.append("www.youtube.com")
website_list.append("www.youtube.com.br")
website_list.append("www.ahnegao.com.br")


#value = 8 <= dt.now().hour < 18



while True:
    if 8 <= dt.now().hour <= 17:#17
        print("Back to work")
        with open(host,"r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun time!")
        with open(host,"r+") as file:
            content = file.readlines()
            file.seek(0) #retornando o ponteiro para o inicio do documento
            for line in content:
                #se nao houver nenhum site da lista na linha, escreva a linha
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate() #apaga tudo para baixo no documento
                
               
    time.sleep(5) #faz o programa esperar 5 segundos

