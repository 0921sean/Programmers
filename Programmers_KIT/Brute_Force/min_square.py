def solution(sizes):
    max_list = []
    min_list = []
    for size in sizes:
        max_list.append(max(size[0], size[1]))
        min_list.append(min(size[0], size[1]))
        
    return max(max_list) * max(min_list)

# 테스트할 케이스들
if __name__ == "__main__":
    sizes_list = [[[60, 50], [30, 70], [60, 30], [80, 40]], [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]], [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]]
    for sizes in sizes_list:
        result = solution(sizes)
        print(result)