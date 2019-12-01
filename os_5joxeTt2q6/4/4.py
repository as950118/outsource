# 쇼핑몰에서 배송을 위해 사용자 주소 확인하는 프로그램

# 입력 받기
def AddrInput():
    print ("Please enter your city and a province abbreviation separated by a comma on the first line and your postal code on the second line")
    city_abbreviation = input().title()
    postal_code = input()
    return city_abbreviation, postal_code

# 이름과 지역약자로 나누기
def AbbSplit(city_abbreviation):
    # 콤마가 없는 경우에는 오류 Case 2
    if not "," in city_abbreviation:
        return -2, -2
    # 콤마를 기준으로 나눠주기
    ## 먼저 find로 콤마의 위치를 찾음
    comma_index = city_abbreviation.find(",")
    ## 해당 위치를 기준으로 분할
    city_name, city_abbreviation = city_abbreviation[:comma_index], city_abbreviation[comma_index+1:]
    # 약자에서 불필요한 스페이스 제거
    city_abbreviation = city_abbreviation.replace(" ", "")
    # 약자가 2자리가 아닐 경우에는 오류 Case 1
    if len(city_abbreviation) != 2:
        return -1, -1
    # 오류가 없다면 이름과 약자를 반환
    return city_name, city_abbreviation

# 우편주소를 두개 그룹으로 나누기
def PostSplit(postal_code):
    # 먼저공백을 없에주고
    postal_code = postal_code.replace(" ", "")
    # 먼저 6글자인지 체크
    if len(postal_code) != 6:
        ## 우편번호가 형식에 맞지 않는 것이므로 Case 3
        return -3, -3
    # 형식에 맞는지 확인(알파벳-숫자-알파벳 숫자-알파벳-숫자)
    if postal_code[0].isalpha() and postal_code[1].isdecimal() and postal_code[2].isalpha() \
            and postal_code[3].isdecimal() and postal_code[4].isalpha() and postal_code[5].isdecimal():
        # 맞다면 두개의 그룹으로 나누어줌
        postal_code_1, postal_code_2 = postal_code[:3], postal_code[3:]
        return postal_code_1, postal_code_2
    else:
        ## 아니라면 우편번호가 형식에 맞지 않는 것이므로 Case 3
        return -3, -3

# 정규화 시키기
def Normalization(city_name, city_abbreviation, postal_code_1, postal_code_2):
    ## 도시이름은 첫글자만 대문자로
    city_name = city_name.title()
    ## 약자는 모두 대문자로
    city_abbreviation = city_abbreviation.upper()
    ## 우편주소도 모두 대문자로
    postal_code_1 = postal_code_1.upper()
    postal_code_2 = postal_code_2.upper()
    return city_name, city_abbreviation, postal_code_1, postal_code_2

# 지역약자가 테이블에 있는지 확인
def CheckAbbr(city_abbreviation):
    abbr_table = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"]
    # 테이블에 해당 도시의 약자가 있다면 해당 약자 순서 return
    if city_abbreviation in abbr_table:
        abbr_num = abbr_table.index(city_abbreviation)
        return abbr_num
    # 없을경우에는 오류 Case -4
    else:
        return -4

# 지역 우편번호 시작자리가 맞는지
def CheckPost(postal_code_1, abbr_num):
    post_table = ["T", "V", "R", "E", "A", "X", "B", "X", "KLMNP", "C", "GHJ", "S", "Y"]
    # 해당위치에 있는 문자가 postal_code_1의 첫번째 숫자와 일치하는게 있다면 return 1
    if postal_code_1[0] in post_table[abbr_num]:
        return 1
    # 아니라면 우편번호가 테이블에 없으므로 오류 Case 5
    else:
        return -5

# 비용 출력
def CheckCost(city_abbreviation):
    cost_table = {"AB":12, "BC":12, "MB":12, "SK":12,
                  "NB":15, "NL":15, "NS":15, "PE":15,
                  "NT":20, "NU":20, "YK":20,
                  "ON":8, "QC":8}
    ret_cost = cost_table[city_abbreviation]
    return ret_cost

# 에러처리
def Err(Err_num):
    ## Case 1 지역약자가 1자리 혹은 3자리 이상의 글자를 입력할때
    if Err_num == -1:
        print("Error : Province abbreviation should be 2 letters. Please re-enter the address")
    ## Case 2 콤마(,)가 없을 경우
    elif Err_num == -2:
        print("Error : Address should be two parts(city and province abbreviation) and separated by comma. Please re-enter the address")
    ## Case 3 우편주소가 안맞을 경우
    elif Err_num == -3:
        print("Error: You entered the wrong postal code. Please check and re-enter it")
    ## Case 4 지역약자가 테이블에 없는 경우
    elif Err_num == -4:
        print("Error: You entered wrong province abbreviation. Please re-enter your city and province abbreviation")
    ## Case 5 우편번호의 첫글자가 테이블에 없는 경우
    elif Err_num == -5:
        print("Error: You entered the wrong postal code. Please check and re-enter it")



##### 프로그램 시작 #####

# 입력받기
city_abbreviation, postal_code = AddrInput()

# 이름과 지역으로 나누기
city_name, city_abbreviation = AbbSplit(city_abbreviation)
## 오류가 있다면 Err 발생후 종료
if city_abbreviation == -1 or city_abbreviation == -2:
    Err_num = city_abbreviation
    Err(Err_num)

else:
    # 우편주소 두개 그룹으로 분리
    postal_code_1, postal_code_2 = PostSplit(postal_code)
    ## 오류가 있다면 Err 발생후 종료
    if postal_code_1 == -3:
        Err_num = postal_code_1
        Err(Err_num)

    else:
        # 정규화 시키기
        city_name, city_abbreviation, postal_code_1, postal_code_2 = Normalization(city_name, city_abbreviation, postal_code_1, postal_code_2)

        # 테이블 검사
        abbr_num = CheckAbbr(city_abbreviation)
        ## 오류가 있다면 Err 발생후 종료
        if abbr_num == -4:
            Err_num = abbr_num
            Err(Err_num)

        else:
            Err_num = CheckPost(postal_code_1, abbr_num)
            ## 오류가 있다면 Err 발생후 종료
            if Err_num == -5:
                Err(Err_num)

            else:
                # 결과 출력
                ret_cost = CheckCost(city_abbreviation)
                print("Shipping to {0}, {1} – {2} {3} will cost ${4}.".format(city_name, city_abbreviation, postal_code_1, postal_code_2, ret_cost))
