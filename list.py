l1=input('enter your list: ').split(',')
ind=int(input('enter index to change: '))
for i in range(len(l1)):
    if ind<=len(l1):
        l1[ind]='changed'
    else:
        print('you entered wrong string')
print(l1)