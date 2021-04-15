#pid UKNF f(a,b,c) 68
#pid UKNF f(a,b,c, d) 69
#pid UKNF f(a,b,c) 78

import urllib.request
from bs4 import BeautifulSoup

def create_knf(temp_array, delete):
    if 'SKNF = 1' in temp_array[0]: return '1'
    if 'SKNF = 0' in temp_array[0] or 'SkNF = 0' in temp_array[0]: return '0'
    if 'UKNF =<br/>' in temp_array[0] or 'SKNF = </p>' in temp_array[0]: return 'empty'
    uknf_array = []
    #print(f'[TEMP_ARRAY]: {temp_array}')

    for i in range(len(temp_array)):
        temp_array[i] = temp_array[i].replace("</span>","").split('">')
        #print(f'[TEMP_ARRAY {i}]: {temp_array[i]}')
        tmp = temp_array[i][1].replace(delete,"")
        uknf_array.append(tmp)

    return ' . '.join(uknf_array)

def get_data(url):
    web = urllib.request.urlopen(url)
    content = web.read()
    soup = BeautifulSoup(content,'html.parser')
    par = soup.find_all('p')

    knf = str(par[14]).split('<sup>1*</sup>')
    uknf = create_knf(knf[0].split(' . '), " <br/><br/><br/>")
    sknf = create_knf(knf[1].split(' . '), "</p>")

    knf = str(par[17]).split(' = ')
    if len(knf) == 2: 
        iknf1 = create_knf(knf[1].split(' + '), "<br/> </p>")
        iknf2 = 'empty'
    elif len(knf) == 3: 
        iknf1 = create_knf(knf[1].split(' + '), "<br/> Iknf<sub>2</sub>")
        iknf2 = create_knf(knf[2].split(' + '), "<br/> </p>")
    else: iknf1, iknf2 = 'empty', 'empty'

    #print(f'{uknf}, {sknf}, {iknf1}, {iknf2}\n')
    data.write(f'{uknf}, {sknf}, {iknf1}, {iknf2}\n')

def d_to_t(n):
    global b
    i = 15
    while n > 0:
        b[i] = str(n % 3) if n % 3 != 2 else 'x'
        n = n // 3
        i -= 1


for i in range(43046721):
    data = open("k4.csv", "a", encoding="utf8")
    b = ['0'] * 16
    d_to_t(i)
    #print(b)
    url = f'http://ppi.madosonline.sk/index.php?b0={b[0]}&b1={b[1]}&b2={b[2]}&b3={b[3]}&b4={b[4]}&b5={b[5]}&b6={b[6]}&b7={b[7]}&b8={b[8]}&b9={b[9]}&b10={b[10]}&b11={b[11]}&b12={b[12]}&b13={b[13]}&b14={b[14]}&b15={b[15]}&pid=79&Transformuj=Transformuj'
    #url = 'http://ppi.madosonline.sk/index.php?b0=0&b1=0&b2=0&b3=0&b4=x&b5=1&b6=0&b7=x&pid=68&Transformuj=Transformuj'
    #print(f'[URL {i}]: {url}')
    get_data(url)
    data.close()