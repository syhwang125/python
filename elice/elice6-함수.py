# 갯수가 정해지지 않은 인자를 받아서 출력하는 함수 `func1`을 선언해보세요. 인자 이름은 원하는대로 정해주시면 됩니다.
def func1(*c):
    print(c)
    
# 전역(global)변수 `param`에 `50`을 저장하는 함수 `func3()`를 선언하세요.
param = 10
def func3():
    global param     ##global 선언 중요 
    param = 50

func3()
print(param)

# x, y, z 세개의 인수를 받아 z, y, x를 리턴하는 함수 reverse(x, y, z)를 선언해보세요.
def reverse(x, y, z):
    o = x
    x = z
    z = o
    return x, y, z

# 아래 부분은 수정할 필요 없습니다. 어떤 결과가 나올지 코드를 보면서 상상해보세요.
ret = reverse(1, 2, 3)
print(ret)  # (3, 2, 1) 출력

r1, r2, r3 = reverse('a', 'b', 'c')
print(r1)   # 'c' 출력
print(r2)   # 'b' 출력
print(r3)   # 'a' 출력