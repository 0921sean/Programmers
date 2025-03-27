def solution(participant, completion):
    player_dict = {}
    
    for part in participant:
        player_dict[part] = player_dict.get(part, 0) + 1
    for comp in completion:
        player_dict[comp] -= 1
    
    for key, value in player_dict.items():
        if value == 1:
            return key

# 테스트할 케이스들
if __name__ == "__main__":
    participant_list = [["leo", "kiki", "eden"], ["marina", "josipa", "nikola", "vinko", "filipa"], ["mislav", "stanko", "mislav", "ana"]]
    completion_list = [["eden", "kiki"], ["josipa", "filipa", "marina", "nikola"], ["stanko", "ana", "mislav"]]
    for participant, completion in zip(participant_list, completion_list):
        result = solution(participant, completion)
        print(result)