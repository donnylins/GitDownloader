import os.path
import os
import sys
import urllib.request
from bs4 import BeautifulSoup

links = []
count = 0

print('''
   ___ _ _      ___                    _                 _           
  / _ (_) |_   /   \___  _ ____      _| | ___   __ _  __| | ___ _ __ 
 / /_\/ | __| / /\ / _ \| '_ \ \ /\ / / |/ _ \ / _` |/ _` |/ _ \ '__|
/ /_\\| | |_ / /_// (_) | | | \ V  V /| | (_) | (_| | (_| |  __/ |   
\____/|_|\__/___,' \___/|_| |_|\_/\_/ |_|\___/ \__,_|\__,_|\___|_|   

                                                                  V0.3
''')

def get_line(word):
    try:
        f = open("Downloads.txt","r+")  
        f.close()
    except FileNotFoundError:
        file = open("Downloads.txt", 'w+')
        file.close()

    with open('Downloads.txt') as f:
        for l_num, l in enumerate(f, 1): # percorrer linhas e enumera-las a partir de 1
            if word in l: # ver se palavra esta na linha
                return True
        return False # não foi encontrada
    
def CountFiles():
    global count
    path = os.getcwd()+'\\Downloads\\.'
    for name in os.listdir(path):
        count = count +1
    return count

def ProgrammingLanguage():
    print('''

       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
      |                                     |
      |======== Programing Languages =======|
      |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
      |                                     |
      |  1. Python        |   6. Java       |
      |  2. PHP           |   7. C++        |
      |  3. Ruby          |   8. C          |
      |  4. JavaScript    |   9. C#         |
      |  5. PowerShell    |   10. Go        |
      |                                     |
      |  100. Qualquer Linguagem            |
      |                                     |
       - - - - - - - - - - - - - - - - - - -  
          ''')
    
    selected = int(input("Selecione a opção: "))
    if selected == 100:
        lang = "https://github.com/search?q="
    elif selected == 1:
        lang = "Python"
    elif selected == 2:
        lang = "PHP"
    elif selected == 3:
        lang = "Ruby"
    elif selected == 4:
        lang = "JavaScript"
    elif selected == 5:
        lang = "PowerShell"
    elif selected == 6:
        lang = "Java"
    elif selected == 7:
        lang = "C%2B%2B"
    elif selected == 8:
        lang = "C"
    elif selected == 9:
        lang = "C%23"
    elif selected == 10:
        lang = "Go"
    else:
        print("[-] Nenhuma opção escolhida")
        sys.exit()
    return lang

def FileExists(name):
    if os.path.isfile(name):
        return True
    else:
        return False

def DownloadFile(url, search, language):
    file_name = url.split('/')[-3] +' - '+ url.split('/')[-4]
    u = urllib.request.urlopen(url)
    f = open('Downloads\\'+search+'\\'+language+'\\'+file_name+'.zip', 'wb')
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)

    f.close()
    print('[+] Arquivo %s baixado com sucesso' %file_name)
    
def get_links(page_url):
    page = urllib.request.urlopen(page_url)
    soup = BeautifulSoup(page, 'html.parser')
    all_links = soup.findAll('a', attrs={'class': 'v-align-middle'})
    for link in all_links:
        links.append('https://github.com'+(link.get("href")+"/archive/master.zip"))

def InitialConfig():
    try:
        os.mkdir("Downloads")
        print("[+] Pasta Downloads Criada")
    except FileExistsError:
        print("[!] Pasta Existente")
        
    if not FileExists("Downloads.txt"):
        ficheiro = open("Downloads.txt", "w")
        ficheiro.close()
        print("[+] Arquivo Downloads.txt Criado\n")
    else:
        print("[!] Arquivo Existente\n")

InitialConfig()

ToSearch = input("Search: ")
if ' ' in ToSearch:
    ToSearch = ToSearch.replace(' ','+')

os.mkdir("Downloads\\"+ToSearch)
Language = ProgrammingLanguage()
os.mkdir("Downloads\\"+ToSearch+"\\"+Language)
if len(Language) > 10:
    url = Language
else:
    url = "https://github.com/search?l="+Language+'&q='+ToSearch+"&type=Repositories"
    
get_links(url)

for i in links:
    if get_line(i):
        print("Arquivo já baixado!")
        continue
    else:
        file = open("Downloads.txt", 'a+')
        file.write(i+'\n')
        file.close()
        DownloadFile(i, ToSearch, Language)
