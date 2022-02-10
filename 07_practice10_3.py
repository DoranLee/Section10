data = '"홍길동", 85'
data_list = data.split(',')
data_list[0] = data_list[0].strip('"')  # "제거
print('이름은 {}이고 점수는 {}점입니다.'.format(data_list[0], data_list[1]))