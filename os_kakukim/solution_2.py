'''
####문제
비어있지 않은 양의 정수로 N개로 이루어진 배열 A에 대해서
binarian은 다음과 같이 정의된다.
binarian(A) = pow2(A[0]) + pow2(A[1]) + ... + pow2(A[N-1])
pow2는 다음과 같이 정의된다.
pow2(k) = 2**k

이때, binarian(A) == binarian(B) 의 결과값을 가지면서
가장 길이가 짧은 배열을 B라고 했을때
이 B의 길이를 구하시오
'''
'''
####해결방식
기본적으로 연산이 다른 방식으로 이루어진다고 해도
같은 결과값을 가지면 같은 형태로 표현이 되는 것은 자명하다.
예를 들어, 10+100 이나 10+10+10..+10 모두 같은 결과를 가지는것에 의문을 가질순없다.

해당 문제에서는 연산이 다양한 숫자들이 아닌 
단순히 2의 제곱들의 합으로 이루어진다.

2의 제곱들의 합은 2진수, 즉 bit 로 쉽게 표현과 연산이 가능하다.
그래서 연산과 연산 결과의 형태를 bit 를 이용하여 진행한다.

모두 잘 알겠지만, bit 값은 오른쪽부터 세어서 n 번째는 2**n이 된다.
이것은 처음 주어지는 A 배열에서 i번째 값이 k일때 2**k( pow2(A[i]) == pow2(k) ) 
라는 점과 같이 응용하여 bit 의 k번째 값으로 바꾸어 생각할 수 있다.

아까 위에서 말했듯, 연산의 결과로 나오는 형태는 어찌 되었든 같은 형태이다.
16+1을 하든 4+8+4+1을 하든 같다는 뜻이다.
그러면 어떤 결과든 한줄의 bit로 나타날 것이고
이 한줄의 bit에서 1의 갯수가 최소 길이가 될것이다.

####시간복잡도
시간복잡도는 binarian(A)를 구하는 부분이 N번 만큼 반복되므로 O(N), 
그 외에 결과값을 구하는 부분은 O(root(N)) 이다.

####공간복잡도
공간복잡도는 따로 이용하지 않고 변수와 bit 연산만을 이용하므로 O(1) 이다.
'''
def solution(A):
    # 먼저 binarian(A)를 구한다.
    # binarian_A = sum([2**a for a in A])
    binarian_A = 0
    for a in A:
        binarian_A += 2 ** a

    # 결과값의 bit 길이를 구한다.
    # len_bin = len(binarian_A) - 2
    len_bin = 0
    i = 0
    while 1 << i <= binarian_A:
        len_bin += 1
        i += 1

    # 결과값의 bit 에서 1의 갯수를 찾는다.
    # ret = sum([1 if (1<<i) & binarian_A else 0 for i in range(len_bin)])
    ret = 0
    for i in range(len_bin):
        if 1 << i & binarian_A:
            ret += 1
    return ret

if __name__ == "__main__":
    print(solution([1, 0, 2, 0, 0, 2, 0, 1]))