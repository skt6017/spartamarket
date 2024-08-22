# Spartamarket

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
	- Bootsrap
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

### Accounts
- POST /accounts/signup: 새로운 사용자 등록.
- POST /accounts/login: 사용자 로그인.
- POST /accounts/logout : 사용자 로그아웃.
- POST /accounts/profile/<int:pk> : 사용자 프로필 조회
- POST /accounts/profile/<int:pk>/follow : 사용자 프로필 팔로잉 목록에 추가

### Products
- POST /products/create: 상품 등록.
- GET /products: 상품 목록 조회.
- GET /products/<int:pk>: 특정 상품 상세 조회.
- POST /products/<int:pk>/update: 등록한 상품 수정.
- POST /products/<int:pk>/delete: 등록한 상품 삭제.
- POST /products/<int:pk>/like: 특정 상품을 찜 목록에 추가 및 제거
- POST /products/<int:pk>/hashtag: 특정 상품에 해시태그 추가
- POST /products/<int:pk>/hashtag/<int: hashtag_pk>/delete: 특정 상품에 해시태그 제거

## ERD
![Uploading Sparatamarket_ERD.drawio (1).png…]()




## 프로젝트 파일 구조




## Trouble Shooting
