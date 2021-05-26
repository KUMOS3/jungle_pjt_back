import requests
import json
from tmdb import URLMaker
from pprintpp import pprint

# API key
my_key = '3f1c187d77531562ac88a15e481a6b98'

def recommendation(title):
    k1 = URLMaker('3772d6f699613e0eeb91c055ec835a35')
    movie_id = k1.movie_id(title)
    if movie_id:
        re_info = k1.get_url('movie', f'{movie_id}/recommendations', region='KR', language='ko')
        res = requests.get(re_info)
        b = res.json()
        m_lst = b.get('results')
        titles = []
        for i in range(len(m_lst)):
            titles.append(m_lst[i].get('title'))

        return titles
    return None

if __name__ == '__main__':

    genre_path = "../fixtures/movies/genredb_original.json"

    genredb = []
    with open(genre_path, "r") as json_file:
        genredb = json.load(json_file)

    data = []
    # popular 영화 평점순 5개 출력
    for title in range(1, 3):
        data += recommendation(title)

    # 장르 구조 만들기, 아직 mtom필드인 movies는 작성되지 않았음.
    genres = []
    for g in genredb:
        genre = {}
        genre["pk"] = g["id"]
        genre["model"] = "movies.genre"

        fields = {}
        fields["name"] = g["name"]
        fields["movies"] = []
        # fields["favorite_users"] = []

        genre["fields"] = fields
        genres.append(genre)

    # 영화 구조 만들기
    movies = []
    for d in range(len(data)):

        movie_title = data[d]

        movies.append(movie_title)


    #1. 인코딩 안된 것 (원본, 데이터 추가시 사용)

    # 2. 인코딩 된 것. 실제 서버의 데이터로 사용
    file_path2 = "../fixtures/movies/recommend_title.json"
    with open(file_path2, 'w', encoding='UTF-8') as outfile:
        json.dump(movies, outfile, indent=4, ensure_ascii=False)





