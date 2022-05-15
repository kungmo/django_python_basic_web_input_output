from django.db import models

# Create your models here.
'''
파이썬으로 구현한 함수가 들어갈 곳이다.
여기에 선생님들께서 원하는 기능을 구현하셨던 함수를 넣고 함수의 입력 변수로 content1과 content2를 입력 받는다.
myfunction1이라는 함수가 돌아간 후 돌려줄 값을 return 뒤에 써준다. 돌려준 값은 views.py에서 받아서 쓸 수 있다.
여기에 함수를 여러 개 넣어서 추가할 수도 있다.
'''

# 두 입력값을 합치는 간단한 함수. 숫자끼리면 더하고, 숫자 아닌 것 같아서 오류가 나면 그냥 문자열을 붙여서 돌려주는 함수
def myfunction1(content1, content2):
    try:
        sum = int(content1) + int(content2)
        return "content1과 content2를 합치면 {0}이다".format(sum)
    except:
        sum = content1 + content2
        return "content1과 content2 문자열을 붙이면 {0}이다".format(sum)