### 쿠버네티스 구동
minkube start

### 배포
redis-deplyment.yaml 

### 매니페스타 파일 적용
k apply -f redis-deployment.yaml

### Redis 배포 확인
k get pods
k get svc

### Redis 접속
k exec -it <redis-pod-name> -- redis-cli

### 1번 데이터 베이스 선택
SELECT 1

### 키-값 설정
SET myKey "Hello, Redis"

### 값 가져오기
GET myKey

### python 애프리케이션 작성
counter.py

### python 도커파일 작성
Dockerfile

### python 애플리케이션을 Docker 이미지로 빌드
docker build -t my-redis-counter

### Docker Hub에 로그인
docker login -u pia22

### Docker 이미지를 쿠버네티스 클러스터에 배포
docker tag my-redis-counter pia222/my-redis-counter

docker push pia222/my-redis-counter


