a_list = ['above','cookie','app','about','admin','bisket','apple','april']
for i , item in enumerate(a_list):
    if item.find('a') != -1 :
        print('{} 제거됩니다.'.format(a_list.pop(i)))

print(a_list)

# pop하면서 index num이 땡겨지며 리스트의 데이터가 다 검토되지 못함
# while 이용하여 다시 풀어보기

a_list1 = ['above','cookie','app','about','admin','bisket','apple','april']
while True:
    for a, b in enumerate(a_list1):
        if b.find('a') != 1 :
            a_list1.pop(a)
    break
print(a_list1)