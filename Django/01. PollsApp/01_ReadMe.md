* 출처</br>
  SCHOOL OF WEB: [http://schoolofweb.net/](http://schoolofweb.net/)


###	Django Projects vs Apps

```language
Projects vs Apps
앱이란 어떠한 기능을 하는 웹 어플리케이션
	ex) 웹 블로그 시스템, 투표 어플리케이션
프로젝트란 특정 웹 사이트의 어플리케이션들로 이루어진 집합.
프로젝트는 여러개의 앱을 포함할 수 있으며, 하나의 앱은 여러개의 프로젝트에 포함 될 수 있습니다.
 ```

### Django App 생성

```bash
> python manage.py startapp [polls]
```

```language
[polls]/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

### Django View

```python
## [polls]/views.py ##
from django.http import HttpResponse

def index(req):
	return HttpResponse("Hello, world.");
```
</br>
URLConf를 만들어 생성된 뷰 URL에 맵핑
`[polls]/urls.py` 생성
```python
## [polls]/urls.py ##
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```
`url()` argument: regex - 정규식 패턴
`url()` argument: view - 일치하는 패턴을 찾으면, url() 인수로 전달된 특정 view 함수 실행합니다.
`url()` argument: name - URL에 이름을 지정하면 장고 앱 어딘가에서 템플릿과 같은 파일에서 참조가 가능합니다.

</br>
루트(Projects) URLConf가 `[polls]/urls` 맵핑
```python
## [Projects명]/urls.py ##
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
```
`Include()`: 다른 URL 패턴을 포함시킬 때 사용, `admin.site.urls`은 예외
</br>
생성한 뷰가 정상동작하는지 확인
```bash
> python manage.py runserver
## http://localhost:[포트]/[polls]/
```

### 데이터베이스 설정
```python
## [프로젝트]/settings.py ##
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        ## 'django.db.backends.postgresql','django.db.backends.mysql', 'django.db.backends.oracle' 
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
`ENGINE`: 데이터베이스 엔진을 설정합니다.
`NAME`: 데이터베이스 이름. SQLite를 사용 시 파일 이름을 포함한 절대 경로를 입력합니다.
```python
## 다른 데이터베이스 사용 시 ##
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

### 타임존 설정
```python
## [프로젝트]/settings.py ##
TIME_ZONE = 'Asia/Seoul'
```

### Django Default App
Django 프로젝트를 생성하면 기본 제공되는 Django App
```python
INSTALLED_APPS = [
    'django.contrib.admin',		# 관리자 사이트
    'django.contrib.auth',		 # 인증 시스템
    'django.contrib.contenttypes', # 컨텐츠 타입을 위한 프레임워크
    'django.contrib.sessions',	 # 세션 프레임워크
    'django.contrib.messages',	 # 메세지 프레임워크
    'django.contrib.staticfiles',  # Static 파일 관리를 위한 프레임워크
]
```
</br>
기본 제공하는 App 중에는 최소 한개 이상의 데이터베이스 테이블을 사용하기 때문에, 사용하기 전에 테이블을 생성할 필요가 있습니다.
```bash
> python manage.py migrate
```
`migrate`: `INSTALLED_APPS`를 확인하고 `[프로젝트]/settings.py` 파일과 기본 어플리케이션이 가지고 있는 데이터베이스 마이그레이션 파일에 따라 필요한 테이블을 생성합니다.

#### 모델 생성
```python
## [polls]/models.py ##
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
`Field` 클래스를 정의할 때 첫번째 옵션 인수를 사용하면, 설정된 이름으로 표시(실제 데이터베이스 Field값이 변경되는 건 아님)

#### 모델 활성화
- 이 앱의 데이터베이스 스키마 생성(CREATE TABLE statements).
- Question 과 Choice 오브젝트에 엑세스 할 수 있는 Pythone database-access API 사용

</br>
`INSTALLED_APPS` 에 생성한 `[앱]` 추가합니다.
```python
## [프로젝트]/settings.py ##
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
Django 프로젝트에 생성한 `[앱]` 추가 후 밑의 명령어 수행합니다.
```bash
> pythone manage.py makemigrations [polls]
##
Migrations for 'polls':
  polls/migrations/0001_initial.py:
    - Create model Choice
    - Create model Question
    - Add field question to choice
```
`makemigrations`: 새로 추가한 파일이나 변경된 파일이 있음을 알려주고, 변경된 내용을 Migration 파일에 저장합니다.
</br>
```bash
> python manage.py sqlmigrate [polls] 0001
```
`sqlmigration`: 실제 SQL 명령어를 실행하지 않고, 실행될 내용만을 확인합니다.
`check`: 마이그레이션 시작하거나 데이터베이스를 변경하기 전에 문제를 확인합니다.
</br>
```python
> python manage.py migrate
##
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
```
`migrate`: 실행되지 않은 모든 마이그레이션을 적용합니다.
`django_migrations` 테이블에 마이그레이션을 기록하여 모델의 변경된 내용을 확인합니다.

#### API 사용하기
```bash
> python manage.py shell
```
#####database API 사용
```bash
>>> from polls.models import Question, Choice   # 우리가 만든 모델 클래스를 임포트 합니다.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# 새로운 Question 오브젝트 생성.
# 타임존 서포트가 디폴트 settings 파일에 활성화되어 있으므로,
# pub_date에 datetime.datetime.now()이 아닌
# timezone.now()을 사용하여 tzinfo를 포함하고 있는 datetime을 대입하여 주십시오.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# 위에서 클래스 오브젝트를 생성하였지만 메모리상에만 만든것이고 아직 데이터베이스에 저장되지는 않았습니다.
# save() 명령어를 실행하여 데이터베이스에 저장을 해봅시다.
>>> q.save()

# 이제 오브젝트가 ID를 가진 것을 볼 수 있습니다.
# 데이터베이스에 따라 "1"가 아니고 "1L"를 출력하는 경우가 있습니다.
# 이것은 사용하고 있는 데이터베이스가 integetr를 long integer 오브젝트로 리턴하기 때문이니 아무 문제 없습니다.
>>> q.id
1

# 파이썬 속성을 통해 모델의 필드에 엑세스해 보십시오.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# 파이썬 속성을 변경하여 필드 값을 변경한 후, save() 함수를 실행하여 주십시오.
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() 클래스 메소드는 데이터베이스에 있는 모든 question 오브젝트를 보여줍니다.
>>> Question.objects.all()
<QuerySet [<Question: Question object>]>
```
</br>
 `<Question: Question object>` 확인할 수 있도록 `__str__()` 함수 추가합니다.
```python
## [polls]/models.py ##
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):  # __unicode__ on Python 2
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):  # __unicode__ on Python 2
        return self.choice_text
```
</br>
테스트를 위한 커스텀 메소드 추가합니다.
```python
## [polls]/models.py ##
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```
</br>
Object 확인 및 커스텀 메소드 확인을 위해 다시 `Shell`을 실행합니다.
```bash
> python manage.py shell
```
```bash
>>> from polls.models import Question, Choice

# 조금 전에 추가한 __str__() 메소드가 출력한 내용을 확인하십시오.
>>> Question.objects.all()
<QuerySet [<Question: What`s up?>]>

# 장고는 키워드 인수를 이용한 강력한 데이터베이스 검색 API 를 제공합니다.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What`s up?>]>
>>> Question.objects.filter(question_text__startswith=`What`)
<QuerySet [<Question: What`s up?>]>

# 올해 개제된 질문을 검색해봅시다.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What`s up?>

# 존재하지 않는 ID를 검색하면 에러 메세지가 출력됩니다.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# 데이터베이스의 기본키로 검색하는 것이 가장 보편적이기에
# 장고는 기본키 검색 쇼트컷 (shortcut) 을 제공합니다.
# 밑의 코드는 Question.objects.get(id=1)와 같습니다.
>>> Question.objects.get(pk=1)
<Question: What`s up?>

# 이번에는 우리가 만든 커스텀 메소드가 잘 실행되는지 확인합시다.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Question에 2개의 Choice를 추가해보죠. create 콜은 새로운 Choice 오브젝트를 만들고,
# 데이터베이스의 INSERT 구문의 역할을 하며, 새로운 choice를 기존의 choice 세트에 추가 하고,
# 새로 만든 Choice 오브젝트를 리턴합니다. (한 문장이 엄청 기네요;;)
# 장고는 외래키 관계의 반대편 오브젝트의 세트를 가지고 있습니다.
# (e.g. question이 가지고 있는 choice 세트) 이것들은 API를 통해 액세스할 수 있습니다.
>>> q = Question.objects.get(pk=1)

# 기본키가 1인 Question 오브젝트가 관계하고 있는 choice 세트를 출력해 봅시다. -- 아직 아무것도 없습니다.
>>> q.choice_set.all()
<QuerySet []>

# 3개의 choice를 추가해보죠.
>>> q.choice_set.create(choice_text=`Not much`, votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text=`The sky`, votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text=`Just hacking again`, votes=0)

# Choice 오브젝트는 자신이 관계하고 있는 Question 오브젝트에 액세스할 수 있는 API를 가지고 있습니다.
>>> c.question
<Question: What`s up?>

# 반대로 Question 오브젝트도 Choice 오브젝트에 액세스할 수 있는 API를 가지고 있습니다.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# API는 자동으로 모든 관계를 추적합니다.
# 더블 언더스코어를 사용하여 관계를 연결합니다.
# 이것은 제한 없이 원하는 만큼 연결할 수 있습니다.
# pub_date가 올해인 모든 Choice 오브젝트를 검색하여 봅시다.
# (위에서 만든 변수인 'current_year'를 다시 사용합시다.
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# delete()을 사용하여 이 중 하나의 choice를 삭제해 보죠.
>>> c = q.choice_set.filter(choice_text__startswith=`Just hacking`)
>>> c.delete()
(1, {u`polls.Choice`: 1})
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>]>
```
