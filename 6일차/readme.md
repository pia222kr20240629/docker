# 윈도우 <- > 가상머신 간의 파일 전송  윈도우 commnad 창에서 실시
  ### 가상머신 ->  현재 경로의 윈도우로 모든 파일 전송  반대는 반대로 명령어를 입력한다.
  - scp root@192.168.150.37:/home/rocky/secret/* ./

### mkdir secret
### cd secret
### vi username.txt
  - admin
### vi password.txt
  - 1q2w3e4r
### secret 생성
  - kubectl create secret generic db-user-pass --from-file=./username.txt --from-file=./password.txt
### secret 상세조회
  - kubectl descrive secret/db-user-pass
### yaml 형태로 조회
  - kubectl get secret/db-user-pass -o yaml
### base64 인코딩 된 정보를 디코딩
  - echo <yaml형태로 조회했을때 인코딩된 문자열> | base64 --decoe
### 설정한 secret을 환경변수로 연결
  - alpine-env.yml 파일 작성
### 환경변수 확인
  - k apply -f alpine-env.yml
  - k exec -it alpine-env -- env

# 실습2
  - echo -n 'admin' | base64
  - echo -n 'password' | base64
### my-secret.yml 
  - k apply -f my-secret.yml
### my-pod.yml 
  - k apply -f my-pod.yml
### pod 로그 확인
  - k get pod
  - k logs my-pod
  - 출력 확인

# openSSL을 이용한 tls 키 생성
### 개인키 tls.key 생성
  - openssl genrsa -out tls.key 2048
### 인증서 서명 요청(CSR) 생성
  - openssl req -new -key tls.key -out tls.csr
### 자체 서명된 인증서(tls.crt)생성
  - openssl x509 -req -in tls.csr -signkey tls.key -out tls.crt -days 365
### base64 인코딩
  - base64 tls.crt > tls.crt.base64
  - base64 tls.key > tls.key.base64
### ssh-secret.yml 파일 생성
  - tls.crt.base64의 파일이 줄 바꿈이 있어서 다음과 같이 yml 파일의 기본 모양을 만든다
  -  echo "tls.crt: $(tr -d '\n' < tls.crt.base64)" > tls-secret.yml
  -  echo "tls.key: $(tr -d '\n' < tls.key.base64)" >> tls-secret.yml
### ssh-secret.yml 배포
  - k apply -f tls-secret.yml
  - k apply -f my-service.yml
  - k apply -f tls-ingress.yml
  - k apply -f my-appp.yml
  - k port-forward service/my-service 8080:80
  - http://localhost:8080 접속해서 확인


