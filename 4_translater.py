import requests

url = 'https://fanyi.baidu.com/sug'

while True:
    content = input("input:").strip()
    
    if content == "q":
        break

    data = {'kw': content}
    
    response = requests.post(url,data)

    if response.status_code == 200:
        resp = response.json()
        for data in resp['data']:               #data={'k':'','v':[]}
            #for v in data['v']:                     #v='int 打招呼，哈喽‘’
            #print(v)
            print(data['v'])
    