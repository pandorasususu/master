# 2022.06.27

[toc]

## JAVA

### 1. JAVA 특징

**1.1 Write Once, Run Anywhere**

c++ 등의 언어같은 경우에는 소스코드를 만들고 컴파일을 통해 binary code가 작성되면 os이나 ram같은 기계가 이를 읽고 동작시켜줌. 이런 과정이 운영체제에 종속적이기 때문에 특정 os에서 만든 프로그램을 다른 os에서 동작시킬 수 없음. <==>

java는 .java로 작성된 코드를 컴파일을 통해 .class 형태의 바이트코드로 만들고, 이것이 JVM(Java Virtual Machine)이 동작시킴. os 종류와 상관없이 JVM만 설치되어있으면 동작시킬 수 있다. 플랫폼 독립적

**1.2 Garbage Collection**

더 이상 사용하지 않는 메모리를 자동적으로 정리하는 기능

**1.3 JAVA 객체지향 특징**

OOP is A.P.I.E

Abstraction, Polymorphism, Inheritance, Encapsulation



### 2. 변수란?

컴퓨터에서 할당된 데이터를 저장하는 메모리 공간

기본형 primitive: 미리 정해진 크기의 데이터, 변수 자체에 값을 저장

논리형: boolean
정수형: byte(8bit, -2^7~2^7-1), short(16bit, -2^15~2^15-1), int(기본형, 32bit, -2^31~2^31-1), long(64bit, -2^63~2^63-1, 맨 뒤에 L붙임), <맨 앞의 bit는 sign bit>

```
정수형 데이터의 최댓값을 넘어가는 값을 입력하면 리셋되어 최솟값으로 간다. 논리적으로는 오류가 맞으나 컴퓨터는 에러를 출력하지 않는다. overflow 상황
```

실수형: float(32bit, 맨 뒤에 f붙임), double(기본형, 64bit), <둘의 차이점은 정밀도, double이 더 정밀함>

```
실수의 연산은 근사값으로 하기 때문에 부정확하다.
```

문자형: char(16bit), 내부적으로 ascii와 unicode로 지정된 값 사용, <문자형은 single quotation ''으로 표현하는 한글자, 문자열은 double quotation ""으로 표현하는 1개 이상의 글자들>

참조형 reference: 크기가 정해지지 않은 데이터,  변수에는 값을 참조할 수 있는 주소 저장
=> 기본형 이외의 모든 데이터 타입



### 3. 형변환 Type casting

기본형끼리, 참조형끼리 형 변환 가능

boolean은 다른 기본형과 호환되지 않음

기본형과 참조형의 형변환은 wrapper 클래스를 통해서 가능

묵시적 형 변환: 값의 손실이 발생하지 않음 <==> 명시적 형 변환: 값의 손실 발생 



### 4. JAVA 연산자

**4.1 연산자 기본**

이항 연산자는 연산 전에 피연산자의 타입을 일치시킨다. 
이 때 두개의 피연산자 중 더 큰 타입으로 형변환이 이루어진다.
피연산자의 크기가 4byte(int) 미만이면 int로 변경후 연산이 진행된다.
++이나 --는 값이 아닌 변수에만 적용 가능하다.

**4.2 비트 논리 연산자**

& 두 피연산자 모두 1이면 1, 그 외에는 0
| 두 피연산자 모두 0이면 0, 그 외에는 1
^  두 피연산자 값이 다르면 1, 같으면 0
~ 피연산자의 비트가 1이면 0, 0이면 1

**4.3 비트 이동 연산자**

<< 앞의 피연산자 비트 열을 뒤 피연산자 만큼 왼쪽으로 이동하고, 이동에 따른 빈 공간은 0으로 채움
 ex) int a = 10; int b = a << 1; => a = 20

">>" 앞의 피연산자 비트 열을 뒤 피연산자 만큼 오른쪽으로 이동하고 이동에 따른 빈 공간은 음수는 1, 양수는 0으로 채움

ex) ex) int a = 10; int b = a >>1; => a = 5

">>>" 앞의 피연산자 비트 열을 뒤 피연산자만큼 오른쪽으로 이동하고 이동에 따른 빈 공간은 0으로 채움

**4.4 논리 연산자**

short circuit 연산자: &&, || 



### 5. JAVA 조건문

switch() 안에 들어올 수 있는 것들

=> 정수호환(double, float는 사용 못함), Enum, Class Object(wrapper) , Method Call

```java
Enum(enumeration type, 열거체)
앞으로 바뀌지 않을, 관련이 있는 상수들의 집합 ex) 요일들의 이름, 무지개의 색
바뀌지 않을 값들이므로, new 생성자를 사용할 수 없다
예시)
enum enumPractice {
	SUNDAY(10), MONDAY(0), TUESDAY(0), WEDNESDAY(0), THURSDAY(0), FRIDAY(2), SATURDAY(10);
	
	final int like;
    //final을 통해 외부에서 like를 조작하는 것을 방지
    
	enumPractice (int like) {
		this.like = like; 
	}
    //fields를 설정할 수도 있음
    //filds: class 안에 있지만 method 밖에서 정의된 변수
}

public class practice2 {
    public static void main(String[] args) {
    	enumPractice day = enumPractice.FRIDAY;
    	
    	if (day==enumPractice.FRIDAY) {
    		System.out.println("TGIF");
    	}
    	
    	for (enumPractice myDay : enumPractice.values()) {
    		System.out.println(myDay);
    		System.out.println(myDay.like);
    	}
}
}
```

```
Wrapper
기본 타입 데이터를 객체 타입으로 변환
Byte, Short, Integer, Long, Float, Double, Character, Boolean
```



## Python

https://wikidocs.net/16068

### Iterator

iterable한 객체: list, dict, set, str, tuple, range, bytes 
iterator는 Iterable한 객체를 내장함수 또는 iterable 객체의 메소드로 객체를 생성할 수 있음

```python
#파이썬 내장함수 iter()를 사용해 iterator 객체 생성
a = [1, 2, 3]
a_iter = iter(a)
#type(a_iter)  -> <class 'list_iterator'>

print(next(a_iter))
#1
print(next(a_iter))
#2
print(next(a_iter))
#3
print(next(a_iter))
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#StopIteration

#iterable 객체가 가진 매직메소드 __iter__ 이용해 iterator 생성
b = {1, 2, 3}
b_iter = b.__iter__()
#type(b_iter) -> <class 'set_iterator'>'''
```



### Generator

iterator를 생성해주는 함수, 함수 안에 yield 사용

```python
>>> def test_generator():
...  yield 1
...  yield 2
...  yield 3
...
>>> gen = test_generator()
>>> type(gen)
<class 'generator'>
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
3
>>> next(gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

>>> import collections.abc
>>> isinstance(gen, collections.Iterable)
True
>>> for i in test_generator():
...  print(i)
...
1
2
3
>>>
```



