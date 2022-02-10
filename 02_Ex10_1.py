# -를 포함하여 주민등록번호를 입력받아 생년월일을 표기하시오.
# 형식이 맞지 않을 경우 하이픈의 위치가 잘못되었다고 표기하시오.

while True:
    p = input('하이픈을 포함하여 전체 주민등록번호를 입력하세요>')
    if p.find('-') != 6 :
        print('하이픈의 위치가 잘못되었습니다.')
        continue
    birthday = p.split('-')[0]
    print('생년월일은 {}입니다.'.format(birthday))
    break
