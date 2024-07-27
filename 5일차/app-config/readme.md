- 각각의 파일을 k apply -f <yaml file> 로 배포하고

- k exec -it pod-with-configmap -- env | grep DATABASE  명령을 통해 적용여부를 확인한다


- k exec -it pod-with-env-configmap -- env | grep -E 'API_|LOG_'
