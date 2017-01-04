### Python Web Crawler Tutorials
간단한 샘플 코드를 작성하기에 앞서, 아래의 3가지 모듈을 설치한다.

## requests
`requests`는 파이썬에서 웹 상의 데이터를 처리할 때 주로 사용하는 모듈이다.
기본적으로 `GET`/`POST` 요청을 보내거나 `Response`를 받는 등의 HTTP Request를 주고받을 수 있다.
 * http://docs.python-requests.org/en/master/

```python
pip install requests
```

## BeautifulSoup
`BeautifulSoup`는 HTML, XML 파일에서 데이터를 읽어내는 대표적인 라이브러리로
`lxml`, `HTMLParser` 등의 파서와 함께 사용되며 Parse tree를 간편하게 탐색, 검색, 수정할 수 있다.
 * https://www.crummy.com/software/BeautifulSoup/bs4/doc/

```python
pip install beautifulsoup4
```

## lxml
`lxml`은 libxml2, libxslt 라이브러리의 파이썬 바인딩이다. (XML 파서)
`Python`에서 기본으로 제공되는 `HTMLParser`를 사용해도 되지만, `lxml`이 기능/속도 면에서 월등히 앞선다고 한다.
 * http://lxml.de

```python
pip install lxml
```

</br>
## 샘플코드 작성
http://codesimu.tistory.com 에 등록되어 있는 게시물 제목들을 가져오는 코드를 작성한다.
앞서 설치한 requests와 BeautifulSoup를 import 시킨다.
```python
import requests
from bs4 import BeautifulSoup
```
</br>

크롤링 동작을 할 함수를 만들어준다.
codesimu.tistory.com/[페이지번호] 형식으로 while 반복문을 통해 url을 설정한다.
```python
import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://codesimu.tistory.com/' + str(page)
        page += 1
```
</br>

대상 url의 데이터를 `requests.get(url)`로 가져와 텍스트 부분만 임의의 변수 `plain_text`에 저장한다.
그리고 가져온 데이터를 BeautifulSoup로 파싱하는데, 이 때 `lxml` 파서를 사용한다.
```python
import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://codesimu.tistory.com/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        page += 1
```
</br>

각 페이지의 타이틀에 해당하는 HTML 태그가 h2 > a 아래에 있는 값이므로
파싱한 데이터에서 아래와 같이 `soup.select('h2 > a')`로 가져온 뒤 해당 값을 출력한다.

```python
import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://codesimu.tistory.com/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for link in soup.select('h2 > a'):
            title = link.string
            print(title)

        page += 1
```