# module import
import os
import time
import redis
import psycopg2

# env path  setting info
redis_host			= os.getenv('REDIS_HOST','localhost')
redis_port			= int(os.getenv('REDIS_PORT',6379))
postgres_host		= os.getenv('POSTGRES_HOST','localhost')
postgres_port		= int(os.getenv('POSTGRES_PORT',5432))
postgres_user		= os.getenv('POSTGRES_USER','postgres')
postgres_password		= os.getenv('POSTGRES_PASSWORD','postgres')
postgres_db			= os.getenv('POSTGRES_DB','postgres')

# redis connect
r = redis.Redis(host=redis_host, port=redis_port, db=0)

# postgres connect
conn = psycopg2.connect(
	host=postgres_host,
	port=postgres_port,
	user=postgres_user,
	password=postgres_password,
	dbname=postgres_db
)
cusor = conn.cursor()
# table create(if not exist)
cursor.execute('''
	CREATE TABLE IT NOT EXISTS votes(
	id SERIAL PRIMARY KEY,
	vote TEXT NOT NULL
	)
''')
# apply to db
conn.commit()

print('woker started, waiting for votes.....')

while True:
	vote = r.blpop('votes',0)[1].decode('utf-8')
	cursor.execute('INSERT INTO votes(vote) values(%s)', (vote,))
	conn.commit()
	print("Process vote:",vote)
	time.sleep(1)
