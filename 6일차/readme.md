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
