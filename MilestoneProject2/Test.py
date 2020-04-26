

list1 = [1,2,3,4,5,1,2,3,1,2,3]

for i in list1 or i+1 in list1:
    print('Number found')

repeat = 'none'
while repeat != 'Y' and repeat != 'N':
    repeat = input('Do you want to continue playing? Y/N: ').upper()

