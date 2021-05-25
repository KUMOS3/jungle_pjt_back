import requests
import json
from tmdb import URLMaker
from pprintpp import pprint

# API key
my_key = '3f1c187d77531562ac88a15e481a6b98'

def ranking(i):
    # URLMaker 클래스의 인스턴스인 url을 만든다.
    url = URLMaker(my_key)

    # url = url.get_url(language='ko-KR') # 장르
    url = url.get_url(region='KR', language='ko', page=i)
    # URLMaker 클래스의 get_url 메서드를 사용하며, 가변인자(k:v)로 지역과 언어를 설정한다.
    print(url)
    # requests 모듈을 이용해 url에 해당하는 데이터를 요청하기위해 .get()메서드를 사용한다.
    r = requests.get(url)
    # json파일로 변환한다.
    movie_jason = r.json()
    # json파일로 변환된 파일에서 key가 result인 value를 리스트로 가져온다.
    # movie_list = movie_jason.get('genres') # 장르
    movie_list = movie_jason.get('results')
    return movie_list


    # # 변수 선언
    # movie_title_and_vote_dict = {} # k : v = 평점 : 제목을 넣을 dict 변수 생성
    # vote_movies = [] # 평점 내림차순으로 정렬된 (평점, 제목) 형태의 set을 담을 list 변수 생성
    # vote_highest_movies_info = [] # 평점 내림차순으로 상위 5개의 (평점, 제목) 형태의 set을 담을 list 변수 생성

    # # movie_list의 모든 영화정보를 순회
    # for movie_info in movie_list:
    #     # k : v = 평점 : 제목을 저장
    #     movie_title_and_vote_dict[movie_info.get('vote_average')] = movie_info.get('title')
    #     # 딕셔너리의 키값을 기준으로 정렬하기 위해 함수를 생성
    #     def f1(x):
    #         return x[0]
    #     # 딕셔너리의 경우, 딕셔너리에서 sort를 제공하지 않으므로 내장함수인 sorted()를 사용해야
    #     # dict
    #     vote_movies = sorted(movie_title_and_vote_dict.items(),key=f1,reverse=True)
    #     # 평점 내림차순으로 상위 5개를 슬라이싱하여 저장
    #     vote_highest_movies=vote_movies[:5]
        
    # # 리스트 안의 각 (평점, 제목) 형태의 set에 대하여
    # for vote_highest_movie_set in vote_highest_movies:
    #     # 영화 정보 리스트의 각 영화 정보 dict에 대하여
    #     for movie in movie_list:
    #         # set[1], 즉 제목과 영화 정보 dict에 있는 제목이 같을 경우 
    #         if vote_highest_movie_set[1] == movie.get('title'):
    #             # 해당 영화정보 dict를 리스트에 추가 
    #             vote_highest_movies_info.append(movie)
    # # 결과 반환
    # return vote_highest_movies_info
    

if __name__ == '__main__':

    genre_path = "./fixtures/movies/genredb_original.json"

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

    # for genre in genres:
    #     genre["fields"]["movies"] = JSON.parse(genre["fields"]["movies"])
    # data = ranking() # 장르

    # pprint(data)

    # !!!!!!!!!!!!! 꼭 두개 다 해놔야 함 !!!!!!!!!!!!!!!!!!!

    #1. 인코딩 안된 것 (원본, 데이터 추가시 사용)
    file_path = "./fixtures/movies/moviedb_original.json"
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    # 2. 인코딩 된 것. 실제 서버의 데이터로 사용
    file_path2 = "./fixtures/movies/moviedb_encoded.json"
    with open(file_path2, 'w', encoding='UTF-8') as outfile:
        json.dump(movies, outfile, indent=4, ensure_ascii=False)

    file_path3 = "./fixtures/movies/genredb.json" # 장르
    with open(file_path3, 'w', encoding='UTF-8') as outfile:
        json.dump(genres, outfile, indent=4, ensure_ascii=False)




