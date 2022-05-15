from django.urls import path
from . import views

'''
/input_output/urls.py는 프로젝트 이름이 input_output이라서 완전 기본값으로 준 urls.py를 먼저 참조하는데
거기에서 path('', include('inputoutput.urls')),라고 써놨으므로 이 파일(/inputoutput/urls.py) 내용을 참조하러 온다
이걸 보면 path를 ''로 둬서 127.0.0.1로 그냥 접속하면 views.py 에 있는 inputoutput을 찾아가도록 하고
path를 'result/'로 둬서 127.0.0.1/result로 접속하면 views.py에 있는 result를 찾아가도록 한다
'''

urlpatterns = [
    path('', views.inputoutput, name='inputoutput'),
    path('result/', views.result, name='result'),
    path('inputoutput_samepage/', views.inputoutput_samepage, name='inputoutput_samepage'),
]

