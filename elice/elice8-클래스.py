# MyClass를 선업합니다.
class MyClass():
    # MyClass의 클래스 멤버에 '안녕하세요'를 저장합니다.
    var = '안녕하세요'
    # 클래스 멤버인 var를 출력하는 MyClass의 클래스 메소드 선언합니다.
    def sayHello(self):
        print(self.var)

# MyClass 객체를 생성합니다.
obj = MyClass()
# '안녕하세요'를 출력합니다.
print(obj.var)
# '안녕하세요' 출력합니다.
obj.sayHello()

#클래스 멤버와 인스턴스 멤버 이해하기
#클래스 멤버: 객체간 서로 공유되는 변수
#인스턴스 멤버: 객체별로 고유한 값을 저장하는 변수
#인스턴스 멤버는 self.멤버이름을 통해 선언할 수 있습니다. (특정 객체의 멤버 이기때문에 self.멤버이름의 형식으로 선언하는것 입니다.)
class KiaK3:
    brand = '기아'  #클래스 멤버
    model = 'K3'    #클래스 멤버
    def owner(self, name):
        self.name = name  #인스턴스 멤버

# MyClass 선언
class MyClass:
    var = '안녕하세요!'
    def sayHello(self):
        param1 = '안녕'
        # self를 이용해 아래 인스턴스 멤버 param2를 선언하고 '하이'를 저장해주세요.
        self.param2 = '하이'
        print(param1)
        print(self.var)

obj = MyClass()
obj.sayHello()

# 객체 `obj`의 인스턴스 멤버 `param2`를 출력해보세요.
print(obj.param2)        

# MyClass 선언
class MyClass:
    # '안녕하세요'를 출력하는 클래스 메소드 `sayHello`를 선언하세요.
    def sayHello(self):
        print('안녕하세요')

    # name을 입력받아 print('%s! 다음에 보자' %name)을 실행하는 클래스 메소드 `sayBye`를 선언하세요.
    def sayBye(self, name):
        self.name = name
        print('%s! 다음에 보자' %name)

## 아래는 출력을 위한 코드 입니다. 수정하실 필요 없습니다.
obj = MyClass()
obj.sayHello()      #'안녕하세요' 출력
obj.sayBye('철수')   #'철수! 다음에 보자' 출력

## 클래스  생성자  
class MyClass:
    #1 txt를 인자로 받는 생성자를 정의해 주세요.
    def __init__(self, txt):     // 생성자 
        #2 var라는 인스턴스 멤버를 선언하고, 인자로 받은 `txt` 값을 넣어주세요.
        self.var = txt
        #3 'MyClass 인스턴스 객체가 생성되었습니다.'라는 문구를 출력하세요.
        print('MyClass 인스턴스 객체가 생성되었습니다.')

# 실습 결과를 출력하기 위한 코드입니다. 수정하지 마세요.
obj = MyClass('안녕하세요')    # 'MyClass 인스턴스 객체가 생성되었습니다'가 출력됩니다.
print(obj.var)    # '안녕하세요'가 출력됩니다.

## 클래스 소멸자 
class MyClass:
    #1 3번째 줄에 소멸자를 정의해보세요.
    def __del__(self):
        #2 `MyClass 인스턴스 객체가 메모리에서 제거됩니다.`라는 문구가 출력되도록 하세요. 
        print('MyClass 인스턴스 객체가 메모리에서 제거됩니다.')

## 아래는 출력을 위한 코드 입니다. 수정하실 필요 없습니다.
obj = MyClass()    # MyClass 인스턴스 객체를 생성하고 obj로 지정합니다.
del obj    #'MyClass 인스턴스 객체가 메모리에서 제거됩니다'가 출력됨


### 클래스 상속 ####
# class Subclass(SuperClass):
#자식클래스는 여러 개의 부모클래스로부터 상속받을 수 있습니다.
#만약 자식클래스와 부모클래스의 멤버 또는 메소드가 중복된다면, 자식클래스의 요소를 우선시 합니다.

#1 Add 클래스에서 두 개의 수를 받아 덧셈을 하는 add 함수를 구현해주세요.
class Add: 
    def add(self, n1, n2):
        return n1 + n2

#2 Calculator 클래스가 Add 클래스를 상속받도록 하세요.
class Calculator(Add):
    def sub(self, n1, n2):
        return n1 - n2

obj = Calculator()
print(obj.sub(1,2))
#3 obj 객체를 사용하여, 정수 1과 2를 더하는 연산을 해보세요. 
print(obj.add(1,2))