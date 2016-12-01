### Python 문법
`Python`은 `{}`(Braket) 같은 블럭 구분 대신 들여쓰기로 코드블럭을 구분하는데, 이는 파이썬의 가장 큰 특징 중 하나이다.
코드 작성이 편하다는 장점이 있지만 들여쓰기 공백을 다르게 쓴다면(협업을 할때) 바로 `unexpected indent error`가 발생한다.

### 제어문

  * if문
    ```python
    if 조건문:
    	...
    elif 조건문:
    	...
    else:
    	...
    ```
    
  * while문
	```python
    x = 0
    while x < 10:
    	x = x + 1
    	...
    ```
  * for문
    ```python
    for 변수 in 리스트
    	...
    ```
    
### 자료형
  * List
    ```python
    a = [ ]
    b = [1, 2, 3]
    c = ['Life', 'is', 'too', 'short']
    d = [1, 2, 'Life', 'is']
    e = [1, 2, ['Life', 'is']]

    b[1]
     >>> 2
    d[:2]
     >>> [1,2]

    b.append(4)
     >>> [1, 2, 3, 4]
    d.insert(4, "too short")
     >>> [1, 2, 'Life', 'is', 'too short']
    b + c
     >>> [1, 2, 3, 'Life', 'is', 'too', 'short']

    b.pop(2)
     >>> [1, 2]
    d.remove("is")
     >>> [1, 2, 'Life']

    c.sort()
     >>> ['Life', 'is', 'short', 'too']
    b.reverse()   
     >>> [3, 2, 1]
    ```
  * Set
    `파이썬 2.3`부터 지원하기 시작한 자료형으로, 집합에 관련된 것을을 쉽게 처리하기가 용이하다.
    Set은 중복을 허용하지 않고 순서의 개념이 없다. 따라서 인덱싱으로 값을 얻을 수 없다.
    ```python
    s1 = set([1, 2, 3, 4, 5, 6])
    s2 = set([4, 5, 6, 7, 8, 9])
    s2 = set("Hello")
    s1 & s2 
    s1.intersection(s2)
     >>> {4, 5, 6}
    s1 | s2
    s1.union(s2)
     >>> {1, 2, 3, 4, 5, 6, 7, 8, 9}
    s1 - s2
    s1.difference(s2)
     >>> {1, 2, 3}
    s1.add(7)
     >>> {1, 2, 3, 4, 5, 6, 7}
    s2.update([10, 11, 12])
     >>> {4, 5, 6, 7, 8, 9, 10, 11, 12}
    s1.remove(2)
     >>> {1, 3, 4, 5, 6}
    ```
  * Tuple
  읽기 전용으로 사용된다. 리스트와 비교해서 속도가 빠르다는 장점이 있지만, 한번 지정한 값을 바꿀수 없고 리스트에 비해 제공되는 함수가 적다.
    ```python
    t1 = ()
    t2 = (1,)
    t3 = (1, 2, 3)
    t4 = 1, 2, 3
    t5 = ('a', 'b', ('ab', 'cd'))

    a = list(t3)
    type(a)
     >>> <type 'list'>    

    b = set(t3)
    type(b)
     >>> <type 'set'>
    ```
  * Dictionary  
	```python
    dic = {'name':'sim', 'phone':'01035671689', 'birth': '0208'}
    
    dic['sex'] = 'male'
     >>> {'phone': '01035671689', 'name': 'sim', 'birth': '0208', 'sex': 'male'}
    del dic['birth']
     >>> {'phone': '01035671689', 'name': 'sim'}

	dic.keys()
     >>> dict_keys(['name', 'phone', 'birth'])
    dic.values()
     >>> dict_keys(['sim', '01035671689', '0208'])
    ```

### 함수
  * 정의
  	함수는 def(define의 약자) 라는 키워드로 정의한다. 위에서 설명했듯 `{}`을 사용하지 않고 들여쓰기로 블럭을 구분한다. 
    ```python
    def sum(a, b): 
    	return a + b
    ```
  * 여러개의 인수를 받는 함수
  	```python
    def sum_many(*args): 
    	sum = 0 
    	for i in args: 
        	sum = sum + i 
    	return sum 

    ```
  * 함수 내에서 전역변수 설정
  	```python
    def func():
        global n
        n = n * 10
    
    func()
    print (n)
    ```
    
### 클래스
  * 정의
  	클래스 내에서 함수가 정의될 때는 꼭 첫 번째 인수로 `self`가 들어가야 한다. 이 `self`는 현재의 인스턴스 객체를 가리키는 기능을 하는데 말 그대로 자기자신을 가리킨다고 보면 된다.
    
  	```python
    class 클래스이름[(상속 클래스명)]:
        <클래스 변수 1>
        <클래스 변수 2>
        ...
        def 클래스함수1(self, 인수1, 인수2,,,]):
            <수행할 문장 1>
            <수행할 문장 2>
            ...
        def 클래스함수2(self, 인수1, 인수2,,,]):
            <수행할 문장1>
            <수행할 문장2>
        ...
    ```
    
  * 계산기 만들기
  	```python
    class Calculator:
        def __init__(self):
            self.result = 0

        def adder(self, num1, num2):
            self.result = num1 + num2
            return self.result

    cal = Calculator()
    print(cal.adder(5, 10))
    ```
    
  * 상속
    ```python
    class Calculator_Extend(Calculator):
        def adder(self, num1, num2):
            self.result = num1 + num2 
            print('result : %s' % (self.result))
            return self.result
    
    cal2 = Calculator_Extend()
	print(cal2.adder(10,20))
    ```






