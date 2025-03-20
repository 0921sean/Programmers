def solution(sizes):
    max_x = 0
    max_y = 0
    
    for size in sizes:
        x, y = size
        if x >= y:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        else:
            max_x = max(max_x, y)
            max_y = max(max_y, x)
            
    return max_x * max_y

# 테스트할 케이스들
if __name__ == "__main__":
    sizes_list = [[[60, 50], [30, 70], [60, 30], [80, 40]], [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]], [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]]
    for sizes in sizes_list:
        result = solution(sizes)
        print(result)