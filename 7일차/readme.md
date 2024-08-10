chat-app
  - -server.js        #node.js 서버
  - -package.json    # 패키지 관리
  - -public/           
    - -index.html    # 화면


- npm 설치는 nodejs설치를통해 해결
- sudo dnf update
- sudo dnf install nodejs npm
- node -v
- npm -v
- npm install express
- npm start     --> localhost:3000 접속해서 실행 확인
# 도커로 컨테이너화
- docker build -t chat-app .
- docker run -d -p 3000:3000 chat-app
- localhost:3000으로 확인하고.
- docker stop <containerid>
# 쿠버네티스 배포
