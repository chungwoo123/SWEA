'''
어떤 수 n이 1이 될때까지 다음 두 과정 중 하나를 반복적으로 선택해 수행하려고 함.

단, 두 번째 연산은 N이 K로 나누어 떨어질 떄만 선택 가능함.

1. N에서 1을 뺀다
2. N을 K로 나눈다

N과 K가 주어졌을 때, 연산을 실행하기 위한 최소 횟수를 구하는 프로그램을 작성하시오.

'''
N, K = map(int, input().split())
result = 0

def solve1():
    global result 
    result += 1
    return N - 1

def solve2():
    global result
    result += 1
    return N // K

while N != 1:
    if N % K == 0:
        N = solve2()  # 함수가 돌려준 값을 N에 대입하여 업데이트!
    else:
        N = solve1()  # 함수가 돌려준 값을 N에 대입하여 업데이트!

print(result)  # 결과 출력 추가