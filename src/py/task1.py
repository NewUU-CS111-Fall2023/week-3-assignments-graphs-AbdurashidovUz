a=int(input())
b=int(input())
answer = []

while b>=a:
    answer.append(b)
    if b%2 == 0:
        b=b//2
    elif b%10==1:
        b=(b-1)//10
    else:
        break

if answer[-1]==a:
    print ("yes")
    print (len(answer))
    print(answer[::-1])
else:
    print("NO")
