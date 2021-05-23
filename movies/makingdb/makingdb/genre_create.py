import requests
import json
from tmdb import URLMaker
from pprintpp import pprint

# API key
my_key = '3f1c187d77531562ac88a15e481a6b98'

def ranking():
    # URLMaker 클래스의 인스턴스인 url을 만든다.
    url = URLMaker(my_key)

    url = url.get_url(language='ko-KR') # 장르
    # URLMaker 클래스의 get_url 메서드를 사용하며, 가변인자(k:v)로 지역과 언어를 설정한다.
    
    # requests 모듈을 이용해 url에 해당하는 데이터를 요청하기위해 .get()메서드를 사용한다.
    r = requests.get(url)
    # json파일로 변환한다.
    genre_json = r.json()

    # json파일로 변환된 파일에서 key가 result인 value를 리스트로 가져온다.
    genre_list = genre_json.get('genres') # 장르

    return genre_list


# !!! 실행 전 tmdb내용 장르로 바꿔줘야
if __name__ == '__main__':
    
    data = ranking()

    #1. 인코딩 안된 것 (원본, 데이터 추가시 사용)
    file_path = "movies/fixtures/movies/genredb_original.json"
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    # 2. 인코딩 된 것. 실제 서버의 데이터로 사용
    file_path2 = "movies/fixtures/movies/genredb.json" # 장르
    with open(file_path2, 'w', encoding='UTF-8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)




