# 사전 환경 설정
### 윈도우에서 스프링부트로 생성한 프로젝트를 리눅스로 옮기고  컴파일 
### maven 17버전 설치
 - https://maven.apache.org/download.cgi
 - 클릭->tar.gz archives	Binary apache-maven-4.0.0-beta-3-bin.tar.gz (sha512, asc)
- 리눅스로 파일 전송
- 리눅스폴더에서 압축해제
- tar -xzvf apache-maven-4.0.0-beta-3-bin.tar.gz 
- 환경변수에 등록하려고 압축푼 파일을 
- sudo mv apache-maven-4.0.0-beta-3 /usr/local/apache-maven

- export M2_HOME=/usr/local/apache-maven
- export PATH=$M2_HOME/bin:$PATH
- source ~/.bashrc
- mvn -v

- 스프링부트 소스가 있는 디렉터리에서
- mvn clean package

- target폴더가 생김

###  자바 17설치
- sudo dnf install openjdk-17-jdk
- java -version

## 도커실행
docker-compose up -d

## 브라우져에서 http://localhost:8080
