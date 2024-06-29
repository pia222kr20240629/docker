# docker
### 설치
sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo

sudo dnf install docker-ce docker-ce-cli containerd.io

###  도커 자동실행
sudo systemctl start docker
sudo systemctl enable docker


###  사용자 권한
sudo usermod -aG docker $USER
###  권한 적용
newgrp docker

###  도커 동작 확인
docker --version
###  도커를 이용해서 hello-world 이미지를 받아서 컨터이너로 실행후 종료
docker run hello-world

###  도커 상태 확인
###  실행중인 컨테이너 확인
docker ps
###  모든 컨테이너 확인
docker ps -all
###  이미지 확인
docker images


![image](https://github.com/pia222kr20240629/docker/assets/174164680/480d042f-80af-4d21-a891-c223ebe1541e)


### mysql client 설치 - 접속을 위한
sudo dnf install mysql

### mysql 컨터이너 실행
docker run -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=true --name mysql mysql:5.7
### 1
### 1
### 1
