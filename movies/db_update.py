import requests
import json
from tmdb import URLMaker
from pprintpp import pprint

# API key
my_key = '3f1c187d77531562ac88a15e481a6b98'

def ranking(i):
    # URLMaker 클래스의 인스턴스인 url을 만든다.
    url = URLMaker(my_key)

    url = url.get_url(region='KR', language='ko', page=i)
    # URLMaker 클래스의 get_url 메서드를 사용하며, 가변인자(k:v)로 지역과 언어를 설정한다.
    
    # requests 모듈을 이용해 url에 해당하는 데이터를 요청하기위해 .get()메서드를 사용한다.
    r = requests.get(url)
    # json파일로 변환한다.
    movie_jason = r.json()
    
    # json파일로 변환된 파일에서 key가 result인 value를 리스트로 가져온다.
    movie_list = movie_jason.get('results')

    return movie_list


if __name__ == '__main__':

    file_path = "./fixtures/movies/moviedb_original.json"

    data = []
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    # 데이터 추가 로직 작성
    data += ranking(6)

    # pprint(data)

    # !!!!!!!!!!!!! 꼭 두개 다 해놔야 함 !!!!!!!!!!!!!!!!!!!

    # !!!!!!!!!!!!! 꼭 두개 다 해놔야 함 !!!!!!!!!!!!!!!!!!!

    # 1. 인코딩 안된 것 (원본, 데이터 추가시 사용)
    file_path = "./fixtures/movies/moviedb_original.json"
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    # 2. 인코딩 된 것. 실제 서버의 데이터로 사용
    file_path2 = "./fixtures/movies/moviedb_encoded.json"
    with open(file_path2, 'w', encoding='UTF-8-sig') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)