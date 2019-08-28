"""
python으로 telegram message 보내기
"""

import requests

# requests.get('텔레그램으로 msg 보내는 url')
# requests.get("https://api.telegram.org/bot557013477:AAHpa5yr-HQyfmMzIVyHUvYVSa2b_GwMsrQ/sendMessage?chat_id=635763667&text=잘살아보세")

# 1. getUpdates을 통해 chat_id를 가져옴
url1 = "https://api.telegram.org/bot557013477:AAHpa5yr-HQyfmMzIVyHUvYVSa2b_GwMsrQ/getUpdates"
response = requests.get(url1)
# print(response) # 200뜨면 됩니다
# 콘솔에서 python lotto.py 입력해서 확인
# print(response.text) # 내용이 나옴
res_dict = response.json() # dictionary타입으로 가져옴
# print(res_dict)
# print(res_dict['result'][0]['message']['chat']['id'])


# url = base_url + token + method + str(chat_id) + msg
# url = f'{base_url}/bot{token}/getupdates'


# chat_id = res_dict['result'][c]['message']['chat']['id']

chat_id_list = []

result = res_dict['result']

for res in result:
    chat_id_list.append(res['message']['chat']['id'])
    # print(res['message']['chat']['id'])

chat_id_set = set(chat_id_list)


    

# 2. url을 조합하여 requests로 요청 보내기
token = '557013477:AAHpa5yr-HQyfmMzIVyHUvYVSa2b_GwMsrQ/'
base_url = 'https://api.telegram.org/'
# method = 'sendMessage?chat_id='

# msg = '&text=TeQuiero'

text = '와 자동화했다'
# url = base_url + token + method + str(chat_id) + msg
# url = f'{base_url}/bot{token}/getupdates'
# print(url)
# requests.get(str(url))
# requests.get("https://api.telegram.org/bot557013477:AAHpa5yr-HQyfmMzIVyHUvYVSa2b_GwMsrQ/sendMessage?chat_id=635763667&text=잘살아보세")

for c in chat_id_set:
    
    # url = base_url + token + method + str(c) + msg
    url = f'{base_url}bot{token}sendMessage?chat_id={c}&text={text}'
    
# print(url)
    requests.get(str(url))
# requests.get("https://api.telegram.org/bot557013477:AAHpa5yr-HQyfmMzIVyHUvYVSa2b_GwMsrQ/sendMessage?chat_id=635763667&text=잘살아보세")
