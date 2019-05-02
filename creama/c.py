n = int(input())
ret = []
for i in range(n):
    temp = list(str(input()))
    for i in range(len(temp)-1, -1, -1):
        if not temp[i].isdigit():
            op1 = temp.pop()
            op2 = temp.pop()
            temp.append(op1 + op2 + temp[i])
        else:
            temp.append(temp[i])
    print(temp[-1])
