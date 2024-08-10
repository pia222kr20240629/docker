chat-app
  - -server.js        #node.js 서버
  - -package.json    # 패키지 관리
  - -public/           
    - -index.html    # 화면


- npm 설치는 nodejs설치를통해 해결
- sudo dnf update    # npm 설치를 위한 dnf 업데이트
- sudo dnf install nodejs npm  # node를 설치하면 npm도 같이 설치된다   위의명령어와 이 명령어는 로컬계정의 루트에서 실행하는것을 추천
- node -v
- npm -v
- npm install express
- npm start     --> localhost:3000 접속해서 실행 확인
# 도커로 컨테이너화
- docker build -t chat-app .
- docker run -d -p 3000:3000 chat-app
- docker push pia222/chat-app:latest
- localhost:3000으로 확인하고.
- docker stop <containerid>
# 쿠버네티스 배포
- k apply -f deployment.yml
- k apply -f service.yml
![image](https://github.com/user-attachments/assets/6d694903-1c9d-4cbe-b91f-fb50fac96e04)

-http://internel ip:30000



# 웹기반 파일 업로드 다운로드
file-upload-app
  - -Dockerfile
  - -app.js
  - -package.json
  - -public/
    - -index.html 
