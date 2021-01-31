### 11. 문자열 
### 문자열에서 특정 위치의 문자 
# 실습에 사용할 변수를 선언합니다. 수정하지 마세요.
txt1 = 'A tale that was not right'
txt2 = '이 또한 지나가리라.'
# 1. txt1의 인덱스5에 해당하는 문자 'e'를 출력하세요. 
print(txt1[5])
# 2. txt2의 끝에서 2번째 문자 '라'를 출력하세요. 반드시 음수 값을 입력해주세요.
print(txt2[-2])

# 실습에 사용할 변수를 선언합니다. 수정하지 마세요.
txt1 = 'A tale that was not right'
txt2 = '이 또한 지나가리라.'
# 1. txt1에서 'ale'을 출력하세요.
print(txt1[3:6])
# 2. txt1에서 'A tale'을 출력하세요.
print(txt1[0:6])
# 3. txt2에서 '가리라.'를 출력하세요.
print(txt2[7:11]) 

### 문자열에서 짝수 인덱스 추출하기 (변수명[시작 인덱스:끝 인덱스:스텝]) 
# 실습에 사용할 변수를 선언합니다. 수정하지 마세요.
txt = 'aAbBcCdDeEfFgGhHiIjJkK'
# 1. txt의 짝수 인덱스에 해당하는 문자만 추출하세요.
ret1 = txt[::2]
# 2. txt의 홀수 인덱스에 해당하는 문자만 추출하세요.
ret2 = txt[1::2]
# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(ret1)
print(ret2)

### 문자열 거꾸로 만들기 
# 실습에 사용할 변수를 선언합니다. 수정하지 마세요.
txt = 'abcdefghijk'
# 1. txt에 저장된 문자열을 거꾸로 만들어 변수 ret에 저장하세요.
ret = txt[::-1]
# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
print(ret)

### 문자열이 알파벳인지 검사하기
##변수명.isalpha()를 작성하여 사용할 수 있습니다. 문자열의 모든 문자가 알파벳 또는 한글로만 구성되어 있으면 True를 리턴하고 아니면 False를 리턴합니다. 공백이 있어도 False가 반환됩니다.
txt3 = 'Warcraft Three'
txt4 = '3PO'
print(txt3.isalpha())   #false
print(txt3.isalpha())   #false

### 문자열이 숫자인지 검사하기 
txt1 = '010-1234-5678'
txt3 = '3피오R2D2'
# 1. txt1이 숫자로 구성되었는지 확인하고 그 결괏값을 변수 ret1에 저장하세요.
print( txt1.isdigit() )
# 1. txt3이 알파벳/한글/숫자로 구성되었는지 확인하고 그 결괏값을 변수 ret1에 저장하세요.
print( txt3.isalnum() )
# 1. txt를 모두 대문자로 변환한 후 변수 ret1에 저장하세요.
txt = 'Python is a widely used High-level Programming Language for general-purpose programming.'
print( txt.upper() )
# 2. txt를 모두 소문자로 변환한 후 변수 ret2에 저장하세요.
print(txt.lower())

txt = '  양쪽에 공백이 있는 문자열입니다.     '
# 1. txt 문자열의 왼쪽 공백을 제거한 후 ret1에 저장하세요.
print('<'+txt.lstrip()+'>')
# 2. txt 문자열의 오른쪽 공백을 제거한 후 ret2에 저장하세요.
print('<'+txt.rstrip()+'>')
# 3. txt 문자열의 왼쪽, 오른쪽 공백을 제거한 후 ret3에 저장하세요.
print('<'+txt.strip()+'>')

### 문자열 수치형 자료로 변환하기 
numstr1 = '3.14'
numstr2 = '125'
# 1. 문자열 numstr1을 실수로 변환한 값을 num1에 저장하세요.
num1 = float(numstr1)
# 2. 문자열 numstr2을 정수로 변환한 값을 num2에 저장하세요.
num2 = int(numstr2)
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(type(num1))    # num1의 자료형을 출력합니다.
print(type(num2))    # num2의 자료형을 출력합니다. 

### 수치형 자료 문자열로 변환하기 
num2 = 3.14
# 2. 수치형 자료 num2를 문자열로 변환한 값을 numstr2에 저장하세요.
numstr2 = str(num2)
print('num2을 문자열로 변환한 값은 "%s"입니다.' %numstr2)

### 문자열에 있는 문자 개수 구하기 
# 실습에 사용할 변수를 선언합니다.
txt = 'A lot of things occur each day, every day.'
# 1. txt 문자열에 'o'의 개수를 확인한 후 word_count1에 저장하세요.
word_count1 = txt.count('o')
# 2. txt 문자열에 'day'의 개수를 확인한 후 word_count2에 저장하세요.
word_count2 = txt.count('day')
# 3. txt 문자열에 공백(' ')의 개수를 확인한 후 word_count3에 저장하세요.
word_count3 = txt.count(' ')
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(word_count1)
print(word_count2)
print(word_count3)

### 특정 문자 위치 찾기 
# 실습에 사용할 변수를 선언합니다.
txt = 'A lot of things occur each day, every day.'
# 1. 'e'가 최초로 나타는 위치의 인덱스를 offset에 저장하세요.
offset1 = txt.find('e')
# 2. 'day'가 최초로 나타는 위치의 인덱스를 offset에 저장하세요.
offset2 = txt.find('day')
# 3. 인덱스 30 이후에 'day'가 최초로 나타는 위치의 인덱스를 offset에 저장하세요.
offset3 = txt.find('day', 30)
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(offset1)
print(offset2)
print(offset3)

### 문자열 분리하기 
# 실습에 사용할 변수를 선언합니다.
fb_url = 'https://www.facebook.com/elice.io'
blog_url = 'https://medium.com/elice'
# 1. 마침표(.)를 기준으로 fb_url에 저장된 문자열을 분리하세요.
ret1 = fb_url.split('.')
# 2. 슬래쉬(/)를 기준으로 blog_url에 저장된 문자열을 분리하세요.
ret2 = blog_url.split('/')
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret1)
print(ret2)

### 문자열 결합하기 
# 실습에 사용할 변수를 선언합니다.
loglist = ['2017/09/01', '10:10:25', '프로그램이 종료']
# 1. loglist의 문자열 멤버들을 하나의 문자열로 결합하세요. 멤버를 연결한 문자를 '-'로 설정하세요.
log = '-'.join(loglist)
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(log)

###  특정문자를 다른 문자로 바꾸기 
txt2 = '매일 많은 일들이 일어납니다.'
# 3. txt2의 문자열 '매일'을 '항상'으로 바꾼 문자열을 ret3에 저장하세요.
ret3 = txt2.replace('매일', '항상')
print(ret3) 


### 문자열 정렬하기 
# 실습에 사용할 변수를 선언합니다.
strdata = 'pneumonoultramicroscopicsilicovolcanoconiosis'

# 1. `strdata`에 저장된 문자열을 오름차순으로 정렬해서 `ret1`에 저장하세요.
ret1 = sorted(strdata)
print(ret1)  #['a', 'a', 'c', 'c', 'c',~~~~~ 
# 2. 리스트 형태의 `ret1`을 문자열로 결합하여 `ret1`에 다시 저장하세요.
ret1 = ''.join(ret1)

# 3. `strdata`에 저장된 문자열을 내림차순으로 정렬하여 `ret2`에 저장하세요.
ret2 = sorted(strdata, reverse=True)

# 4. 리스트 형태의 `ret2`을 문자열로 결합하여 `ret2`에 다시 저장하세요.
ret2 = ''.join(ret2)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('오름차순으로 정렬된 문자열은 <' + ret1 + '>입니다.')
print('내림차순으로 정렬된 문자열은 <' + ret2 + '>입니다.')

### 문자 코드값 구하기 
# 안내문을 띄우고 엘리스 터미널에 입력한 사용자의 입력값을 ch에 저장합니다.
ch = input('문자를 1개를 입력하세요: ')
# try~except문을 실행합니다.
try:
    # 사용자가 입력한 문자의 코드값을 chv에 저장합니다. 
    chv = ord(ch)
    # 사용자가 입력한 문자와 문자의 코드값을 출력합니다.
    print('문자: %s \n코드값: %d' %(ch, chv))
# try 코드블럭에서 오류가 발생할 겨우 except에 해당하는 코드블럭을 실행합니다.
except:
    print('ERROR: ord()의 인자로 숫자 또는 한 개 이상의 문자를 입력할 경우 오류가 발생합니다!!!')

### 코드값에 대응하는 문자 얻기
# random 모듈에서 무작위의 정수를 리턴하는 randint 함수를 호출합니다.
from random import randint

# for문 아래의 6~9코드를 5번 실행합니다.
for i in range(5):
    # 0과 1000 사이의 랜덤한 정수를 randnum에 저장합니다.
    randnum = randint(0, 1000)
    # chr를 이용해 정수에 대응한는 문자를 randchr에 저장합니다.
    randchr = chr(randnum)
    # randnum에 저장된 코드값과 randchr에 저장된 문자를 출력합니다.
    print('코드값 <%d>에 대응하는 문자는 <%s>입니다.' %(randnum, randchr))

### 문자열로 된 식을 실행하기 : eval()을 사용하면 코드로 실행 가능한 문자열을 인자로 받아 결괏값을 리턴
# 실습에 사용할 변수를 선언합니다.
expr1 = '2+3'
expr2 = 'round(3.7)'
# 1. expr1에 저장된 문자열을 파이썬 코드로 실행하고 그 결과를 ret1에 저장하세요.
ret1 = eval(expr1)
# 2. expr2에 저장된 문자열을 파이썬 코드로 실행하고 그 결과를 ret2에 저장하세요.
ret2 = eval(expr2)
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret1)
print(ret2)

