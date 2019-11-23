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
시간복잡도는 처음에 binarian(A)를 구할때 O(N)이고, 
결과를 구할때는 배열의 최대 크기인 O(MAX) 이다.

####공간복잡도
공간복잡도는 배열의 최대 크기인 O(MAX*sizeof(type(counter))) 이다.
'''
def solution(A):
    # 배열의 최대크기 설정
    MAX = 11000
    # bit counter 배열 선언
    counter = [0] * MAX

    # A 배열에서 number 하나씩 꺼내어서
    for number in A:
        # counter의 index == number에 해당하는 값을 +1 해줌
        counter[number] += 1

    # bit 연산을 위한 carry 설정
    carry = 0
    # counter 배열을 모두 조사하여
    for i in range(MAX):
        # counter의 i번째에 해당하는 값에 +carry를 해줌
        # 케리가 있었다면 +1 될 것이고 아니라면 그대로 값이 유지될 것임
        counter[i] += carry
        # 그리고 carry = counter[i] // 2 를 해줌
        # 왜냐하면 bit가 한 자리씩 왼쪽으로 이동할 때마다 * 2가 되므로
        # 반대로 // 2 해준 값을 carry로 설정해줘야함
        carry = counter[i] // 2
        # 현재 index의 counter가 홀수일 경우에는 1, 아니면 0으로 처리해줌
        counter[i] %= 2

    # 결과값 구하기
    answer = 0
    for i in range(MAX):
        # 해당 index의 counter에 값이 있을경우 + counter[index]해줌
        # counter[index]는 1 또는 0임
        answer += counter[i]

    return answer

if __name__ == "__main__":
    print(solution([1,0,2,0,0,2, 0, 1,0]))