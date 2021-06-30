import random
print('Types of Dices')
print('1.Unbiased')
print('2.Digit 1 has higher probability of appearance')
print('3.Digit 2 has higher probability of appearance')
print('4.Digit 3 has higher probability of appearance')
print('5.Digit 4 has higher probability of appearance')
print('6.Digit 5 has higher probability of appearance')
print('7.Digit 6 has higher probability of appearance')
q=int(input('Which type of dice you want'))
if q!=1:
    qw=input('do you want to put chances of biased digit(y/n)')
    if qw=='y':
        qw=float(input('chances in decimal Example 0.4,0.5,0.32 etc'))
        ps=(1-qw)/5
        if q==2:
            while True:
                a=input('')
                k=random.choices([1,2,3,4,5,6],[qw,ps,ps,ps,ps,ps])
                print(k)
        if q==3:
            while True:
                a=input('')
                k=random.choices([2,1,3,4,5,6],[qw,ps,ps,ps,ps,ps])
                print(k)
        if q==4:
            while True:
                a=input('')
                k=random.choices([3,1,2,4,5,6],[qw,ps,ps,ps,ps,ps])
                print(k)
        if q==5:
            while True:
                a=input('')
                k=random.choices([4,2,1,3,5,6],[qw,ps,ps,ps,ps,ps])
                print(k)
        if q==6:
            while True:
                a=input('')
                k=random.choices([5,2,3,1,4,6],[qw,ps,ps,ps,ps,ps])
                print(k)
        if q==7:
            while True:
                a=input('')
                k=random.choices([6,2,3,4,1,5],[qw,ps,ps,ps,ps,ps])
                print(k)
    elif qw=='n':
        print('ok default chances of biased digit is 4 out of 10')
    
if q==1:
    while True:
        a=input('')
        print(random.randint(1,6))
if q==2:
    while True:
        a=input('')
        k=random.choices([1,2,3,4,5,6],[0.40,0.12,0.12,0.12,0.12,0.12])
        print(k)
if q==3:
    while True:
        a=input('')
        k=random.choices([2,1,3,4,5,6],[0.40,0.12,0.12,0.12,0.12,0.12])
        print(k)
if q==4:
    while True:
        a=input('')
        k=random.choices([3,1,2,4,5,6],[0.40,0.12,0.12,0.12,0.12,0.12])
        print(k)
if q==5:
    while True:
        a=input('')
        k=random.choices([4,2,1,3,5,6],[0.40,0.12,0.12,0.12,0.12,0.12])
        print(k)
if q==6:
    while True:
        a=input('')
        k=random.choices([5,2,3,1,4,6],[0.40,0.12,0.12,0.12,0.12,0.12])
        print(k)
if q==7:
    while True:
        a=input('')
        k=random.choices([6,2,3,4,1,5],[0.40,0.12,0.12,0.12,0.12,0.12])
        print(k)

