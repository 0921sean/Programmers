# # 다른 사람의 풀이
# def solution(prices):
#     stack = []
#     answer = [0] * len(prices)
    
#     for i in range(len(prices)):
#         if stack != []:
#             while stack != [] and stack[-1][1] > prices[i]:
#                 past, _ = stack.pop()
#                 answer[past] += i - past
#         stack.append([i, prices[i]])
#     for i, s in stack:
#         answer[i] += len(prices) - i - 1
#     return answer

# 내가 작성한 풀이
def solution(prices):
    price_list = []
    time_list = [0] * len(prices)
    
    for i in range(len(prices)):
        # 만약 price_list가 비어있다면 또는 현재 가격이 이전 가격보다 높거나 같으면, 현재 가격을 추가하고 시간을 기록
        if not price_list or prices[i] >= price_list[-1][1]:
            price_list.append([i, prices[i]])
            print(f"현재 가격: {price_list}, 시간: {time_list}")
            continue
        # 현재 가격이 이전 가격보다 낮으면, 이전 가격을 제거하고 시간을 기록
        while True:
            if price_list and price_list[-1][1] > prices[i]:
                cal_price = price_list.pop()
                time_list[cal_price[0]] += i - cal_price[0]
            else:
                price_list.append([i, prices[i]])
                break
        print(f"현재 가격: {price_list}, 시간: {time_list}")
                
    for i in range(len(time_list)):
        if time_list[i] == 0:
            time_list[i] += len(prices) - i - 1
    return time_list

# 테스트 케이스
if __name__ == "__main__":
    prices_list = [[1, 2, 3, 2, 3], [1, 2, 3, 2, 3, 1], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]]
    for prices in prices_list:
        result = solution(prices)
        print(result)