#password.py

#조건은 다음과 같음
#1. 최소한 10글자 이상
#2. 최소한 1글자의 대문자
#3. 최소한 숫자 하나
#4. 최소한 다음 특수문자 중 하나 사용($#%&*)
#5. 공백없이

def passwordIsOk(string_password):
    ret = True

    check_length = True
    if len(string_password) < 10:
        check_length = False
    if not check_length:
        print("length should be at least 10")
        ret = False

    check_upper = False
    for word in string_password:
        if word.isupper():
            check_upper = True
            break
    if not check_upper:
        print("password should have at least one uppercase letter")
        ret = False

    check_num = False
    for word in string_password:
        if word.isdecimal():
            check_num = True
            break
    if not check_num:
        print("password should have at least one numeral")
        ret = False

    check_special = False
    specials = "$#%&*"
    for word in string_password:
        if word in specials:
            check_special = True
            break
    if not check_special:
        print("password should have at least one of the symbols $, #, %, &, *")
        ret = False

    check_space = True
    for word in string_password:
        if word.isspace():
            check_space = False
            break
    if not check_space:
        print("spaces are not allowed")
        ret = False

    if ret:
        print("Password is valid")
    else:
        print("Invalid password")

    return ret

if __name__ == "__main__":
    input_password = str(input("Input password : "))
    passwordIsOk(input_password)