import pandas as pd
listA = ['hong', 'lee', 'ryu', 'yoon']
seriesA = pd.Series( listA )
type(seriesA)

listB = ( ['hong', 29, 'F'], ['lee', 24, 'M'], \
          ['rye', 28, 'M'], ['yoon', 31, 'F'])
dataframeB = pd.DataFrame(listB)
type(dataframeB)
dataframeB.index = ['No.1', 'No.2', 'No.3', 'No.4']
dataframeB.columns = ['Name', 'Age','Sex']
dataframeB
dataframeB['Age']    # 열 추출 
dataframeB[['Name', 'Age']]   #리스트 형태로 열 추출 

dataframeB[1:3]   #0부터 시작되며,끝위치-1까지 가져옴  [첫위치:끝위치] 
dataframeB['No.2':'No.4']  

data = pd.read_csv('../bigdata/x_test.csv')   #csv 파일 읽어오기 
data
data.to_csv('../bigdata/x_test_utf8_cp.csv')   # 읽은 데이터를 csv 파일로 저장 