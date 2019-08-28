"""
requests를 통해 동행복권 API 요청을 보내어, 1등 번호를 가져와 python list로 만듬
"""

import requests

# 1. requests 통해 요청 보내기
url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873"
response = requests.get(url)
# print(response) # 200뜨면 됩니다
# 콘솔에서 python lotto.py 입력해서 확인
# print(response.text) # 내용이 나옴
res_dict = response.json() # dictionary타입으로 가져옴
# print(res_dict)
# print(res_dict['drwtNo1'])

result = []
# result.append(res_dict['drwtNo1'])
# result.append(res_dict['drwtNo2'])
# result.append(res_dict['drwtNo3'])
# result.append(res_dict['drwtNo4'])
# result.append(res_dict['drwtNo5'])
# result.append(res_dict['drwtNo6'])
# print(result)

for i in range(1,7):
    result.append(res_dict[f'drwtNo{i}'])