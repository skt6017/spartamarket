# Spartamarket

## 📖 목차
1. [프로젝트 소개](#프로젝트-소개)
2. [팀소개](#팀소개)
3. [프로젝트 계기](#프로젝트-계기)
4. [주요기능](#주요기능)
5. [개발기간](#개발기간)
6. [기술스택](#기술스택)
7. [서비스 구조](#서비스-구조)
8. [와이어프레임](#와이어프레임)
9. [API 명세서](#API-명세서)
10. [ERD](#ERD)
11. [프로젝트 파일 구조](#프로젝트-파일-구조)
12. [Trouble Shooting](#trouble-shooting)
    
## 👨‍🏫 프로젝트 소개
스파르타코딩클럽의 팀 프로젝트로 개발된 중고거래 플랫폼입니다.
사용자는 회원 가입 후, 자신의 물건을 등록하고 다른 사용자가 등록한 물건을 찜할 수 있습니다.

## 팀소개
서경태 - 팀장  
김한규 - 서기  
김채림  
박현진

## 프로젝트 계기
중고거래 시장의 급격한 성장과 더불어, 사용자들에게 안전하고 편리한 거래 환경을 제공하기 위함입니다.
특히, 기존 중고거래 플랫폼에서 발생하는 사기 및 안전 문제를 해결하고, 더욱 직관적이고 간편한 사용자 경험을 제공하기 위해 Sparta Market을 기획하게 되었습니다.
팀원들은 이러한 문제를 해결하고, 신뢰할 수 있는 중고거래 플랫폼을 만들고자 이 프로젝트를 시작했습니다.

## 💜 주요기능

- 회원 가입 / 로그인 : 유저는 회원가입을 통해 플랫폼에 가입할 수 있으며, 로그인 후 서비스를 이용할 수 있습니다.

- 유저 프로필 : 유저는 자신의 프로필 페이지에서 등록한 물품 및 찜한 물품을 확인할 수 있습니다.

- 팔로잉 : 다른 유저를 팔로우할 수 있습니다.

- 판매할 물건 업로드 : 유저는 자신의 중고 물품을 등록하고 관리할 수 있습니다.

- 찜하기 : 마음에 드는 물품을 찜하여 나중에 확인할 수 있습니다.

- 해시태그 : 설정된 해시태그로 물건 목록 혹은 상세페이지에 노출할 수 있습니다.


## ⏲️ 개발기간
- 2024.08.21(수) ~ 2024.08.28(수)

## 📚️ 기술스택
- 프론트엔드(Frontend)
	- HTML/CSS
	- Bootstrap
	- JavaScript

- 백엔드(Backend) 
    - Python
    - Django

- 데이터베이스(Database)
  	- SQLite

- 기타 도구 및 라이브러리
  	- Git/GitHub
  	- django-extensions

### ✔️ Language
- Python: 백엔드 로직, 데이터 처리 및 API 개발을 위한 언어.
- JavaScript: 클라이언트 사이드 스크립트 및 상호작용을 위한 언어.
- SQL: 데이터베이스 쿼리 및 관리에 사용.
  
### ✔️ Version Control
- Git: 소스 코드 버전 관리 시스템. 프로젝트의 버전 기록을 유지하고 협업을 지원함.
- GitHub: 원격 저장소 호스팅 서비스, 코드 리뷰 및 협업을 지원.

### ✔️ IDE
- Visual Studio Code: Python, JavaScript, HTML/CSS의 개발을 위한 통합 개발 환경. 확장성 높은 플러그인 시스템 지원.
  
### ✔️ Framework
- Django: Python 기반의 웹 프레임워크, 모델-뷰-템플릿(MVT) 패턴을 사용하여 효율적인 웹 애플리케이션 개발.
- Bootstrap: CSS 프레임워크로, 반응형 디자인과 빠른 스타일링을 지원.
- FontAwesome: 아이콘 라이브러리, 사용자 인터페이스 디자인에 도움을 줌.

### ✔️  DBMS
- SQLite: 가벼운 관계형 데이터베이스 관리 시스템. 파일 기반의 데이터베이스로, 설정과 유지 관리가 간편하며, 로컬 개발과 작은 규모의 배포에 적합.
  
## 서비스 구조
- 프론트엔드: 사용자 인터페이스와 사용자 경험을 제공.
- 백엔드: 데이터 처리, 비즈니스 로직 및 API를 처리.
- 데이터베이스: SQLite를 사용하여 사용자 및 상품 데이터를 저장 및 관리.
- API: 프론트엔드와 백엔드 간의 데이터 교환을 처리.

## 와이어프레임
- 홈페이지: 주요 기능 및 회원 가입/로그인 버튼 제공.
- 상품 목록 페이지: 등록된 상품 목록 및 검색 기능 제공.
- 상품 상세 페이지: 상품 세부 정보와 찜하기 버튼 제공.
- 회원 대시보드: 사용자 프로필, 등록한 상품 관리, 찜한 상품 보기.

## API 명세서

### Accounts API

1. 로그인 (Login)
- Method: `POST`
- Endpoint: `/accounts/login/`
- Params: `username`, `password`

2. 로그아웃 (Logout)
- Method: `POST`
- Endpoint: `/accounts/logout/`

3. 회원가입 (Signup)
- Method: `POST`
- Endpoint: `/accounts/signup/`
- Params: `username`, `password1`, `password2`, `email`, `first_name`, `last_name`, `image` (optional)

4. 프로필 수정 (Update Profile)
- Method: `POST`
- Endpoint: `/accounts/update/`
- Params: `username`, `email`, `first_name`, `last_name`, `image` (optional)

5. 비밀번호 변경 (Change Password)
- Method: `POST`
- Endpoint: `/accounts/change_password/`
- Params: `old_password`, `new_password1`, `new_password2`

6. 계정 삭제 (Delete Account)
- Method: `POST`
- Endpoint: `/accounts/delete/`


### Products API

1. 상품 목록 조회 (Products List)
- Method: `GET`
- Endpoint: `/products/`
- Params: `sort` (optional, default: `-view_count`)

2. 상품 상세 조회 (Product Detail)
- Method: `GET`
- Endpoint: `/products/<int:pk>/`

3. 상품 생성 (Create Product)
- Method: `POST`
- Endpoint: `/products/create/`
- Params: `title`, `content`, `image` (optional), `new_hashtags` (optional)

4. 상품 수정 (Update Product)
- Method: `POST`
- Endpoint: `/products/<int:pk>/update/`
- Params: `title`, `content`, `image` (optional), `new_hashtags` (optional)

5. 상품 삭제 (Delete Product)
- Method: `POST`
- Endpoint: `/products/<int:pk>/delete/`

6. 상품 좋아요 (Like Product)
- Method: `POST`
- Endpoint: `/products/<int:pk>/like/`

7. 해시태그로 상품 조회 (Products by Hashtag)
- Method: `GET`
- Endpoint: `/products/<int:hashtag_pk>/hashtag/`

8. 상품 검색 (Search Products)
- Method: `POST`
- Endpoint: `/products/search/`
- Params: `searched`


### Users API

1. 사용자 목록 조회 (Users List)
- Method: `GET`
- Endpoint: `/users/`

2. 사용자 프로필 조회 (Profile Detail)
- Method: `GET`
- Endpoint: `/users/profile/<str:username>/`

3. 사용자 팔로우/언팔로우 (Follow/Unfollow User)
- Method: `POST`
- Endpoint: `/users/<int:user_pk>/follow/`



## ERD
![Sparatamarket_ERD drawio](https://github.com/user-attachments/assets/b4e5a89f-492b-4bea-b672-6e2bbbef02ef)




## 프로젝트 파일 구조

```plaintext
SpartaMarket/
├── accounts/               # 사용자 계정 관련 앱
│   └── *                   # 앱 관련 파일들 (admin.py, models.py, views.py 등)
├── media/                  # 미디어 파일 저장소
├── products/               # 제품 관련 앱
│   └── *                   # 앱 관련 파일들 (admin.py, models.py, views.py 등)
├── templates/              # 템플릿 파일들 (HTML 등)
├── static/                 # 정적 파일들 (CSS, 이미지 등)
├── spartamarket/           # 프로젝트 설정 디렉터리
│   ├── settings.py         # 프로젝트 설정 파일
│   ├── urls.py             # 전역 URL 패턴 정의
├── users/                  # 사용자 관련 앱
│   └── *                   # 앱 관련 파일들 (admin.py, models.py, views.py 등)
├── manage.py               # Django 관리 커맨드 파일
└── README.md               # 프로젝트 설명서
