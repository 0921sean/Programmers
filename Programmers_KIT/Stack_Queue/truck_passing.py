# from collections import deque

# # 다른 사람의 풀이
# def solution(bridge_length, weight, truck_weights):
#     bridge = deque([0] * bridge_length)
#     total_weight = 0
#     step = 0
#     truck_weights.reverse()
    
#     while truck_weights:
#         total_weight -= bridge.popleft()  # 다리에서 트럭이 빠져나감
#         # 다리 위에 트럭이 못 올라가는 경우
#         if total_weight + truck_weights[-1] > weight:
#             bridge.append(0)
#         # 다리 위에 트럭이 올라갈 수 있는 경우
#         else:
#             truck = truck_weights.pop()
#             bridge.append(truck)
#             total_weight += truck
#         step += 1
#     return step + bridge_length  # 마지막 트럭이 다리를 완전히 지나갈 때까지의 시간 추가

# 직접 만든 해결책
def solution(bridge_length, weight, truck_weights):
    total_time = 0      # 총 소요 시간
    truck_bridge = []   # 다리 위 트럭 큐
    bridge_weight = 0   # 현재 다리 위 트럭 무게 합
    
    while truck_weights:
        # 매초마다
        total_time += 1
        
        # 다리 위의 나머지 트럭들에서는 1초만큼 지나감
        for truck in truck_bridge:
            truck[1] -= 1
            
        # 다리를 지난 트럭은 제거
        if truck_bridge and truck_bridge[0][1] == 0:
            bridge_weight -= truck_bridge[0][0]
            truck_bridge.pop(0)
        
        # 다음 트럭이 다리 위에 올라올 수 있는지 확인
        if bridge_weight + truck_weights[0] <= weight:
            added_truck = truck_weights.pop(0)
            truck_bridge += [[added_truck, bridge_length]]
            bridge_weight += added_truck
                
        # print(f"현재 시간: {total_time}, 다리 위 트럭: {truck_bridge}, 다리 위 무게: {bridge_weight}")
  
    total_time += truck_bridge[-1][1]  # 마지막 트럭이 다리를 완전히 지나갈 때까지의 시간 추가
         
    return total_time

# 첫 시도
# def solution(bridge_length, weight, truck_weights):
#     total_time = 0      # 총 소요 시간
#     truck_bridge = []   # 다리 위 트럭 큐
#     bridge_weight = 0   # 현재 다리 위 트럭 무게 합
    
#     while truck_weights:
#         # 1번 케이스: 1초 뒤에 다리 위에 트럭이 추가되는 경우
#         if bridge_weight + truck_weights[0] <= weight:
#             # 1초가 지나며
#             total_time += 1
#             # 다리 위의 나머지 트럭들에서는 시간이 1초만큼 지나감
#             for truck in truck_bridge:
#                 truck[1] -= 1
#                 # 다리를 지난 트럭은 제거
#                 if truck[1] == 0:
#                     passed_truck = truck_bridge.pop(0)
#                     bridge_weight -= passed_truck[0]
#         # 2번 케이스: 1초 뒤에 다리 위에 트럭이 추가되지 않는 경우
#         else:
#             # 가장 앞 트럭이 다리를 지나가기까지 남은 시간만큼 추가되며
#             passed_truck = truck_bridge.pop(0)
#             total_time += passed_truck[1]
#             bridge_weight -= passed_truck[0]
#             # 다리 위의 나머지 트럭들에서는 시간이 그만큼 지나감
#             for truck in truck_bridge:
#                 truck[1] -= passed_truck[1]
#         # 공통: 다음 트럭이 다리 위에 올라옴
#         if bridge_weight + truck_weights[0] <= weight:
#             added_truck = truck_weights.pop(0)
#             truck_bridge += [[added_truck, bridge_length]]
#             bridge_weight += added_truck
#         # print(f"현재 시간: {total_time}, 다리 위 트럭: {truck_bridge}, 다리 위 무게: {bridge_weight}")
    
#     total_time += truck_bridge[-1][1]
        
#     return total_time
        

# 테스트 케이스
if __name__ == "__main__":
    bridge_length_list = [2, 100, 100]
    weight_list = [10, 100, 100]
    truck_weights_list = [[7, 4, 5, 6], [10], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
    for bridge_length, weight, truck_weights in zip(bridge_length_list, weight_list, truck_weights_list):
        result = solution(bridge_length, weight, truck_weights)
        print(result)