# README

jungle project backend



## movies_movie

- popularity
  - 최근 뜨는 영화 추천에 사용
- is_for_kids
  - 어린이 전용 영화인지 아닌지



## accounts_user

- username(ID)

- password

- nickname

- (email)

- birth_year

  - 선택하게 만들면 좋음 아니면 4자리 숫자 (범위 지정)만 받기
  - 키즈 사용 시

- date_joined

  - 1년 되면 "정글 고인물"

- last_login

  - 2일 연속 출석하면 "정글링에 맛들인"

- favorite_genre

  - 장르를 3개 이상 체크하면 "아무거나 주워먹는"

- (favorite_moive)

- achivement_list

  - 해리포터 : 후플푸프
    - 칭호: "후플푸프 기숙사생"

- achivement_now

  - 지금 고른 칭호

- 좋아요 영화를 누른 영화 리스트

  - 유저 좋아요가 눌러져있으면 모달 평가 아이콘 변경해주기

  - 좋아요에 있는 영화를 별로에요를 누르면 좋아요 리스트에서 빼줘야 함

- 별로에요를 누른 영화 리스트

- 좋아요 누르고 리뷰남기고 코멘트 달면 "정글을 알아가는"

- F12를 누르면 함수 발생 -> "개발자인가봐"

  - 모달: "어머어머 개발자인가봐 고생이 많으세요 칭호를 드립니다"

## community_review

- id
- title
- movie_title
- movie_rate
  - 반영되도록 함
  - 별점에 따라 vue에서의 리뷰 색이 바뀜
    - 빨강 연한빨강 회색 연한 초록 초록





### community_review_like

- user랑 연결 - 좋아요 5개 이상 누르면 "사랑이 많은"

- vote_count= -6115

  vote_average= -21378

  popularity= 31880

  movie_like_users= [ 31 ]

  - 투표수가 높은 영화를 3개 이상 누르면 "내로라하는 영화는 섭렵한"
  - 평점수가 높은 영화를 3개 이상 누르면 "영화계의 미식가"
  - 인기도, 유행도가 높은 영화를 3개 이상 누르면 "오 좀 유행을 아는 놈인가"
  - 이 영화를 처음 좋아하는 사람이라면 "당신은 이 영화의 트레져헌터"
  - 처음 리뷰남기고 좋아요 누르는 사람 선착순 100명 보석주는것도 재밌겠다.



### movies_movie_wish

- 찜하기, wishlist기능





추후 기능에 따라 추가되어야 할 모델 혹은 백엔드내용

- 영화 추천 기능
  - django에서 view함수로 해결
  - 랜덤, 영신's pick, 장르, 나라

- (모델X)난이도 높은 영화 클리어 기능
  - Movies_movie에 난이도레벨이 들어가야
  - 혹은 모델링 없이 임의로 django에 난이도높은 리스트를 만들어둠
- (모델X)나 몇개 기록했다
- (모델X)업적 내용 보여주는 기록
  - 업적
    - "너 정글링이 뭔 지 알아?" => 정글링 좀 해본
  - vue에서 state만들어서 활용, django에서 업적 주는 내용과 같도록 유의해야

- (모델O)검색 기능
  - 좋아하는 영화 등록 가능하도록 accounts_user에 favorite_movie 추가
  - 회원가입시 검색기능, 프로파일에서 변경 기능(에바) 추가
- 출석체크
  - accounts_user에 daily_check_list추가
    - 처음에 none, 2021년 5월 19일에 출석하면 `2021-05-19`추가
    - 2일 연속 출석하면 "또 오셨군요"
    - 5일 연속 출석하면 "정글링에 푹 빠진"
    - 출석체크탭에서 보여주기(와 개어렵겠다)

- 예고편 => vue

- 프로필에서는 평점별로 모아 볼 수 있게 하고, 다른 사람의 것도 볼 수 있게 한다

  - ... 추후 고민

- 타 사용자의 5점 기반으로 유사한 영화(당신이 좋아할 확률이 높은 영화)도 보여줄 수 있다

  - 나만의 평점리스트
    - 내가 5점 준 영화 정렬
    - 다른 사람이 5점 준 영화
    - 이 영화를 5점 준 사람이 또 5점 준 영화를 추천
  - ... 추후 고민

- #### 누적 기록

  - 페이지 맨 하단 '총 n개의 평가가 쌓였어요'
  - 리뷰 개수를 세서 getters로 반환



