import os
from flask import Flask, jsonify, request
import redis

# python flask...
app = Flask(__name__)  # web application


# 환경 변수에서 설정 가져오기
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))

# Redis 연결
r = redis.Redis(host=redis_host, port=redis_port,db=0)

@app.route('/vote', methods=['POST'])
def vote():
	data = request.json
	vote = data.get('vote')
	if vote:
		r.rpush('votes',vote)
		return jsonify({'status':'success'}), 200
	return jsonify({'status':'error', 'message':'Invalid vote'}), 400

if __name__ == '__main__'	:
	app.run(host='0.0.0.0', port=80)
