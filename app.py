from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

# 1. 주문서를 만들고,
# 2. 해당 주문이 들어왔을 때 무엇을 할지 정의

@app.route('/name')
def name():
    return '이건희'

@app.route('/hello/<name>')
def hello(name):
   # return 'hello ' + name
   # return 'hello {}'.format(name)
    return f'hello {name}'         # 오늘날 많이 사용한다.

@app.route('/square/<int:number>')
def square(number):
    # number를 제곱하여 반환
    return str(number ** 2)

@app.route('/menu')
def menu():
    foods = ['바스버거', '대우식당', '진가와', '고갯마루']
    food = random.choice(foods)
    return food

@app.route('/lotto')
def lotto():
    winner = [3,5,12,13,33,39]
    lottos = random.sample(range(1, 46), 6) # 리턴값이 list로 나와서 오류
    # return str(sorted(lottos))

    # winner와 lottos의 리스트를 비교하는 구문
    dap = []
    for i in winner:
        if i in lottos:
            dap.append(i)
    
    if len(dap) == 6:
        return (str(sorted(lottos)) + " 1등")
    elif len(dap) == 5:
        return (str(sorted(lottos)) + " 3등")
    elif len(dap) == 4:
        return (str(sorted(lottos)) + " 4등")
    elif len(dap) == 3:
        return (str(sorted(lottos)) + " 5등")    
    else:
        return (str(sorted(lottos)) + " 꽝")
    # 만약 6개가 모두 일치하면 1등
    
    # 만약 5개가 일치하면 3등

    # 만약 4개가 일치하면 4등

    # 만약 3개가 일치하면 5등

    # return str(sorted(lottos)) + 등수

@app.route('/lotto2')
def lotto2():
    winner = [3,5,12,13,33,39]
    lottos = random.sample(range(1, 46), 6) # 리턴값이 list로 나와서 오류
    cnt = len(set(winner) & set(lottos))

    rank = "꽝"
    if cnt == 6:
        rank = "1등"
    elif cnt == 5:
        rank = "3등"
    elif cnt == 4:
        rank = "4등"
    elif cnt == 3:
        rank = "5등"
    
    return str(sorted(lottos)) + rank