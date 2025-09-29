def solution(genres, plays):
    genre_dict = {}
    genre_play_dict = {}
    answer = []
    
    # 장르별 재생 횟수 딕셔너리 생성 ({'classic': 1450, 'pop': 3100})
    for i in range(len(genres)):
        genre_dict[genres[i]] = genre_dict.get(genres[i], 0) + plays[i]
        
    # 재생 횟수 기준 내림차순으로 정렬 (['pop', 'classic'])
    sorted_genres = [k for k, v in sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)]
    
    # 장르별 재생 횟수와 인덱스 저장 ({'pop': [[600, 1], [2500, 4]], 'classic': [[500, 0], [150, 2], [800, 3]]})
    for genre in sorted_genres:
        for i in range(len(genres)):
            if genres[i] == genre:
                genre_play_dict[genres[i]] = genre_play_dict.get(genres[i], []) + [[plays[i], i]]
    
    # 장르별로 재생 횟수 내림차순으로 정렬하고, 인덱스 오름차순으로 정렬 ({'pop': [[2500, 4], [600, 1]], 'classic': [[800, 3], [500, 0], [150, 2]]})
    for genre_play in genre_play_dict.values():
        sorted_genre_plays = sorted(genre_play, key=lambda x: (-x[0], x[1]))
        # 상위 2개의 곡만 인덱스 추출
        for i in range(min(len(sorted_genre_plays), 2)):
            answer.append(sorted_genre_plays[i][1])
            
    return answer
            
# 테스트할 케이스들
if __name__ == "__main__":
    genres_list = [["classic", "pop", "classic", "classic", "pop"]]
    plays_list = [[500, 600, 150, 800, 2500]]
    for genres, plays in zip(genres_list, plays_list):
        result = solution(genres, plays)
        print(result)