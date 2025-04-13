### 14. 응용편
# 이름없는 한줄짜리 함수 만들기 
# lambda 인자, 인자, .... : 실행코드 
# func2 = lambda name, age: '이름: %s \n나이: %d' %(name, age)
print('-------- 이름없는 한줄짜리 함수 만들기 lambda --------- ')
# 1. x와 y를 인자로 받아 합을 출력하는 lambda 함수를 정의하고 add에 저장하세요.
add = lambda x, y : x+y
# 2. add를 이용해 1과 3의 합을 출력하세요. 
print(add(1,3))

print('-------- 인자를 바꾸어 함수를 반복 호출하여 결과값 얻기 --------- ')
## map(f, A)와 같이 map()의 첫번째 인자로 함수를, 
## 두번째 인자로 f에 대입할 집합을 입력하면, 
## A의 모든 요소를 f에 대입한 결과를 얻을 수 있습니다.

# 실습에 사용할 변수를 선언합니다.
args = [1, 2, 3, 4, 5]
# 1. x를 인자로 받아 x의 제곱 x*x를 리턴하는 lambda 함수를 f에 저장하세요.
f = lambda x : x*x
### 2. args의 모든 요소를 f에 대입하여 결과를 얻은 후 ret1에 저장하세요.
ret1 = map(f, args)
# 3. ret1에 저장된 객체를 리스트 형태로 변환하세요.
ret2 = list(ret1)
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret2)

print('-------- 텍스트 파일을 읽고 출력하기  --------- ')
### 텍스트 읽기모드로 파일을 열기 open() -> r,w 모드 read() -> close() 
# 1. open()을 이용해 stockcode.txt 텍스트 파일을 읽기 모드로 열고, 파일 객체를 f에 저장하세요.
f = open('stockcode.txt', 'r')
# 2. read()를 이용해 stockcode.txt 파일의 모든 내용을 읽고 data의 저장하세요. 
data = f.read()
# 3. data에 저장된 stockcode.txt 파일의 모든 내용을 출력하세요.
print(data)
# 4. close()를 이용해 stockcode.txt 파일을 닫으세요. 
f.close()

print('-------- 텍스트 파일을 한줄씩 읽고 출력하기  --------- ')
# 실습에 사용할 변수를 선언합니다.
line_num = 1
# 1. open()을 이용해 stockcode.txt 텍스트 파일을 읽기모드로 열고, 파일 객체를 f에 저장하세요.
f = open('stockcode.txt', 'r')
# 2. readline()을 이용해 stockcode.txt 파일 내용의 한 줄을 읽고 line에 저장하세요.
line = f.readline()
# 3. 실행 버튼을 누르고 주석과 함께 코드를 이해해보세요.
# line_num이 6보다 작을 동안 코드블럭을 실행합니다.
while line_num < 6:
    # line_num과 stockcode.txt 파일 내용의 한 줄을 같이 출력합니다.
    print('%d | %s' %(line_num, line), end='')
    # stockcode.txt 파일 내용의 다음 줄을 읽고 line에 저장합니다.
    line = f.readline()
    # line_num에 1을 더합니다.
    line_num += 1
# 파일을 닫습니다.
f.close()

print('-------- 텍스트 파일을 한줄씩 읽고 출력하기  --------- ')
# 1. open()을 이용해 stockcode.txt 텍스트 파일을 읽기모드로 열고, 파일 객체를 f에 저장하세요.
f = open('stockcode.txt','r')
# 2. readlines()을 이용해 stockcode.txt 파일의 내용을 원소로 갖고 있는 리스트를 lines에 저장하세요. 
lines = f.readlines()
# 3. 실행 버튼을 누르고 주석과 함께 코드를 이해해보세요.
# lines의 인덱스와 요소를 각각 line_num과 line에 순서대로 저장합니다.
for line_num, line in enumerate(lines):
    # 첫번째 반복문에서는 인덱스 0과 000020 동화약품 \n이 line에 저장됩니다.
    print('%d %s' %(line_num+1, line), end='')
# 파일을 닫습니다.
f.close()

print('-------- 파일을 열고 자동으로 닫기   --------- ')
### 파일을 다룰떄는 open(), close() 
## with open() as 를 사용하면 파일에 대한 처리가 끝나면 자동으로 파일을 닫을 수 있음 
# 1. with open() as를 이용해 stockcode.txt 텍스트 파일을 읽기모드로 열고, 파일 객체를 f에 저장하세요.
with open('stockcode.txt', 'r') as f: 
# 실습 결과를 출력하는 코드입니다. 수정하지 마세요. 
    for line_num, line in enumerate(f.readlines()):
        print('%d %s' %(line_num+1, line), end='')

print('-------- 파일의 특정 부분만 읽기   --------- ')
### seek() 는 파일의 특정부분으로 파일을 읽는 위치를 이동시키고 해당 위치부터 일정크기만큼 읽을 수 있음 
### read() 인자로 정수를 입력하면 읽을 크기를 지정할 수 있음 
# 1. stockcode.txt를 읽기 모드로 열고 f에 저장합니다.
f = open('stockcode.txt', 'r')
# 2. stockcode.txt의 105 바이트 위치부터 파일을 읽기 시작하세요.
f.seek(105)
# 3. 500 바이트 만큼 파일을 읽고 그 내용을 data에 저장하세요.
data = f.read(500)
# 4. 파일을 닫으세요.
f.close()
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(data)

print('-------- 현재 시간 출력하기   --------- ')
### localtime()은 현재 서버 시간을 time.struct_time 형식의 데이터로 리턴함
### localtime()의 리턴값을 변수에 저장하고 인덱싱을 사용히먄 햔제 날짜, 시간등을 접근할 수 있음
# 인덱스0: tm_year (현재 년도)
# 인덱스1: tm_mon (현재 월)
# 인덱스2: tm_mday (현재 날짜)
# 인덱스3: tm_hour (현재 시간)
# 인덱스4: tm_min (현재 분)
# 인덱스5: tm_sec (현재 초)
# 인덱스6: tm_wday (현재 요일)
# 인덱스7: tm_yday (1월 1일부터 현재까지 날짜수)
# 인덱스8: tm_isdst (섬머타임 적용 여부)

# 1. time 모듈에서 localtime() 함수를 임포트하세요.
from time  import localtime
# 2. localtime()을 이용해 time.struct_time 형식의 현재시간을 user_time에 저장하세요.
user_time = localtime()
# 3. user_time의 인덱스3 값을 hour에 저장하세요.
hour = user_time[3]
# 4. user_time의 인덱스4 값을 minute에 저장하세요.
minute = user_time[4]
# 5. user_time의 인덱스5 값을 sec에 저장하세요.
sec = user_time[5]
# 아래는 출력을 위한 코드입니다. 수정하지 마세요..
print('이 코드는 <%d시 %d분 %d초>에 실행되었습니다 (UTC+09:00).' %(hour+9, minute, sec))

print('-------- 프로그램 실행시간 계산하기    --------- ')
## datetime 객체의 now() 함수는 현재 시간의 1/10,000,000 초단위까지 처리
# 1. datetime 모듈에서 datetime 객체를 임포트하세요.
from datetime import datetime
# 2. 현재 시간을 측정하여 start에 저장하세요.
start = datetime.now()
# 아래는 실습에 사용되는 코드입니다. 수정하지 마세요.
ret = 0
for i in range(100000):
    ret += i
# 3. 현재 시간을 다시 측정하여 end에 저장하세요.
end = datetime.now()
# 4. start와 end에 저장된 두 시간의 차이를 계산하고 elapsed에 저장하세요.
elapsed = end - start
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('1에서 100000까지 더한 결과: %d' %ret)
print('총 계산 시간:', elapsed)

print('-------- 주어진 숫자를 천단위로 구분하기     --------- ')
#input() - 사용자 입력받기
#if~else - if문 개념 배우기
#isdigit() - 문자열이 숫자인지 검사하기
#[::-1] - 리스트 요소 순서를 역순으로 만들기
#for - for문 개념 배우기
#enumerate() - 리스트의 모든 요소를 인덱스와 쌍으로 추출하기
#len() - 시퀀스 자료 크기 이해하기

# 사용자로부터 숫자를 입력받아 변수 num에 저장합니다.
num = input('아무 숫자를 입력하세요: ')
# 사용자가 입력한 문자열이 숫자로만 구성되어 있는지 확인합니다.
if num.isdigit():
    # 숫자로만 구성된 문자열이면 사용자가 입력한 숫자를 거꾸로 배열하여 변수 num에 재지정 합니다.
    num = num[::-1]
    # 결과를 담을 변수 ret을 선언합니다.
    ret = ''
    # num에서 인덱스와 요소를 하나씩 추출합니다.
    for i, c in enumerate(num):
        # 인덱스i에 1을 더하여 추출한 숫자의 위치에 대응합니다.
        i += 1
        # 요소의 위치가 num의 마지막이 아니고 3의 배수이면 추출한 요소 뒤에 쉼표를 더한 값을 ret에 추가합니다.
        if i != len(num) and i%3 == 0:
            ret += (c + ',')
        # 추출한 요소가 마지막에 위치하거나 3의 배수가 아니면 추출한 요소를 ret에 추가합니다. 
        else:
            ret += c
    # ret을 거꾸로 배열합니다.
    ret = ret[::-1]
    print(ret)
# 사용자가 입력한 문자열이 숫자로만 이루어져 있지 않으면 입력한 내용이 숫자가 아니라는 메시지를 출력합니다. 
else:
    print('입력한 [%s]은 숫자가 아닙니다.' %num)

print('-------- URL 에서 호스트 도메인 추출하기     --------- ')
# 실습에 사용할 변수를 선언합니다.
url = 'https://academy.elice.io/courses/112/lectures/1331/materials/9'
# 1. url에 저장된 문자열을 '/'로 구분한 결과를 tmp에 저장하세요.
tmp = url.split('/')
# 2. tmp에 저장된 리스트에서 인덱스2에 해당하는 요소를 domain에 저장하세요.
domain = tmp[2]
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('URL을 /로 구분한 결과: ', tmp)
print('호스트 도메인: ', domain)

print('-------- 스택 구현하기    --------- ')
# 1. 원소를 갖고 있지 않은 빈 리스트를 생성하여 mystack에 저장하세요.
mystack = []
# data를 mystack에 요소로 추가하는 putdata 함수를 정의합니다.
def putdata(data):
    # 2. 전역변수 mystack에 접근하세요.
    global mystack
    # 3. mystack 리스트에 putdata 함수의 인자인 data를 맨 마지막 요소로 추가하세요.
    mystack.append(data)

# 요소를 mystack으로부터 하나 추출하는 함수 popdata를 정의합니다.
def popdata():
    # 전역변수 mystack에 접근합니다.
    global mystack
    # mystack의 크기가 0이면, 즉 추출할 데이터가 없으면 None을 리턴합니다. 
    if len(mystack) == 0:
        return None
    # mystack에 데이터가 있으면 mystack.pop()을 리턴합니다.
    return mystack.pop()

# 위에서 정의한 putdata를 이용해 문자열, 리스트, 숫자를 mystack에 추가해봅니다.
putdata('데이터1')
putdata([3, 4, 5, 6])
putdata(12345)

# mystack에 저장된 원소를 확인하기 위해 출력해봅니다.
print('<스택상태>: ', end=''); print(mystack)

# popdata()를 호출하여 mystack에서 데이터를 하나 추출하여 ret에 저장합니다.
ret = popdata()
# ret이 None일 때까지 popdata()를 호출하여 mystack으로부터 원소를 하나씩 추출합니다.
while ret != None:
    # mystack에서 추출된 원소를 출력합니다.
    print('스택에서 데이터 추출된 원소: ', end=''); print(ret)
    # mystack에서 원소가 추출된 후 mystack에 저장된 원소를 출력합니다.
    print('<스택상태>: ', end=''); print(mystack)
    ret = popdata()

print('-------- 문장에 나타나는 문자 빈도수 계산하기     --------- ')
## def - 함수 이해하기
# with~as - 파일을 열고 자동으로 닫기
# read - 텍스트 파일을 읽고 출력하기
# for - for문 개념 배우기
# if~else - if문 개념 배우기
# sorted - 사전 정렬하기
# lambda - 이름없는 한줄짜리 함수 만들기

# 1. filename을 인자로 받는 getTextFreq 함수를 정의하세요.
def getTextFreq(filename):
    # 2. with open() as를 이용해 인자로 받은 filname을 읽기모드로 열고 파일 객체를 f에 저장하세요.
    with open(filename,'r') as f: 
        # 3. read()를 이용해 인자로 받은 filename 파일의 모든 내용을 읽고 text에 저장하세요.
        text = f.read()
        # 4. 원소를 갖고 있지 않은 빈 사전을 생성하여 fa에 저장하세요.
        fa = {}
        # text의 모든 문자를 추출하고 그 문자가 fa의 키로 존재하면 해당 값을 1 증가합니다. 
        for c in text:
            if c in fa:
                fa[c] += 1
            # text에서 추출한 문자가 fa의 키로 존재하지 않으면 fa에 새로운 요소로 추가합니다.
            else:
                fa[c] = 1
    return fa

# python.txt를 인자로 하여 getTextFreq가 리턴한 사전을 ret에 저장합니다. 
ret = getTextFreq('python.txt')
# ret을 내림차순으로 정렬하여 ret에 다시 저장합니다. 
ret = sorted(ret.items(), key=lambda x:x[1], reverse=True)
# (문자, 빈도수)가 요소로 구성된 리스트 형식의 ret을 화면에 보기 좋게 출력합니다.
for c, freq in ret:
    # 문자가 '\n'이면 줄바꿈 기호이므로 화면에 출력하지 않고 넘어갑니다.
    if c == '\n':
        continue
    print('[%c] -> [%d]회' %(c, freq))

print('-------- 텍스트 파일에 있는 단어 개수 계산하기     --------- ')
# with~as - 파일을 열고 자동으로 닫기
# read - 텍스트 파일을 읽고 출력하기
# split() - 문자열을 특정 문자로 분리하기
# 1. with open() as를 이용해 python.txt를 읽기모드로 열고 파일 객체를 f에 저장하세요.
with open('python.txt','r') as f:
    # 2. read()를 이용해 인자로 받은 python.txt의 모든 내용을 읽고 data에 저장하세요.
    data = f.read()
    # 3. data에 저장된 python.txt 내용을 split()하여 분리하고 tmp에 저장하세요.
    tmp = data.split()
    # tmp의 크기, 즉 요소 및 단어의 개수를 출력합니다.
    print('단어수: [%d]' %len(tmp))


print('-------- 파일에서 특정 단어 개수 계산하기    --------- ')
# def - 함수 이해하기
#with~as - 파일을 열고 자동으로 닫기
##read - 텍스트 파일을 읽고 출력하기
#while - while문 개념 배우기
#lower() - 문자열 대소문자 변환하기

# 1. filename과 word를 인자로 받는 countWord 함수를 정의하세요.
def countWord(filename, word):
    # 2. with open() as를 이용해 인자로 받은 filname을 읽기모드로 열고 파일 객체를 f에 저장하세요.
    with open(filename, 'r') as f:
        # 3. read()를 이용해 인자로 받은 filename 파일의 모든 내용을 읽고 text에 저장하세요.
        text = f.read()
        # 4. text에 저장된 모든 문자를 소문자로 변경한 후 text에 다시 저장하세요.
        text = text.lower()
        # text에서 word가 최초로 나타나는 위치를 구하여 pos에 저장합니다.
        pos = text.find(word)
        # 단어의 개수를 담을 변수 count를 선언합니다.
        count = 0
        # find()는 찾고자 하는 문자열이 없을 경우 -1을 리턴합니다. 해당 단어를 찾지 못할 때까지 반복합니다. 
        while pos != -1:
            # 문자열이 존재할 경우 count를 1 증가합니다.
            count += 1
            # word의 위치 다음부터 다시 text에서 word를 찾습니다.
            pos = text.find(word, pos+1)
    return count

word = 'python'
# python.txt에서 'python'이 등장하는 빈도수를 ret에 저장합니다.
ret = countWord('python.txt', word)
# ret에 저장된 python의 빈도수를 출력합니다.
print('[%s]의 개수: %d' %(word, ret))