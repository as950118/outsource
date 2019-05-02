import datetime

n = int(input())
M = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
ret = []
for i in range(n):
    d,m,y = map(str, input().split())
    for i in range(4):
        if d[i].isalpha():
            d = int(d[:i])
            break
    m = M[m]
    y = int(y)
    ret.append(str(datetime.date(y,m,d)))
print(ret)

