import urllib.request
from bs4 import BeautifulSoup

def create_udnf(temp_array):
    global udnf
    udnf_array = []

    for i in range(len(temp_array)):
        temp_array[i] = temp_array[i].replace("</span>","").split('">')
        tmp = temp_array[i][1].replace(" <br/><br/><br/>","")
        udnf_array.append(tmp)

    udnf = ' + '.join(udnf_array)

url = 'http://ppi.madosonline.sk/index.php?b0=0&b1=0&b2=1&b3=0&b4=1&b5=0&b6=1&b7=x&pid=68&Transformuj=Transformuj'
web = urllib.request.urlopen(url)
content = web.read()
soup = BeautifulSoup(content,'html.parser')
par = soup.find_all('p')
 
dnf = str(par[14]).split('<sup>1*</sup>')
idnf = str(par[17])
udnf = ''
create_udnf(dnf[0].split(' + '))

print()
print(f'[udnf]: {udnf}')
#print(f'[SDNF]: {sdnf}')
#print(f'[IDNF]: {idnf}')
print()