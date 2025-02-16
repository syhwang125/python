## 파이썬 유용한 내장함수 
# 1. 실행버튼을 클릭한 후 터미널에 '안녕하세요 파이썬'을 입력해보세요.
#k = input('<값>을 입력하세요: ')
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
#print('당신이 입력한 값은 <' + k + '>입니다.')

# 실습에 사용될 변수를 선언합니다. 수정하지 마세요.
numdata = 57
strdata = '파이썬'
listdata = [1, 2, 3]
dictdata = {'a':1, 'b':2}

# 실습에 사용될 함수를 선언합니다. 수정하지 마세요.
def func():
    print('안녕하세요.')

# 1. numdata의 자료형을 확인 및 출력하세요.
print(type(numdata))

# 2. strdata의 자료형을 확인 및 출력하세요.
print(type(strdata))

# 3. listdata의 자료형을 확인 및 출력하세요.
print(type(listdata))

# 4. dictdata의 자료형을 확인 및 출력하세요.
print(type(dictdata))

# 5. func의 자료형을 출력하세요.
print(type(func))

#### 몫과 나머지 계산 (divmod)

# 실습에 사용될 변수를 선언합니다. 수정하지 마세요.
a = 11113
b = 23

# 실습에 사용될 변수를 선언합니다. 수정하지 마세요.
m = 12400
h = 60

# 1. a를 b로 나누었을 때의 몫과 나머지 값을 각각 ret1, ret2에 저장하세요.
ret1, ret2 = divmod(a, b)

# 2. m을 h로 나누었을 때의 몫과 나머지 값을 각각 ret3, ret4에 저장하세요.
ret3, ret4 = divmod(m, h)

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print('<%d/%d>는 몫이 <%d>, 나머지가 <%d>입니다.' %(a, b, ret1, ret2))
print('<%d>분은 <%d시간 %d분>으로 변환할 수 있습니다.' %(m, ret3, ret4))

### 10진수 -> 16진수 변환 
# 1. 97을 16진수로 변환한 후 h1에 저장하세요.
h1 = hex(97)

# 2. 98을 16진수로 변환한 후 h2에 저장하세요.
h2 = hex(98)

# 3. h1에 저장된 값을 10진수로 변환한 후 a에 저장하세요.
a = int(h1, 16)

# 4. h2에 저장된 값을 10진수로 변환한 후 b에 저장하세요.
b = int(h2, 16)

# 5. a와 b를 더한 값을 16진수로 변환한 후 ret에 저장하세요.
ret = hex(a+b)

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(h1)
print(h2)
print(a)
print(b)
print(ret)

### 10진수 - 2진수 변환 
# 1. 97을 2진수로 변환한 후 b1에 저장하세요.
b1 = bin(97)

# 2. 98을 2진수로 변환한 후 b2에 저장하세요.
b2 = bin(98)

# 3. b1에 저장된 값을 10진수로 변환한 후 a에 저장하세요.
a = int(b1, 2)

# 4. b2에 저장된 값을 10진수로 변환한 후 b에 저장하세요.
b = int(b2, 2)

# 5. a와 b를 더한 값을 2진수로 변환한 후 ret에 저장하세요.
ret = bin(a+b)

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(b1)
print(b2)
print(a)
print(b)
print(ret)

###  절대값 
# 1. 정수 -3의 절대값을 abs1에 저장하세요.
abs1 = abs(-3)

# 2. 실수 -5.72의 절대값을 abs2에 저장하세요.
abs2 = abs(-5.72)

# 3. 복소수 3+4j의 절대값을 abs3에 저장하세요.
abs3 = abs(3+4j)

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(abs1)
print(abs2)
print(abs3)

### 반올림수 
### round() 는 두개의 숫자를 인자로 받음 
### 첫번째 인자는 반올림할 값
### 두번째 인자는 반올림 자리수 : 1,2,3일때는 각각 소수점 둘째, 셋쨰, 넷째자리 반올림
### -1, -2 이면 1의 자리, 10의 자리에서 반올림 
# 1. 정수 1118을 소수점 첫째자리에서 반올림한 값을 ret1에 저장하세요.
ret1 = round(1118, 0)

# 2. 실수 16.554를 소수점 첫째자리에서 반올림한 값을 ret2에 저장하세요.
ret2 = round(16.554, 0)

# 3. 정수 1118를 1의자리에서 반올림한 값을 ret3에 저장하세요.
ret3 = round(1118, -1)

# 4. 실수 16.554를 소수점 셋째자리에서 반올림한 값을 ret4에 저장하세요.
ret4 = round(16.554, 2)

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(ret1)
print(ret2)
print(ret3)
print(ret4)

### 실수형-정수형 자료 변환
## int() 실수형 자료를 정수형 자료를 변환
# 1. -5.4를 정수형 자료로 변환한 값을 idata1에 저장하세요.
idata1 = int(-5.4)

# 2. 1.78e1을 정수형 자료로 변환한 값을 idata2에 저장하세요.
idata2 = int(1.78e1)

# 3. 171.56을 정수형 자료로 변환한 값을 idata3에 저장하세요.
idata3 = int(171.56)

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(idata1)
print(idata2)
print(idata3)

### 정수형-실수형 자료변환
# 1. 10을 실수형 자료로 변환한 값을 변수 fdata에 저장하세요.
fdata = float(10)

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(fdata)


###  최대값, 최소값 
# 실습에 사용될 변수를 선언합니다. 수정하지 마세요.
listdata = [9.96, 1.27, 5.07, 6.45, 8.38, 9.29, 4.93, 7.73, 3.71, 0.93]
txt = 'Alotofthingsoccureachday'

# 1. listdata의 최대값을 maxlist에 저장하세요.
maxlist = max(listdata)

# 2. listdata의 최소값을 minlist에 저장하세요.
minlist = min(listdata)

# 3. txt의 최대값을 maxtxt에 저장하세요.
maxtxt = max(txt)

# 4. txt의 최소값을 mintxt에 저장하세요.
mintxt = min(txt)

# 5. 2+3, 2*3, 2**3, 3**2 중 최대값을 maxval에 저장하세요.
maxval = max(2+3, 2*3, 2**3, 3**2)

# 6. 'abz', 'a12'의 최소값을 minval에 저장하세요.
minval = min('abz', 'a12')

# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(maxlist)
print(minlist)
print(maxtxt)
print(mintxt)
print(maxval)
print(minval)


