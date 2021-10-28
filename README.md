- 환경설정은 python 3.7 버전에 django-rest-framework 최신 버전 사용 및 추가로 사용한 패키지는 requirements.txt에 기재됨

완료사항

- 질문을 데이터베이스에 저장, 수정, 삭제하는 API 개발

  - URL : /board/
  - Method : POST, PATCH, DELETE
  - URL Params : PATCH, DELETE시 Required=id[int]
  - Request Header : Authorization : Bearer jwt토큰해시값
  - Sample Call  
     curl --location --request GET 'http://localhost:8000/board/' \
     --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1NDQ2MzAwLCJpYXQiOjE2MzU0MzEzOTMsImp0aSI6IjI1ODU0YzQ2N2Q1NDRjNDdiYTRmODRmY2YxNjUyZjMxIiwidXNlcl9pZCI6Mn0.QIKU5eAVC-ASPNMRKUuy46lsXdXrT_CQD5NaA_rRi5c'
  - Success Response: status=200, {"count":1,"next":null,"previous":null,"results":[{"id":1, "title":"testing","context":"sadfsadfsadfsdaf","created_at":"2021-10-29T00:47:49.801348+09:00","modified_at":"2021-10-29T00:47:49.801829+09:00","user":2}]}
  - Error Response : drf 기본 에러 리스폰스

- 질문의 댓글을 데이터베이스에 저장하는 API 개발

  - URL : /comment/
  - Method : POST
  - URL Params : 없음
  - Request Header : Authorization : Bearer jwt토큰해시값
  - Sample Call  
     curl --location --request POST 'http://localhost:8000/comment/' \
     --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1NDM4NTkzLCJpYXQiOjE2MzU0MzEzOTMsImp0aSI6IjlhNGM4ZmJmYzUyZjRjMWI4NTczMWIxZDRjODZmODFiIiwidXNlcl9pZCI6Mn0.\_vMtSL5SYaFQQBmXTjOsLV7kAZ6tDsHPiejBu-CV2kQ' \
     --header 'Content-Type: application/json' \
     --data-raw '{
    "context" : "6574567456745",
    "board" : 1
    }'
  - Success Response: status=200 ,{"context" : "@34234", "board":2 ...}
  - Error Response : drf 기본 에러 리스폰스

- 질문에 달린 댓글 목록을 출력하는 API 개발

  - URL : /board/
  - Method : GET
  - URL Params : Required=id[int]
  - Request Header : Authorization : Bearer jwt토큰해시값
  - Sample Call  
     curl --location --request GET 'http://localhost:8000/board/1/' \
     --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1NDQ2MzAwLCJpYXQiOjE2MzU0MzEzOTMsImp0aSI6IjI1ODU0YzQ2N2Q1NDRjNDdiYTRmODRmY2YxNjUyZjMxIiwidXNlcl9pZCI6Mn0.QIKU5eAVC-ASPNMRKUuy46lsXdXrT_CQD5NaA_rRi5c'
  - Success Response: {
    "comment_in_board": [
    {
    "id": 1,
    "context": "eeeeeee",
    "created_at": "2021-10-29T00:56:09.052615+09:00",
    "modified_at": "2021-10-29T00:56:09.052794+09:00",
    "user": 2,
    "board": 1
    },
    {
    "id": 2,
    "context": "6574567456745",
    "created_at": "2021-10-29T01:27:09.392048+09:00",
    "modified_at": "2021-10-29T01:27:09.392223+09:00",
    "user": 2,
    "board": 1
    }
    ]
    }
  - Error Response : drf 기본 에러 리스폰스

- 키워드로 질문의 제목 또는 본문내용을 검색하는 API 개발

  - URL : /board/
  - Method : GET
  - URL Params : Required=?context, ?title - 검색하고자 하는 내용 혹은 제목
  - Request Header : Authorization : Bearer jwt토큰해시값
  - Sample Call  
     curl --location --request GET 'http://localhost:8000/board/?context=df' \
     --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1NDQ2MzAwLCJpYXQiOjE2MzU0MzEzOTMsImp0aSI6IjI1ODU0YzQ2N2Q1NDRjNDdiYTRmODRmY2YxNjUyZjMxIiwidXNlcl9pZCI6Mn0.QIKU5eAVC-ASPNMRKUuy46lsXdXrT_CQD5NaA_rRi5c'
  - Success Response: {"count":1,"next":null,"previous":null,"results":[{"id":1, "title":"testing","context":"sadfsadfsadfsdaf","created_at":"2021-10-29T00:47:49.801348+09:00","modified_at":"2021-10-29T00:47:49.801829+09:00","user":2}]}
  - Error Response : drf 기본 에러 리스폰스

- 질문 작성일 기준 각 월별 전체 질문 중에서 가장 좋아요가 많은 질문을 출력하는 API 개발
  - URL : /board/monthly_reaction
  - Method : GET
  - URL Params : Required - month - 검색하고자하는 달(월단위)
  - Request Header : Authorization : Bearer jwt토큰해시값
  - Sample Call  
     curl --location --request GET 'http://localhost:8000/board/monthly_reaction/?month=2021-10' \
     --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1NDQ2MzAwLCJpYXQiOjE2MzU0MzEzOTMsImp0aSI6IjI1ODU0YzQ2N2Q1NDRjNDdiYTRmODRmY2YxNjUyZjMxIiwidXNlcl9pZCI6Mn0.QIKU5eAVC-ASPNMRKUuy46lsXdXrT_CQD5NaA_rRi5c'
  - Success Response: {
    "results": {
    "id": 1,
    "title": "testing",
    "context": "sadfsadfsadfsdaf",
    "created_at": "2021-10-29T00:47:49.801348+09:00",
    "modified_at": "2021-10-29T00:47:49.801829+09:00",
    "user": 2
    }
    }
  - Error Response : drf 기본 에러 리스폰스

선택사항 개발

- signup 계정생성 API
  - URL : /user/registration/
- signin 로그인 API
  - URL : /user/login
- refresh 토큰 재발급 API
  - URL : /user/token/refresh/
