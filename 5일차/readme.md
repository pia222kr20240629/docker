### 인그래스(ingress)
- 클러스터 외부에서 클러스터 내부의 서비스로 HTTP 및 HTTPS 라우팅을 관리하는 리소스
- 두개의 간단한 Nginx 배포
- 각각의 Nginx 배포를 서비스로 노출
- Ingress 리소스를 사용해서 트래픽을 각각의 서비스로 라우팅


## 1. nginx 배포 설정
- 두개의 nginx 배포설정
- nginx1-deployment.yaml, nginx2-deployment.yaml
- kubectl apply -f nginx1-deployment.yaml
- kubectl apply -f nginx2-deployment.yaml


## 2. 서비스 생성
- nginx1-service.yaml nginx2-service.yaml
- kubectl apply -f nginx1-service.yaml
- kubectl apply -f nginx2-service.yaml

## 3. ingress 리소스 생성
- ingress.yaml
- kubectl apply -f ingress.yaml

## ingress 애드온 활성
- minikube addons enable ingress


## 클러스터 ip 확인
- minikube ip

## 도메인셋팅 
- sudo sh -c 'echo "<minikube ip> example.com" >> /etc/hosts'

## 브라우져 테스트
- http://<minikube ip>/nginx1
- http://<minikube ip>/nginx2


# Volume 만들기
- Pod에 속한 컨터이너간의 디렉터리를 공유하는 방법
- sidecar 패턴
  - 특정(app) 컨터이너에서 생성된 파일을 별도의 컨터이너(sidecar)가 수집
- k apply -f empydir.yaml
- k logs -f sidecar -c sidecar

## hostpath
- 호스트 디렉터리를 컨테이너 디렉터리에 연결하는 방법
- 호스트의 /var/log 디엑터리를 연결해서 내용 확인
- k apply -f hostpath.yaml
- 컨터이너에 접속후 /host/var/log 디렉터리를 확인
- k exec -it host-log --sh
- ls -al /host/var/log  컨터이너의 데이터
- host의 내용과 같아야한다...
- docker ps
- docker exec -it <containerid> /bin/bash
- ls -al /var/log

- 컨테이너에서 파일을 생서하면 host 에서 확인가능
- 컨테이너에 접속을 해서 torch 명령어로 파일을 생성한후에 host에서 확인 가능

  # ConfigMap
  ## ConfigMap 만들기
   - 파일을 통째로 configmap으로 만든다음 컨테이너에서 사용
