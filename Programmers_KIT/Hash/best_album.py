def solution(genres, plays):
    genre_total_plays = {}  # 장르별 총 재생 횟수
    genre_songs = {}        # 장르별 노래 모음
    answer = []
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        # 장르별 총 재생 횟수 계산
        genre_total_plays[genre] = genre_total_plays.get(genre, 0) + play
    
        # 장르별 노래 모음 (인덱스 포함)
        if genre in genre_songs:
            genre_songs[genre].append((i, play))
        else:
            genre_songs[genre] = [(i, play)]
    
    # 재생 횟수 내림차순 정렬
    sorted_genres = sorted(genre_total_plays.keys(), key=lambda x: genre_total_plays[x], \
                           reverse = True)
    
    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    for genre in sorted_genres:
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[1], x[0]))
        
        # 최대 2개까지만 선택
        for i in range(min(2, len(sorted_songs))):
            answer.append(sorted_songs[i][0])
        
    return answer

# 테스트할 케이스들
if __name__ == "__main__":
    genres_list = [["classic", "pop", "classic", "classic", "pop"]]
    plays_list = [[500, 600, 150, 800, 2500]]
    for genres, plays in zip(genres_list, plays_list):
        result = solution(genres, plays)
        print(result)