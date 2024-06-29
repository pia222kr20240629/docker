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
### 컨테이너 실행이 되는 상태에서 mysql에 접속하기
mysql -h 127.0.0.1 -u root
### 접속한후에 mysql 명령어 써보기
![image](https://github.com/pia222kr20240629/docker/assets/174164680/557466b2-6a08-4f99-a136-31e42952a882)


### 도커 컨테이너 확인
docker ps 
docker ps -a

### 삭제
docker rm -f [ 컨터이너 아이디]

docker rmi -f [ 이미지 아이디 ]

## 워드프레스용 데이터베이스 생성하기
mysql -h 127.0.0.1 -u root

create database wp CHARACTER SET utf8;
grant all privileges on wp.* to wp@'%' identified by 'wp';
quit

docker run -d -p 8080:80 --link mysql:mysql -e WORDPRESS_DB_HOST=mysql -e WORDPRESS_DB_NAME=wp -e WORDPRESS_DB_USER=wp -e WORDPRESS_DB_PASSWORD=wp wordpress




### 워드프레스 생성
docker run -d -p 8080:80 --link mysql:mysql -e WORDPRESS_DB_HOST=mysql -e WORDPRESS_DB_NAME=wp -e WORDPRESS_DB_USER=wp -e WORDPRESS_DB_PASSWORD=wp wordpress


## tensorflow 실행
docker run -d -p 8888:8888 -p 6006:6006 teamlab/pydata-tensorflow:0.1





















