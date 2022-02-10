'''
    함수(function) : 단독으로 존재하는 기능
    메서드(method) : 객체(object) 안에 존재하는 기능
'''

# 정렬
#   d(십진법 숫자), s(문자) 10칸만큼의 공간에서 오른쪽(>)정렬
print('오른쪽 정렬 : {:>10d}'.format(123))
print('오른쪽 정렬 : {:>10s}'.format('s'))
#   생략시 숫자는 오른쪽, 문자는 왼쪽 정렬(like 엑셀)
print('왼쪽 정렬 : {:10d}'.format(123))
print('왼쪽 정렬 : {:10s}'.format('s'))
#   가운데 정렬 : ^
print('가운데 정렬 : {:^10d}'.format(123))
print('가운데 정렬 : {:^10s}'.format('s'))
#   빈 공간을 ><^ 앞의 문자로 채움(한 글자만 가능)
print('오른쪽 정렬 : {:*>10d}'.format(123))
print('왼쪽 정렬 : {:*<10d}'.format(123))
print('가운데 정렬 : {:*^10d}'.format(123))
print('---------------------------------')

# 검색
s='Hello World Test World In Python'
#   단어의 개수
print(s.count('World'))
print(s.count('World',11))  # index num 11이후부터 검색
#   단어의 위치
print(s.find('World'))
print(s.find('World', 11))  # index num 11이후부터 검색
print(s.rfind('World'))     # 맨 뒤에서부터 검색
print(s.find('Java'))       # 찾는 값이 없을 경우 -1

print(s.index('World'))
# print(s.index('Java'))      # 찾는 값이 없을 경우 Error
print('---------------------------------')

print(s.upper())            # 모두 대문자로
print(s.lower())            # 모두 소문자로
print(s.capitalize())       # 첫 글자만 대문자, 나머지는 소문자로 변경
print('---------------------------------')

lst = ['A','B','C','D','E']
print('+'.join(lst))        # 리스트의 각 요소들을 하나의 문자열로 합쳐줌(압축)
l = '+'.join(lst)
print(l.split('+'))         # 압축해제
print('---------------------------------')

# 문자대체
print(s.replace('World','Hell'))
print('---------------------------------')

# 공백제거
s1 = '           A'
s2 = 'A           '
s3 = '      A     '
print(s1.lstrip(), len(s1.lstrip()))    # 왼쪽 공백 제거
print(s2.rstrip(), len(s2.rstrip()))    # 오른쪽 공백 제거
print(s3.strip(), len(s3.strip()))      # 양쪽 공백 제거

s1 = '..........A'
print(s1.lstrip('.'), len(s1.lstrip('.')))    # 왼쪽의 해당 문자 제거
