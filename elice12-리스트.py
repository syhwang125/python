### 순차적인 정수 리스트 민들기 
#1. 0~9까지 순차적인 정수를 ret1에 저장하세요.
ret1 = range(0,10)
# 2. ret1에 저장된 0~9까지 순차적인 정수를 리스트 형태로 변환해 ret1_list에 저장하세요.
ret1_list = list(ret1)
print(ret1_list) 

### 리스트에서 특정 위치의 요소 얻기    (12-2)  ????????
# 실습에 활용할 변수를 선언합니다.
listdata = [1, 2, 'a', 'b', 'c', [4, 5, 6]]
enumlist = list(enumerate(listdata))
print(enumlist)

print(listdata.index(2))




### 리스트에서 특정 요소의 위치 구하기 
# index()는 리스트에서 멤버의 값을 알고 있을 때 해당 멤버가 최초로 나타나는 위치의 인덱스를 리턴합니다.
# 실습에 활용할 변수를 선언합니다.
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕석', '해왕성']
earth = '지구'
saturn = '토성'

# 1. earth 변수를 사용해 solarsys 리스트에서 지구의 위치를 구하세요.
pos1 = solarsys.index(earth)
print(pos1)
 # 실습에 활용할 변수를 선언합니다.
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕석', '해왕성']
earth = '지구'
saturn = '토성'

# 1. earth 변수를 사용해 solarsys 리스트에서 지구의 위치를 구하세요.
pos1 = solarsys.index(earth)

# 2. saturn 변수를 사용해 solarsys 리스트에서 토성의 위치를 구하세요. 
pos2 = solarsys.index(saturn)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print('%s은(는) 태양계에서 %d번째에 위치하고 있습니다.' %(earth, pos1))
print('%s은(는) 태양계에서 %d번째에 위치하고 있습니다.' %(saturn, pos2))


### 리스트에서 특정 위치의 요소 변경하기 
# 실습에 활용할 변수를 선언합니다.
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕석', '해왕성']
mars = '화성'
between = '그리고 화성 넘어'

# 1. mars 변수와 index()를 이용해 solarsys 리스트에서 `화성`의 위치를 구하고 `pos`에 저장하세요.
pos = solarsys.index(mars)

# 2. pos에 저장된 '화성'의 인덱스를 이용해 solarsys 리스트에서 '화성'을 between에 저장된 값으로 변경하세요.
solarsys[pos] = between

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(solarsys) 


### 리스트에서 특정 구간에 있는 요소 추출하기 
# 실습에 활용할 변수를 선언합니다.
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
# 1. solarsys의 인덱스1~4에 해당하는 멤버를 슬라이싱하여 만든 새로운 리스트를 rock_planets에 저장하세요.
rock_planets = solarsys[1:5]
# 2. solarsys의 인덱스5에 해당하는 멤버부터 끝까지 슬라이싱하여 만든 새로운 리스트를 gas_planets에 저장하세요.
gas_planets = solarsys[5::]
# 3. solarsys에서 `태양`을 제외하고 짝수 인덱스에 해당하는 멤버(수성, 지구, 목성, 천왕성)를 모두 슬라이싱하여 만든 새로운 리스트를 even_planets에 저장하세요. 
even_planets = solarsys[1::2]
print('태양계의 암석형 행성: ', end = ''); print(rock_planets)
print('태양계의 가스형 행성: ', end = ''); print(gas_planets)
print('태양계의 짝수번째 행성: ', end = ''); print(even_planets)

### 리스트 요소 순서를 역순으로 만들기 
# 실습에 사용할 변수를 선언합니다.
listdata1 = list(range(1,6))
listdata2 = list(range(10,16))

# 1. reverse()를 이용해 listdata1의 모든 요소 순서를 거꾸로 만드세요. 새로운 변수를 만들지 않고 원본 리스트를 변경하세요.
listdata1.reverse()      ##### 

# 2. [::-1]를 이용해 listdata2의 모든 요소 순서를 거꾸로 만들고 ret에 저장하세요.
ret = listdata2[::-1]

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(listdata1)
print(ret) 

### 리스트에 요소 추가하기 
solarsys = ['수성', '금성', '지구', '화성', '목성', '토성']
solarsys.append('천왕성')

### 리스트의 특정 위치에 요소 삽입하기 
# 실습에 사용할 변수를 선언합니다.
solarsys = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
# 1.index()를 이용해 solarsys에서 '화성'의 인덱스 값을 pos1에 저장하세요.
pos1 = solarsys.index('화성')
# 2. solarsys에 '지구'와 '화성' 사이에 새로운 요소로 '달'을 삽입하세요. 
# pos1에 저장된 `화성`의 인덱스값을 사용하세요.
solarsys.insert(pos1, '달')
# 3. index()를 이용해 '달'이 추가된 solarsys에서 '천왕성'의 인덱스 값을 pos2에 저장하세요.
pos2 = solarsys.index('천왕성')
# 4. '달'이 추가된 solarsys에 '토성'과 '천왕성' 사이에 새로운 요소로 'B612'를 삽입하세요. 
# pos2에 저장된 `천왕성`의 인덱스값을 사용하세요.
solarsys.insert(pos2, 'B612')
# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(solarsys) 

### 리스트의 특정 위치의 요소 제거하기 
del solarsys[1] 

### 리스트의 특정 요소 제거하기 
solarsys.remove('태양')

# 1. remove를 이용해 solarsys 리스트에서 '태양'을 제거하세요. 
solarsys.remove('태양')

### 리스트에서 특정 구간에 있는 모든 요소 제거하기 
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

# 1. 슬라이싱을 이용해 인덱스 1번 요소부터 3번 요소 미만까지 제거하세요.
del solarsys[1:3]

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(solarsys)

### 리스트에 있는 요소 개수 구하기 
listdata2 = [[2, 2, 1], 
             [3, 8, 5], 
             [7, 6, 3], 
             [6, 2, 3], 
             [9, 4, 4]]

# 1. solarsys에 있는 요소 개수를 구하세요.
listsize1 = len(listdata2)

### 리스트 제거하기 - del은 리스트를 메모리에서 제거
del week 

### 리스트 요소 정렬하기 
# 실습에 사용할 변수를 선언합니다.
lotto770 = [34, 1, 43, 9, 12, 39, 23]
namelist = ['Marry', 'Sams', 'Aimy', 'Tom', 'Michael', 'Bob', 'Kelly']

# 1. sort를 이용해 lotto770의 원소를 오름차순으로 정렬하세요.
lotto770.sort()

# 2. sorted를 이용해 namelist의 원소를 알파벳 내림차순으로 정렬한 값을 ret에 저장하세요.
ret = sorted(namelist, reverse=True)

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(lotto770)
print(ret)

### 리스트 요소 무작위로 섞기 
## shuffle()을 사용하면 리스트의 요소를 무작위로 섞을 수 있음. 원본리스트 변경됨 
shuffle(lotto770)

### 리스트의 모든 요소를 인덱스와 쌍으로 추출하기 
# 실습에 사용할 변수를 선언합니다.
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

# 1. enumerate와 list를 이용해 solarsys의 모든 요소를 인덱스와 쌍으로 추출하여 ret에 저장하세요.
ret = list(enumerate(solarsys))

# 2. for문과 enumerate를 함께 사용한 아래 코드를 실행해보세요.
# solarsys의 인덱스와 요소를 각각 i와 body에 순서대로 저장합니다. 
for i, body in enumerate(solarsys):    
    # 첫번째 반복문에서는 태양의 인덱스0과 태양이 i와 body에 저장됩니다.
    print('태양계의 %d번째 천체: %s' %(i, body))

# 아래는 출력을 위한 코드입니다. 수정하지 마세요.
print(ret)




