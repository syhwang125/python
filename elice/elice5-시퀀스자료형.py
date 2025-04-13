# 실습에 사용할 변수를 선언합니다.
strdata1 = 'I love Python'
strdata2 = '나는 파이썬을 사랑합니다'
listdata = ['a', 'b', 'c', strdata1, strdata2]
# 1. strdata1의 크기를 출력하세요.
print(len(strdata1))
# 4. listdata의 인덱스 3 요소의 크기를 출력하세요.
print(len(listdata[3]))

strdata3 = '''I love 
python. You love
python too!'''
print(strdata3)

# 4. 포맷 문자열을 이용해 '작년 세계 경제 성장률은 전년에 비해 5% 포인트 증가했다.'를 출력해보세요.
print("작년 세계 경제 성장률은 전년에 비해 %d%% 포인트 증가했다." %num1)

# 실행 버튼을 클릭하고 출력문 결과를 확인해보세요.
print('나는 파이썬을 사랑합니다. \n파이썬은 자바보다 훨씬 쉽습니다.')
print('Name: John Smith\tSex: Male\tAge: 22')
print('이 문장은 화면폭에 비해 너무 길어 보기가 힘듭니다.\
그래서 \\Enter키를 이용해 문장을 다음줄과 연속되도록 했습니다.')
print('작은 따옴표(\')와 큰 따옴표(\")는 문자열을 정의할 때 사용합니다.')

#튜플은 리스트와 비슷하게 여러 멤버를 쉼표로 구분하여 순서 대로 나열하지만 ()를 사용하고 요소의 값을 변경할 수 없습니다.
strdata = (1, 2, 3)

#사전은 ‘키’와 ‘값’을 하나의 쌍으로 갖는 자료형 입니다. 사전은 리스트, 튜플과 달리 시퀀스 자료형이 아니며 다음과 같은 형태를 가지고 있습니다.
#dict = {Key1:Value1, Key2:Value2, Key3:Value3, ...}
# 'a':1, 'b':2, 'c':3 세 개의 키:값 쌍을 멤버로 가지고 있는 사전을 `dict1`에 저장하세요.
dict1 = {'a':1, 'b':2, 'c':3}

# dict1에 키 'a'에 해당하는 값을 출력하세요.
print(dict1['a'])

# dict1에 'd':4 키:값 쌍을 새로 추가하세요.
dict1['d'] = 4

# dict1에 키 'b'에 해당하는 값을 7로 바꿔보세요.
dict1['b'] = 7 

# len()을 사용해 `dict1`의 크기를 출력하세요.
print(len(dict1))