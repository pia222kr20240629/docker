### scp -r root@192.168.150.37:/home/rocky/file-upload-app/** ./


[rocky@localhost ~]$ mkdir ingress-example
[rocky@localhost ~]$ cd ingress-example/
[rocky@localhost ingress-example]$ cat << EOF > Dockerfile
> FROM nginx:alpine
> COPY ./index.html /usr/share/nginx/html/index.html
> EOF
[rocky@localhost ingress-example]$ LS
bash: LS: command not found...
Similar command is: 'ls'
[rocky@localhost ingress-example]$ ls
Dockerfile
[rocky@localhost ingress-example]$ cat << EOF > index.html
> <html>
> <head>
>    <title>Welcome to Kubernetes Ingress Example</title>
> </head>
> <body>
>   <h1>Hello from Kubernetes Ingress!</h1>
> </body>
> </html>
> EOF
[rocky@localhost ingress-example]$ 
