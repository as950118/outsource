#password.py

#조건은 다음과 같음
#1. 최소한 10글자 이상
#2. 최소한 1글자의 대문자
#3. 최소한 숫자 하나
#4. 최소한 다음 특수문자 중 하나 사용($#%&*)
#5. 공백없이

def CheckLength(string_password):
    if len(string_password) < 10:
        return False
    return True

def CheckUpper(string_password):
    for word in string_password:
        if word.isupper():
            return True
    return False

def CheckNum(string_password):
    for word in string_password:
        if word.isdecimal():
            return True
    return False

def CheckSpecial(string_password):
    specials = "$#%&*"
    for word in string_password:
        if word in specials:
            return True
    return False

def CheckSpace(string_password):
    for word in string_password:
        if word.isspace():
            return False
    return True

def passwordIsOk(string_password):
    ret = True
    if not CheckLength(string_password):
        print("length should be at least 10")
        ret = False
    if not CheckUpper(string_password):
        print("password should have at least one uppercase letter")
        ret = False
    if not CheckNum(string_password):
        print("password should have at least one numeral")
        ret = False
    if not CheckSpecial(string_password):
        print("password should have at least one of the symbols $, #, %, &, *")
        ret = False
    if not CheckSpace(string_password):
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