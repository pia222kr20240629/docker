import os
from flask import Flask, jsonify
import psycopg2

# python flask...
app = Flask(__name__)  # web application


# 환경 변수에서 설정 가져오기
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
postgres_host = os.getenv('POSTGRES_HOST', 'localhost')
postgres_port = int(os.getenv('POSTGRES_PORT', 5432))
postgres_user = os.getenv('POSTGRES_USER', 'postgres')
postgres_password = os.getenv('POSTGRES_PASSWORD', 'postgres')
postgres_db = os.getenv('POSTGRES_DB', 'postgres')

# Postgres 연결
conn = psycopg2.connect(
    host=postgres_host,
    port=postgres_port,
    user=postgres_user,
    password=postgres_password,
    dbname=postgres_db
)
cursor = conn.cursor()

@app.route('/results', methods=['GET'])
def get_results():
	cursor.execute('SELECT vote, COUNT(*) from votes GROUP BY vote')
	results = cursor.fetchall()
	return jsonify(results)

if __name__ == '__main__'	:
	app.run(host='0.0.0.0', port=80)
