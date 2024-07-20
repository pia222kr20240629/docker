# 베이스 이미지 설정
FROM python:3.9-slim

# 필요한 패키지 설치
RUN pip install redis psycopg2-binary

# 작업 디렉토리 설정
WORKDIR /app

# Python 코드 복사
COPY worker.py .

# 컨테이너 실행 명령어 설정
CMD ["python3", "worker.py"]
