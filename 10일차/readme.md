# 용량부족으로 google driver 링크 공유합니다.. 이 파일에는 컴파일된 target이 포함되어 있어서  docker-compose build , docker-compose up 하시면 됩니다. 파일명은 final.zip 입니다.
- https://drive.google.com/file/d/1eKfCTHfRWnrkrFtrjcHgsL-US0eu6-4b/view?usp=sharing


# 사전 환경 설정
### 윈도우에서 스프링부트로 생성한 board.zip 리눅스로 옮기고  컴파일 은 아래과정을 참고해서 진행
### 파일 옮기기
- scp ./board.zip root@192.168.150.37:/home/rocky/[사용중인 디렉터리]
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
- docker-compose build
- docker-compose up
- docker ps 로 확인
- docker logs <container id>

## 브라우져에서 http://localhost:8080/posts
- get방식으로 post 테이블에 있는 데이터를 모두 가져온다
## post맨을 다운로드해서"postman-linux-x64.tar.gz"
- 압축해제 "tar -xvzf postman-linux-x64.tar.gz"
  - 압축해제한 실행파일을 커맨드명령어가 아닌 ui에서 실행한다
- 포스트맨 어플에서 file -new -http 를 선택한후
- post 방식으로 변경하고 주소창에는 http://localhost:8080/posts 입력
- 내용에는 json형태로 작성
  ![image](https://github.com/user-attachments/assets/8d108569-cfe4-417a-9b51-60832731243b)

## 오페라 브라우져에서 http://localhost/posts 로 확인한다
![image](https://github.com/user-attachments/assets/31f9faf3-5ac8-45dd-9bdc-27fa18ffe254)

