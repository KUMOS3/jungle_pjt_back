import requests
import json
from tmdb import URLMaker
from pprintpp import pprint

# API key
my_key = '3f1c187d77531562ac88a15e481a6b98'

def ranking(i):
    # URLMaker class의 get_url 함수에서 API키값을 더하고,
    url = URLMaker('3772d6f699613e0eeb91c055ec835a35')
    # 원하는 정보주소에 맞게 매개변수를 지정해서 key와value를 쌍으로 가져온다.
    movie = url.get_url('movie', 'popular')
     # 원하는 정보를 받아서 json파일을 읽을 수 있게 저장한다.
    res = requests.get(movie)
    read_res = res.json()
    # 'results'에 해당하는 value값을 저장한다.
    movie_lst = read_res.get('results')
    # 평점들을 담을 리스트 정의
    genre_lst = []
    # 최종 결과를 담을 리스트 정의
    final = []
    # 영화리스트의 길이만큼 반복한다.
    for i in range(len(movie_lst)):
        # 'vote_average' 의 value 값을 저장해서 avgs리스트에 더한다.
        genre_lst.append(movie_lst[i].get('genre_ids'))     


    for i in range(len(genre_lst)):
        for j in range(len(genre_lst[i])):
            if genre_lst[i][j] == 27:
                final.append(movie_lst[i])
    return final

if __name__ == '__main__':

    genre_path = "../fixtures/movies/genredb_original.json"

    genredb = []
    with open(genre_path, "r") as json_file:
        genredb = json.load(json_file)

    data = []
    # popular 영화 평점순 5개 출력
    for i in range(1, 3):
        data += ranking(i)

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
    for d in data:
        movie_id = d.pop("id")

        movie = {}
        movie["pk"] = movie_id
        movie["model"] = "movies.movie"

        fields = {}
        # del d["genre_ids"]
        del d["original_language"]
        del d["video"]
        fields = d
        fields["movie_like_users"] = ""
        fields["movie_dislike_users"] = ""
        fields["movie_wish_users"] = ""

        # 장르 아이디들로 장르모델에 영화 mtom연결하기
        for movie_genre in d["genre_ids"]:
            for genre in genres:
                if genre["pk"] == movie_genre:
                    genre["fields"]["movies"].append(movie_id)

        movie["fields"] = fields
        movies.append(movie)


    #1. 인코딩 안된 것 (원본, 데이터 추가시 사용)

    # 2. 인코딩 된 것. 실제 서버의 데이터로 사용
    file_path2 = "../fixtures/movies/recommend_horror.json"
    with open(file_path2, 'w', encoding='UTF-8') as outfile:
        json.dump(movies, outfile, indent=4, ensure_ascii=False)





