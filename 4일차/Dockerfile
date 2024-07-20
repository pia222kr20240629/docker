# 베이스 이미지로 Python 3.9 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
RUN pip install redis

# 애플리케이션 파일 복사
COPY counter.py .

# 애플리케이션 실행
CMD ["python", "counter.py"]
