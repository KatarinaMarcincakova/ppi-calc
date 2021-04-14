import urllib.request
from bs4 import BeautifulSoup

def create_dnf(temp_array, delete):
    if 'SDNF = 1' in temp_array[0]: return '1'
    if 'SDNF = 0' in temp_array[0]: return '0'
    if 'UDNF =<br/>' in temp_array[0] or 'SDNF = </p>' in temp_array[0]: return 'empty'
    udnf_array = []

    #print(f'[TEMP_ARRAY]: {temp_array}')

    for i in range(len(temp_array)):
        temp_array[i] = temp_array[i].replace("</span>","").split('">')
        #print(f'[TEMP_ARRAY {i}]: {temp_array[i]}')
        tmp = temp_array[i][1].replace(delete,"")
        udnf_array.append(tmp)

    return ' + '.join(udnf_array)

def get_data(url):
    web = urllib.request.urlopen(url)
    content = web.read()
    soup = BeautifulSoup(content,'html.parser')
    par = soup.find_all('p')

    dnf = str(par[14]).split('<sup>1*</sup>')
    udnf = create_dnf(dnf[0].split(' + '), " <br/><br/><br/>")
    sdnf = create_dnf(dnf[1].split(' + '), "</p>")

    try: idnf = create_dnf(str(par[17]).split(' + '), "<br/> </p>")
    except: idnf = 'empty'
    print(f'{udnf}, {sdnf}, {idnf}\n')
    data.write(f'{udnf}, {sdnf}, {idnf}\n')

def d_to_t(n):
    global b
    i = 7
    while n > 0:
        b[i] = str(n % 3) if n % 3 != 2 else 'x'
        n = n // 3
        i -= 1

data = open("data.csv", "w", encoding="utf8")
for i in range(10):
    b = ['0'] * 8
    d_to_t(i)
    print(b)
    url = f'http://ppi.madosonline.sk/index.php?b0={b[0]}&b1={b[1]}&b2={b[2]}&b3={b[3]}&b4={b[4]}&b5={b[5]}&b6={b[6]}&b7={b[7]}&pid=68&Transformuj=Transformuj'
    print(f'[URL {i}]: {url}')
    get_data(url)

data.close()