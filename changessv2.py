#
# Author : Wharton Wang
# scrap web and write the info. to json file
#
# D:\d.Download\Compressed\Shadowsocks-4.0.10
#
#

url = 'https://my.ishadowx.net/'
filename = 'D:\d.Download\Compressed\Shadowsocks-4.0.10\gui-config.json'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
}

import json
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup


# Define getting free server's port and password function
def get_port_pass():
           
    #    print(lastline)
    gamm = []
    req = Request(url,headers=header)
    webcont = urlopen(req)
    data = BeautifulSoup(webcont.read(),'lxml')
    alpha = data.findAll("div",{"class": "hover-text"})
    for al in alpha:
        h4s = al.findAll('h4')
        IP = h4s[0].span.string.strip()
        Port = h4s[1].span.string.strip()
        Password = h4s[2].span.string.strip()
        Method = h4s[3].string.strip()
        beta = IP,Port,Password
        gamm.append(beta)
    gamm = list(set(gamm))
   # print(gamm)

# Get japan servers info
    delta = []
    for ga in gamm:
   #     print(ga[0])
        if ga[0].startswith('jp') == True:
            delta.append(ga)

    return delta


# Define writing the port and password to the shadowsocks json file
def write_port_pass(fname,params):
    with open(fname,'r') as f:
        json_data = json.load(f)
        json_data_config = json_data['configs']
#   print(json_data)
        for item in json_data_config:
            for p in params:
                if item['server'] == p[0]:
                    item['server_port'] = p[1]
                    item['password'] = p[2]
    f.close()

    with open(fname,'w') as f:
        json.dump(json_data,f,indent=2)
        print('json written')
    f.close()

# Run the get port and password 
params = get_port_pass()
# Run the write 
write_port_pass(filename,params)
print(params)
print("writing done!!")
