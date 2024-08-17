### scp -r root@192.168.150.37:/home/rocky/ingress-example/** ./



### docker build -t ingress-example:latest .
### docker run -d -p 8080:80 --name ingress-example-container ingress-example:latest

![image](https://github.com/user-attachments/assets/0162262d-5f75-4770-8776-d9d24e3037a6)


# 쿠버네티스에 배포 및 Ingress 설정
### ingress 설정 적용
- kubectl apply -f ingress.yaml
### ingress 컨트롤러 적용
- kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
- 만약 에러가 발생한다면
- 기존작업 삭제
    - kubectl delete job ingress-nginx-admission-create -n ingress-nginx
    - kubectl delete job ingress-nginx-admission-patch -n ingress-nginx
- 다시배포
    - kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
### host 파일 수정
- echo "127.0.0.1 ingress-react-example.local" | sudo tee -a /etc/hosts
### 결과 확인
- http://ingress-react-example.local

