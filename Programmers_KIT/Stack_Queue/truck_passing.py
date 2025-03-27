from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0    # 경과 시간
    bridge = deque([0] * bridge_length) # 다리 위의 상태
    bridge_weight = 0   # 현재 다리 위 트럭 무게 합
    truck_weights = deque(truck_weights) # 대기 트럭
    
    # 대기 트럭 없고 다리 위에도 트럭이 없을 때까지 확인
    while bridge:
        time += 1
        
        bridge_weight -= bridge.popleft()
        
        if truck_weights and bridge_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            bridge_weight += truck
        else:
            bridge.append(0)
            
    return time

# 테스트 케이스
if __name__ == "__main__":
    bridge_length_list = [2, 100, 100]
    weight_list = [10, 100, 100]
    truck_weights_list = [[7, 4, 5, 6], [10], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
    for bridge_length, weight, truck_weights in zip(bridge_length_list, weight_list, truck_weights_list):
        result = solution(bridge_length, weight, truck_weights)
        print(result)