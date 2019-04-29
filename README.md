앱 네임이 movie입니다..
하지만 url요청은 movies입니다..

# 08_Django-seed data

### 1. 목표

- 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작
- Seed Data를 활용한 DB설계
- Django Form을 통해 입력받은 데이터 유효성 검증



### 2. 준비사항

- Django
- Python



### 3. 요구사항

- Seed Data 반영
- 영화 생성
  - 접근 URL : `movies/new/`
  - 검증을 통해 유효한 경우 데이터베이스에 저장 후 list페이지로 redirect
- 영화 수정
  - 접근 URL : `movies/<int:id>/edit/`
  - 검증을 통해 유효한 경우 데이터베이스에 저장 후 영화 정보 조회 페이지로 redirect
- 평점 생성
  - 접근 URL : `movies/<int:id>/scores/new/`
  - 영화 정보 조회 페이지에서 form을 통해 평점 작성 가능
  - 검증을 통해 유효한 경우 데이터베이스에 저장 후 영화 정보 조회 페이지로 redirect