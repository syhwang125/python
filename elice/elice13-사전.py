### ㅅㅏ전에 요소 추가하기 
## 사전은 키:값으로 구성된 자료형. {} 사용 
### dic_data = {'key':'val','key2':'val2}   dic_data[k1]=val1
print('---------사전에 요소 추가하기  -----------')
# 실습에 사용할 변수를 선언합니다.
solardict = {}
# 1. solardict에 키가 '태양', 값이 'Sun'인 요소를 추가하세요.
solardict['태양'] = 'Sun'
# 2. solardict에 키가 '지구', 값이 'Earth'인 요소를 추가하세요.
solardict['지구'] = 'Earth'
# 3. solardict에 키가 '달', 값이 'Moon'인 요소를 추가하세요.
solardict['달'] = 'Moon'
# 4. 사전, for, enumerate를 이용한 아래 코드를 주석을 읽으며 이해해보세요.
# 영어 단어로 구성된 english 리스트 선언합니다.
english = ['abandon', 'ablaze', 'abnormality', 'abolish']
# 영어 단어 뜻으로 구성된 korean 리스트를 선언합니다.
korean = ['버리다', '불타는', '변칙', '폐지하다']
# 비어있는 vocab 사전을 선언합니다.
vocab = {}
# english 리스트의 인덱스와 요소를 각각 i와 k에 순서대로 저장합니다. 
for i, k in enumerate(english):
    # korean 리스트의 요소값을 val 변수에 순서대로 저장합니다. (val = '버리다')
    print(i)   # 0
    print(k)   # abandon 
    val = korean[i]
    print(korean[i])    # 버리다 
    # vocab 사전에 english 리스트의 요소를 키로, korean 리스트의 요소를 값으로 추가합니다.
    vocab[k] = val

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(solardict)   #{'태양': 'Sun', '지구': 'Earth', '달': 'Moon'}
print(vocab)       #{'abandon': '버리다', 'ablaze': '불타는', 'abnormality': '변칙', 'abolish': '폐지하다'}

print('---------사전의 특정 요소를 모두 추출 제거하기 -----------')
### 사전의 특정 요소 제거하기 
#1. names의 요소 중 'Sams':2111를 삭제하세요.
solardict = {'태양':'Sun', '지구':'Earth', '달':'Moon'}
del solardict['달']

print('---------사전 모든 요소 제거하기 -----------')
### 사전의 모든 요소 제거하기 
# 2. solardict의 모든 요소를 제거하여 빈 사전으로 만드세요.
solardict.clear()

print('---------사전에서 키만 추출하기 -----------')
### 사전에서 키만 추출하기 
# keys() 를 이용하면 사전에서 모든 키를 추출할 수 있음
# list() 리스트의 형태로 변형하고 싶을 경우 사용 
# 실습에 사용할 변수를 선언합니다.
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
# 1. names의 모든 키를 추출하여 변수 ks1에 저장하세요.
ks1 = names.keys()
# 2. ks1에 객체형으로 저장된 names의 모든 키를 리스트형으로 변경한 후 변수 key_list1에 저장하세요.
key_list1 = list(ks1)
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('names의 모든 키를 객체형으로 추출합니다:\n>>>', ks1)
print('names의 모든 키를 리스트에 담습니다:\n>>>', key_list1)

print('---------사전의 값만 추출하기 -----------')
### 사전에서 값만 추출하기 
### 사전에서 모든 값을 추출할때 values() 
# 실습에 사용할 변수를 선언합니다.
#names2 = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
# 1. names의 모든 값을 추출하여 변수 vals1에 저장하세요.
vals2 = names.values()
# 2. vals1에 객체형으로 저장된 names의 모든 값을 리스트형으로 변경한 후 변수 val_list1에 저장하세요.
val_list2 = list(vals2)
print(val_list2)

print('---------사전 요소를 모두 추출하기 -----------')
### 사전 요소를 모두 추출하기 
# items() 는 사전에서 모든 요소를 추출할 수 있다. 
# 실습에 사용할 변수를 선언합니다.
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
solardict = {'태양':'Sun', '지구':'Earth', '달':'Moon'}
# 1. names의 모든 요소를 추출하여 변수 items1에 저장하세요.
items1 = names.items()
# 2. items1에 객체형으로 저장된 names의 모든 요소를 리스트형으로 변경한 후 변수 item_list1에 저장하세요.
item_list1 = list(items1)
# 3. solardict의 모든 요소를 추출하여 변수 items2에 저장하세요.
items2 = solardict.items()
# 4. items2에 객체형으로 저장된 solardict의 모든 요소를 리스트형으로 변경한 후 변수 item_list2에 저장하세요.
item_list2 = list(items2)
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('names의 모든 요소를 객체형으로 추출합니다:\n>>>', items1)
print('names의 모든 요소를 리스트에 담습니다:\n>>>', item_list1)
print('solardict의 모든 요소를 객체형으로 추출합니다:\n>>>', items2)
print('solardict의 모든 요소를 리스트에 담습니다:\n>>>', item_list2)

### 사전 정렬하기 
# sorted() 사전을 인자료 입력받아 정렬 
# sorted() 는 기본적으로 사전의 키를 오름차순으로 정렬한 결과를 리스트로 리턴
# reverse=True 를 두번째 인자로 입력하면 내림차순으로 정렬한 결과 
# 실습에 사용할 변수를 선언합니다.
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}

# 1. names의 키를 오름차순으로 정렬한 값을 ret1에 저장하세요. 
ret1 = sorted(names)
# 2. names의 키를 내림차순으로 정렬한 값을 ret2에 저장하세요. 
ret2 = sorted(names, reverse=True)
# 3. names의 값을 오름차순으로 정렬한 값을 ret3에 저장하세요.
ret3 = sorted(names.values())
# 4. names의 모든 요소를 오름차순으로 정렬한 값을 ret4에 저장하세요.
ret4 = sorted(names.items())
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret1)
print(ret2)
print(ret3)
print(ret4) 