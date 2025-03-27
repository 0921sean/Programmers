def solution(genres, plays):
    genre_plays = {}
    song_plays = {}
    answer = []
    
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        genre_plays[genre] = genre_plays.get(genre, 0) + play   # 장르별 총 재생 횟수
        
        if genre in song_plays:
            song_plays[genre].append((i, play)) # (인덱스, 노래별 재생 횟수)
        else:
            song_plays[genre] = [(i, play)]
        
    sorted_genres = sorted(genre_plays.keys(), key=lambda x: genre_plays[x], \
                          reverse = True)   # 많이 재생된 장르 순으로 정렬
    
    for genre in sorted_genres:
        sorted_songs = sorted(song_plays[genre], key=lambda x: (-x[1], x[0]))
        
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