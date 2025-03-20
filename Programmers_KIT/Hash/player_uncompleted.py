def solution(participant, completion):
    part_dict = {}
    
    for part in participant:
        part_dict[part] = part_dict.get(part, 0) + 1
        
    for comp in completion:
        part_dict[comp] -= 1
        
    for name, count in part_dict.items():
        if count > 0:
            return name

# 테스트할 케이스들
if __name__ == "__main__":
    participant_list = [["leo", "kiki", "eden"], ["marina", "josipa", "nikola", "vinko", "filipa"], ["mislav", "stanko", "mislav", "ana"]]
    completion_list = [["eden", "kiki"], ["josipa", "filipa", "marina", "nikola"], ["stanko", "ana", "mislav"]]
    for participant, completion in zip(participant_list, completion_list):
        result = solution(participant, completion)
        print(result)