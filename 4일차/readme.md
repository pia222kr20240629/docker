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

### 매니패스트 파일을 작성해서 python 어플리캐이션을 배포
counter-deployment.yaml

### 쿠버네티스를 클러스터에 배포
k apply -f counter-deployment.yaml

## 결과확인
k  get pods
k logs <pod name>

-----------------------------------------------------------------------------
### 투표시스템
- vote
- Reids : 개인별 데이터
- worker

   
- postres
- result : node
---------------------------------------------------
- vote result worker 폴더를 각각 만들고
- git을 참고해서 각 폴더에 Dockerfile 및 py 파일을 만들어서 Docker로 이미지화 한다.(허브에 push)
- 쿠버네티스 배포하기전에 k delete <kind명> --all 로 전부 삭제한다. (서비스, 파드 등등)
- 다시 상위 폴더로 나와서  k apply -f vote.yml을 실행해서 쿠버네티스 배포
- k  get pods 해서 에러가 없음을 확인
- minikube ip  ip 정보를 확인
- http:/<minikube ip>/vote  실행하는데.. 이렇게 하면 GET 방식이여서 post맨을 인터넷에서 다운받아서
- 주소는 http:/<minikube ip>/vote  ui에 보면 요청타입을 json으로 레디오 버튼을 클릭하고
- {"vote":"100"}
- 결과는 http:/<minikube ip>/result

