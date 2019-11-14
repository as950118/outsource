import turtle as t

t.hideturtle()
t.speed(0)
nmonth = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
nday = ['일', '월', '화', '수', '목', '금', '토']


def printnday():
    for i in range(7):
        t.write(nday[i])
        t.forward(30)

    t.forward(40)


def cday(year, month, day):
    increasey = 1
    increasem = 1
    increasedayofm = 0

    while 1:
        dayofm = 31

        if increasem == 4 or increasem == 6 or increasem == 9 or increasem == 11:
            dayofm = 30
        elif increasem == 2:
            if (increasey % 4 == 0 and increasey % 100 != 0) or (increasey % 400 == 0):
                dayofm = 29
            else:
                dayofm = 28
        if (increasey == year) and (increasem == month):
            break;
        increasedayofm += dayofm
        increasem += 1

        if increasem > 12:
            increasem = 1
            increasey += 1
    weekindex = (day + increasedayofm) % 7
    return weekindex


year = int(t.numinput("입력", '연도를 입력하시오:'))

t.penup()
t.goto(-700, 300)
t.pencolor("black")
t.write(str(year) + "년", font=('Arial', 40, 'bold'))

t.right(90)
t.forward(50)
t.left(90)
(x, y) = t.position()
print(x)
print(y)
for i in range(12):
    t.write(nmonth[i], font=('Arial', 20, 'normal'))
    t.forward(250)
    if i == 5:
        t.goto(-700, 0)

t.goto(-700, 210)

for i in range(12):
    printnday()
    if i == 5:
        t.goto(-700, -50)

(q, p) = t.position()
print(p)
print(q)

t.goto(-700, 200)

# qq=cday(year,1,1)

for i in range(1, 32):
    t.write(i)
    t.forward(30)
    if i == 6:
        t.goto(-700, 190)
    elif i == 13:
        t.goto(-700, 180)
    elif i == 20:
        t.goto(-700, 170)
    elif i == 27:
        t.goto(-700, 160)

