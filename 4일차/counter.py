import redis
import os

# Redis 서비스의 이름과 포트를 환경 변수로 설정
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))

# Redis 클라이언트 생성
r = redis.Redis(host=redis_host, port=redis_port)

# 키 값을 증가시킴
counter_key = 'counter'
r.incr(counter_key)

# 현재 카운터 값을 출력
current_value = r.get(counter_key)
print(f"Current counter value: {current_value.decode('utf-8')}")
