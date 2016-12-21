## unittest - UnitTest for Python

[unittest 라이브러리 사용법 보기](https://docs.python.org/2/library/unittest.html)

### 간단한 테스트 작성 후 실행하기

```python
import unittest

class DatabaseConnection:
  def connect(self):
    # blah blah blah~
    return True

class DatabaseTest(unittest.TestCase):
  def test_connect(self):
    conn = DatabaseConnection()
    self.assertTrue(conn.connect())

if __name__ == "__main__":
  unittest.main()
```

```bash
# run
$ python test1.py

# output (if testing succeed)
.
----------------------------------------------------------------------
Ran 1 test in 0.001s
OK

# output (if testing failed)
F
======================================================================
FAIL: test_connect (__main__.DatabaseTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jhlee/Workspace/study/python_temp/unittest/test1.py", line 11, in test_connect
    self.assertTrue(conn.connect())
AssertionError: False is not true
----------------------------------------------------------------------
Ran 1 test in 0.002s
FAILED
 (failures=1)
```

### 테스트 함수의 종류

##### assertEqual(expected, result, msg)
기대값과 결과값을 비교하고, 다르다면 s를 출력한다.

```python
class Tester(unittest.TestCase):
  def test_something(self):
    self.assertEqual(something.get_result(blah, blahblah), something.OK, msg="Something's wrong!")
```

#### assertNotEqual(expected, result, msg)
assertEqual과 반대로 동작한다.

#### assertTrue(result, msg)
기대값이 true인 경우 사용한다.

#### assertRaises(exception)
예외가 발생했는지 확인한다.

```python
import unittest

class DatabaseConnection:
  def connect(self, host):
    raise Exception("Unknown host: " + host)

class DatabaseTest(unittest.TestCase):
  def test_connect(self):
    conn = DatabaseConnection()
    
    with self.assertRaises(Exception) as context:
      conn.connect("127.0.0.1")

    self.assertTrue("Unknown host: 127.0.0.1", context.exception)

if __name__ == "__main__":
  unittest.main()
```language
```

### 실패한 테스트만 실행하기
```python
# example
$ python <테스트_소스>.py <테스트_케이스.테스트_함수>

# see
$ python test1.py DatabaseTest.test_connect
```


### 여러개의 테스트 파일을 한꺼번에 실행하기
```python
$ python -m unittest discover
```

### 테스트 수행 시, 반복되는 초기화/정리 로직은 하나의 함수로 묶기
 * [setUp](https://docs.python.org/2/library/unittest.html#unittest.TestCase.setUp)
 * [tearDown](https://docs.python.org/2/library/unittest.html#unittest.TestCase.tearDown)

```python
import unittest

class FormTestCase(unit test.TestCase):
  # 초기화
  def setUp(self):
    self.button = Button(“Login”)

  # 정리
  def tearDown(self):
    self.button.dispose()
    self.button = null

  def test_button_name(self):
    self.assertEqual(self.button.name(), “Login”, “Button.name() not matched.”)
```
