try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except:    # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.')
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except:    # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.')

# try ~ exception 
# 1. 정의되지 않은 변수 param을 출력해보세요.
#print(param)
# 2. 위 코드를 주석처리하고 아래 코드를 추석 해제한 후, try~except를 사용하면 어떤 결과값이 출력될지 생각해보고 제출해보세요.
try:
    print('안녕하세요.')
    print(param)
except:
    print('예외 상황이 발생했습니다!')

 # 1. try~except~else문을 실행해보세요.
try:
    print('안녕하세요.')
# 2. print(param)을 주석 처리한 후 실행・제출해보세요.
    #print(param)
except:
    print('예외가 발생했습니다!')
else:
    print('예외가 발생하지 않았습니다.')   


# 1. try~except~finally문을 실행해보세요.
try:
    print('안녕하세요.')
    # 2. print(param)을 주석처리한 후 실행・제출해보세요.
    #print(param)
except:
    print('예외가 발생했습니다!')
finally:
    print('무조건 실행하는 코드')