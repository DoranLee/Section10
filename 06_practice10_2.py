# 사업자 번호를 입력받아(형식:000-00-0000) 각 숫자의 개수와 숫자가 맞는지 확인하시오.

no = input('사업자 번호를 입력하세요(예:123-45-67890) > ')
no_list = no.split('-')
result = True

if len(no_list[0]) != 3 or len(no_list[1]) != 2 or len(no_list[2]) != 5 :
    result = False

for n in no_list :
    if not n.isdecimal():
        result = False

if result == True :
    print('올바른 형식입니다.')
else :
    print('올바른 형식이 아닙니다.')