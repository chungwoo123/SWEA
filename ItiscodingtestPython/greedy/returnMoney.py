'''tc = int(input()) # 테스트 케이스

for _ in range(tc): # 테스트 케이스 만큼 반복

    result_money = 0 # 반환할 돈
    customer_money = int(input()) # 손님이 낸 돈

    money500 = customer_money // 500 # 500원 개수
    money100 = (customer_money % 500) // 100 # 100원 개수
    money50 = (customer_money % 100) // 50 # 50원 개수
    money10 = (customer_money % 50) // 10 # 10원 개수
    money5 = (customer_money % 10) // 5 # 5원 개수
    money1 = customer_money % 5 # 1원 개수

    result_money += money500
    result_money += money100
    result_money += money50
    result_money += money10
    result_money += money5
    result_money += money1

    print(result_money)
'''

'''
def solve():
    result_money = 0 # 반환할 돈
    customer_money = int(input()) # 손님이 낸 돈

    coin_types = [500, 100, 50, 10, 5, 1]

    for coin in coin_types:
        result_money += customer_money // coin
        customer_money %= coin
    
    return result_money
'''

# [새 코드] 각 동전의 개수를 상세히 기록하고 출력해주는 버전
def solve_detailed():
    customer_money = int(input()) # 손님이 낸 돈
    coin_types = [500, 100, 50, 10, 5, 1]
    coins_used = {}
    total_coins = 0
    
    for coin in coin_types:
        count = customer_money // coin
        coins_used[coin] = count
        total_coins += count
        customer_money %= coin
        
    print("--- 거스름돈 반환 상세 결과 ---")
    for coin, count in coins_used.items():
        if count > 0:
            print(f"{coin}원 동전: {count}개")
    print(f"총 동전 개수: {total_coins}개")
    
    return total_coins

if __name__ == '__main__':
    solve_detailed()