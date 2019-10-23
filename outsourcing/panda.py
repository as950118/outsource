import pandas as pd
from operator import itemgetter


#####전처리 데이터
datas = pd.read_csv("./NTX.csv")
#print(datas)
####################

######정렬과정

#pandas datas를 한줄씩 출력하는 함수
def print_datas(func_datas):
    for data in func_datas:
        print(data)
    return None


# company_1을 기준점으로 내림차순 정렬하는 함수
# by="Company_1"은 idx Company_1을 기준으로 정렬한다는 뜻임
# ascending=False는 내림차순으로 정렬하는것을 의미
def func_sort(func_datas, row):
    ret_datas = func_datas.sort_values(by=row, ascending=False)
    return ret_datas


# data를 기준열(row)에 따라 나누어 반환하는 함수
def func_split_data(func_datas, row):
    ret_datas = func_datas.groupby(row)
    return ret_datas


# data에서 final을 추가하여 반환하는 함수
def func_final(func_datas):
    ret_datas = []  # 결과 데이터

    #key를 제외한 원본 panda데이터만 추출
    ret_datas = func_datas[1]
    #정렬
    ret_datas = func_sort(ret_datas, ["Company_2_len","Km"])
    #가장 앞의값, 즉 가장 큰값의 Company_2 를 Final로 설정
    final = ret_datas.head(1)["Company_2"].values[0]
    ret_datas["Final"] = final
    return ret_datas



if __name__ == "__main__":
    print("\n\n#####Origin Data######\n")
    print(datas)

    # 내림차순 정렬
    print("\n\n#####Sroted Data#####\n")
    datas = func_sort(datas, "Company_1")
    print(datas)

    # company, nation로 나누기
    print("\n\n#####Splited Data#####\n")
    datas = func_split_data(datas, ["Company_1","Nation"])
    print_datas(datas)

    # final을 추가한 결과 데이터
    print("\n\n#####Result#####\n")
    datas_ret = []
    for data in datas:
        datas_ret.append(func_final(data))
    #pandas로 병합
    datas_ret = pd.concat(datas_ret)
    print(datas_ret)

    #ID 순서로 정렬
    print("\n\n#####Result(2)#####\n")
#    datas_ret = func_sort(datas_ret, "index")
    datas_ret = datas_ret.sort_index()
    print(datas_ret)
