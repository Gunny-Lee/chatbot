"""
requests를 통해 Bithumb open API 활용하여, 실시간 BTC(Bitcoin) 현재가를 출력하는 crypto.py
"""

import requests

# 1. requests 통해 요청 보내기
url = "https://api.bithumb.com/public/ticker/"
response = requests.get(url)
# print(response) # 200뜨면 됩니다
# 콘솔에서 python lotto.py 입력해서 확인
# print(response.text) # 내용이 나옴
res_dict = response.json() # dictionary타입으로 가져옴
print(res_dict)
print(res_dict['data']['opening_price'])

# result = []
# result.append(res_dict['drwtNo1'])
# result.append(res_dict['drwtNo2'])
# result.append(res_dict['drwtNo3'])
# result.append(res_dict['drwtNo4'])
# result.append(res_dict['drwtNo5'])
# result.append(res_dict['drwtNo6'])
# print(result)
