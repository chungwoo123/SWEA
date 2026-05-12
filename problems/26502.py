#2차원 평면 위에 N개의 서로 다른 점이 있다. 각 점의 x, y 좌표는 정수이다.
#당신은 이 중 서로 다른 3개의 점을 골라서 삼각형을 만들려고 한다.
#이 때 삼각형의 한 변은 x축에 평행해야 하고, 다른 한 변은 y축에 평행해야 한다.
# 
#당신이 만들 수 있는 삼각형의 최대 넓이는 얼마인가?

#넓이에 2를 곱하면 정수가 되니, 최대 넓이에 2를 곱해 출력하라.

#만들 수 있는 삼각형이 최소 하나 존재한다. 

#[입력]
 
#첫 번째 줄에 테스트 케이스의 수 TC가 주어진다.
#이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
#각 테스트 케이스는 다음과 같이 구성되었다. 
#첫 번째 줄에 점의 수 N이 주어진다. (3 ≤ N ≤ 100)
#이후 N개의 줄에 점의 좌표 xi, yi 가 주어진다. 모든 좌표는 서로 다르고, 좌표는 절댓값이 10000 이하인 정수이다. 


#[출력]
#각 테스트 케이스 마다 한 줄씩, 문제의 정답을 출력하라.

# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        #정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        #정수형 변수 2개 입력 받는 예제 
d = float(input())                      #실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   #실수형 변수 3개 입력 받는 예제
h = input()                             #문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
#아래의 구문은 input.txt 를 read only 형식으로 연 후,
#앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
#여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
#아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
#따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
#아래 구문을 사용하기 위해서는 import sys가 필요합니다.
#단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
T_str = input().strip()
if T_str:
    T = int(T_str)
    
    for test_case in range(1, T + 1):
        N = int(input().strip())
        
        points = []
        # 각 좌표별 최소/최대값을 저장할 딕셔너리
        min_y_at_x = {}
        max_y_at_x = {}
        min_x_at_y = {}
        max_x_at_y = {}
        
        for _ in range(N):
            # 한 줄씩 읽어서 x, y 좌표 추출
            x, y = map(int, input().split())
            points.append((x, y))
            
            # 해당 x좌표에서 나타난 y의 최소/최대값 갱신
            if x not in min_y_at_x or y < min_y_at_x[x]: min_y_at_x[x] = y
            if x not in max_y_at_x or y > max_y_at_x[x]: max_y_at_x[x] = y
            
            # 해당 y좌표에서 나타난 x의 최소/최대값 갱신
            if y not in min_x_at_y or x < min_x_at_y[y]: min_x_at_y[y] = x
            if y not in max_x_at_y or x > max_x_at_y[y]: max_x_at_y[y] = x
            
        max_area_2 = 0
        
        # 모든 점을 순회하며 해당 점이 '직각을 이루는 모서리'일 때의 최대 넓이 계산
        for x, y in points:
            # 현재 점(x,y)과 같은 x축 상에 있는 점들 중 가장 먼 거리(높이)
            dy = max(abs(y - min_y_at_x[x]), abs(y - max_y_at_x[x]))
            
            # 현재 점(x,y)과 같은 y축 상에 있는 점들 중 가장 먼 거리(밑변)
            dx = max(abs(x - min_x_at_y[y]), abs(x - max_x_at_y[y]))
            
            # 두 변의 곱 (넓이 * 2)
            current_area_2 = dx * dy
            if current_area_2 > max_area_2:
                max_area_2 = current_area_2
                
        # 표준 출력 형식에 맞춰 결과 출력
        print("#{} {}".format(test_case, max_area_2))
    # ///////////////////////////////////////////////////////////////////////////////////
