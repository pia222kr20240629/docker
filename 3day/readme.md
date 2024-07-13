- minikube start
- 에러가발생하면 교제 179페이지를 참고해서 재 시작할것

![image](https://github.com/user-attachments/assets/7d85a658-f3c5-45a7-ae6c-9f28cf5d7391)

- 현재상태확인
- ![image](https://github.com/user-attachments/assets/4484b850-f081-45d5-98af-625d2f97ae79)

- 접속테스트  url정보로 접속
- ![image](https://github.com/user-attachments/assets/729dfda0-efae-4534-97bc-b6af79e221c6)

- 삭제
- ![image](https://github.com/user-attachments/assets/d573ea46-84a2-45d9-9ac2-4da6441a967a)

- kubectl 명령
  - apply : -f옵션 같이사용  상태를 적용
  - get : 리소스 목록
  - describe : 자세하게 보여줌
  - delete : 리소스 제거
  - logs : 컨테이너 로그
  - exec : 컨테이너에 명령어를 전달, 주로 컨테이너에 접근(실행)
  - config : kubectl의 설정

- 별칭 alias
  - alias k='kubectl'
  - 다음실행시에도 기억하게 하려면 설정을 추가
  - echo "alias k='kubectl'" >> ~/.bashrc
  - 환경설정 파일 적용
  - source ~/.bashrc


# Pod 조회
kubectl get pod

# 줄임말(Shortname)과 복수형 사용가능
kubectl get pods
kubectl get po

# 여러 TYPE 입력
kubectl get pod,service
#
kubectl get po,svc

# Pod, ReplicaSet, Deployment, Service, Job 조회 => all
kubectl get all

# 결과 포멧 변경
kubectl get pod -o wide
kubectl get pod -o yaml
kubectl get pod -o json

# Label 조회
kubectl get pod --show-labels










