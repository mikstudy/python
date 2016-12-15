* 출처</br>
  예제로 배우는 Python 프로그래밍: [http://pythonstudy.xyz/python/django](http://pythonstudy.xyz/python/django)</br>
  Django Girls Tutorial: [https://tutorial.djangogirls.org/ko/django/](https://tutorial.djangogirls.org/ko/django/)


###	Django?
`Django(/ˈdʒæŋɡoʊ/ jang-goh/쟁고/장고)`는 파이썬으로 만들어진 무료 오픈소스 웹 어플리케이션 프레임워크(Web application famework)이다.


### 어디에서 사용되는가?
 - Instagram
   Instagram의 Application 서버로 Django가 사용
   
 - Pinterest
   디자인계통 사람들이 많이 사용한다는 이미지 기반 SNS 서비스.
 
 - BitBucket
   Git Reposotory 서비스.

### Django의 특징
  - ORM(Object-Relational Mapping) 추상화 계층</br>
    Django에는 DB Adaptor와 유저 프로그램 사이에 자료형의 변환작업을 자동으로 수행해주는 ORM(Object-Relational Mapping)계층이 존재.
    Model을 설계할 때 파이썬에서 사용하는 자료형들을 그대로 사용할 수 있으며, Table에 정확히 어떤 Type의 Field로 저장되는지 신경쓸 필요가 없다.
	```python
	from django.db import models

    class Food(models.Model):
    	name = models.CharField(Max_lenth=100)
        price = models.IntergerField(default=0)

	users = User.objects.all()
    ```
   ```language
   SELECT --> Est.objects.all() 
           --> Est.objects.filter(id__contains='1')
           --> exclude, get, count,...
  INSERT --> Est.objects.create(name='a',...)
  UPDATE --> est = Est.objects.get(id=1)
               est.name = b; est.save()
  DELETE --> est.delete()
   ```
   
  - Backend Console</br>
	Django에서는 백엔드 콘솔로 제공되는 `manage.py`를 사용해서 모든 백엔드 관리를 수행할 수 있다.
    예를 들어, 완성한 프로젝트를 서버에 옮긴 뒤 다음 명령을 실행하면 설치된 모듈(App)에 정의된 Model들을 검사해서 필요한 DB Table들을 자동으로 생성
    ```bash
	./manage.py migrate
	```
    기본적으로 제공되는 Command 외에, 별도로 Custom Command를 정의해서 manage.py에서 실행 가능하도록 할 수 있다. 각 모듈(App)내에 필요한 명령들을 정의해놓으면 manage.py에서 이 명령을 찾아내서 실행할 수 있다.

  - 모듈화 구성과 모듈의 독립성</br>
    Django는 사이트의 기반이 되는 프로젝트(Sitebase)와 특정 기능을 수행하는 모듈(App)들이 상호 독립적. 따라서 모듈에서 사용하는 Model들은 각 모듈 디렉토리 내에 정의하게 되어 있고, 이미지나 CSS등의 Static File들도 각 모듈 디렉토리 내에 각각 따로 저장하도록 되어 있다.

  **프로젝트(Sitebase)**는 Python환경이나 DB설정, URL Routing과 같이 사이트 전역에 적용되는 자원과 설정들을 관리하고, 관리를 위한 Backend Console을 제공
  
  **모듈(App)**은 사이트에서 실질적인 기능을 수행하며, 필요에 따라 Sitebase에 설치하거나 제거할 수 있다. App에 종속적인 자원인 Model와 Static File들은 모두 모듈 디렉토리 내에 저장되므로 Sitebase와 다른 App에 독립적이다. 따라서 사이트 개발을 모듈 단위로 수행할 수 있다. 완성된 App을 배포할 경우 App디렉토리만 따로 떼어서 전달하면 된다.
    

### 가상환경
1. 가상 환경
  가상 환경(Virtual Environment)는 사용자가 정한 임의의 디렉토리 밑에 Python과 관련 패키지 등을 함께 넣어 그 안에서 독립적인 파이썬 개발 환경을 만들수 있다. 즉, 가상 환경은 파이썬 개발 환경으로서 필요한 경우 한 개발머신 안에 여러 개의 가상 환경을 만들고 각 가상 환경에서 다른 파이썬 버전이나 다양한 패키지들을 독립적으로 설치 가능할 수 있다.
<br>

2. 가상 환경 만들기
  - 윈도우, 맥OS
  ```bash
  임의폴더> python -m venv [가상환경이름]
  ```
  `[가상환경이름]` 소문자여야하고, 공백 및 특수문자 사용불가
<br>

3. 가상 환경 사용하기
  - 윈도우
  ```bash
  임의폴더> [가상환경이름]\Scripts\activate
```
  - 리눅스와 맥OS
  ```bash
  임의폴더> source [가상환경이름]/bin/activate
  미동작시) .[가상환경이름]/bin/activate
```
  - 정상 동적(콘솔의 프롬프트 변경)
  ```bash
  ([가상환경이름] c:\~~~~)
```

### Django 설치
- Django는 `pip`이라는 유틸리티를 사용하여 설치. 가상환경에서 Django를 설치하기 위해서는 먼저 가상환경을 실행하고 `pip` 패키지 매니저를 사용하여 Django를 설치한다.
```bash
([가상환경이름]) pip install django(최신버전설치)
([가상환경이름]) pip install django==1.8(특정버전설치)
```

### Django 프로젝트 생성
- Django에서 새로운 웹 프로젝트를 만들기 위해서는 `django-admin.py`라는 Django 관리자 모듈을 사용한다.
```bash
python -m venv [생성한 가상환경이름] - 가상환경 실행
[프로젝트를 디렉토리로 이동]
[가상환경이설치된 폴더]\Script\django-admin.exe startproject [프로젝트명]
```
- 위의 명령은 새 프로젝트 이름의 서브폴더를 생성하고, 프로젝트 안에 아래 그림과 같이 몇개의 파일들을 생성된다.
```language
-- manage.py (웹 프로젝트 개발, 관리하는데 필요한 여러 기능 제공)
-- [프로젝트폴더]
    ㄴ__init__.py 
    ㄴsettings.py (웹 프로젝트의 세팅을 설정)
    ㄴurls.py (URL 매핑을 위한 파일)
    ㄴwsgi.py
```

### Django 서버 실행
  - 웹 프로젝트로붙터 웹 서비스를 시작하기 위해서는 `manage.py runserver`를 실행.
  ```bash
  [가상환경실행] python manage.py runserver(윈도우)
  [가상환경실행] ./manage.py runserver(맥OS)
  
  #특정포트 사용(8080) 사용시
  python manage.py runserver 8080
```

### Django HelloWorld!
- views.py 추가
```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")
```

- urls.py 수정
```python
from django.conf.urls import url
from django.contrib import admin
from HelloWorld.views import hello

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
]
```
