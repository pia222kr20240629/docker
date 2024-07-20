import os
import time
import redis
import psycopg2

# 환경 변수에서 설정 가져오기
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
postgres_host = os.getenv('POSTGRES_HOST', 'localhost')
postgres_port = int(os.getenv('POSTGRES_PORT', 5432))
postgres_user = os.getenv('POSTGRES_USER', 'postgres')
postgres_password = os.getenv('POSTGRES_PASSWORD', 'postgres')
postgres_db = os.getenv('POSTGRES_DB', 'postgres')

# Redis 연결
r = redis.Redis(host=redis_host, port=redis_port, db=0)

# Postgres 연결
conn = psycopg2.connect(
    host=postgres_host,
    port=postgres_port,
    user=postgres_user,
    password=postgres_password,
    dbname=postgres_db
)
cursor = conn.cursor()

# 테이블 생성 (없으면)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS votes (
        id SERIAL PRIMARY KEY,
        vote TEXT NOT NULL
    )
''')
conn.commit()

print("Worker started, waiting for votes...")

# Redis 큐에서 투표 처리
while True:
    vote = r.blpop('votes', 0)[1].decode('utf-8')
    cursor.execute('INSERT INTO votes (vote) VALUES (%s)', (vote,))
    conn.commit()
    print(f"Processed vote: {vote}")
    time.sleep(1)
