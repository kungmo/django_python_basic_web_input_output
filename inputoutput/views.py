from django.shortcuts import render
from .models import myfunction1 # model.py에 있는 myfunction함수 가져오기
from django import forms
from django.http import HttpResponseRedirect

# Create your views here.

'''
/inputoutput/urls.py에서 result로 가라고 하면 /templates/inputoutput/result.html을 돌려준다
inputoutput.html에서 content1과 content2를 입력 받으면
models.py에서 실제 기능을 구현할 함수 myfunction1을 불러와서 content1과 content2를 집어 넣어서
myfunction1_result 함수에서 나온 값을 받아 myfunction1_result에 넣는다.
data 속에 딕셔너리 형태로 content1, content2, myfunction1_result를 넣고
result.html로 content1, content2, myfunction1_result를 보내준다.
'''
def result(request):
    # content1과 content2를 입력받아서 result.html로 POST 방법을 써서 보냄
    if request.method == 'POST':
        content1 = request.POST['content1']
        content2 = request.POST['content2']
        myfunction1_result = myfunction1(content1, content2)
        data = { 'content1': content1, 'content2': content2, 'myfunction1_result':myfunction1_result }
        return render(request, 'inputoutput/result.html', data)

# /inputoutput/urls.py에서 inputoutput으로 가라고 하면 /templates/inputoutput/inputoutput.html을 돌려준다
def inputoutput(request):
    return render(request, 'inputoutput/inputoutput.html')


def inputoutput_samepage(request):
    if request.method == 'POST':
        content1 = request.POST['content1']
        content2 = request.POST['content2']
        myfunction1_result = myfunction1(content1, content2)
        data = { 'content1': content1, 'content2': content2, 'myfunction1_result':myfunction1_result }
    else:
        myfunction1_result = "입력 없음"
        data = {'myfunction1_result': myfunction1_result}
    return render(request, 'inputoutput/inputoutput_samepage.html', data)