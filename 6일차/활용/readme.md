간단한 flask(스프링 부트, 장고, React.js 등등)를 이용해서  

회원가입

게시판


### 도커 이미지 빌드 및 푸시
  - docker build -t pia222/flask-app:latest .
  - docker push pia222/flask-app:latest

### 쿠버네티스 클러스터 배포
  - k apply -f deployment.yml
  - k apply -f postgres-service.yml

### 도커 컴포즈을 이용한 실행
  - docker-compose up -d
  - docker-compose logs  # 로그확인

### 확인
  - http://localhost:50000
