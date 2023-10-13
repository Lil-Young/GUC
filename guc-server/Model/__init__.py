import dotenv, os
import db
# dotenv 라이브러리를 사용해서 .env 파일을 찾음. 이 파일에는 환경변수와 .env에 들어있는 내용이 저장됨
dotenv_file = dotenv.find_dotenv()
# dotenv 라이브러리를 사용해서 .env 파일에서 환경변수 및 파일에 있는 내용을 로드함. 그래서 .env 파일에 정의된 환경변수를 사용할 수 있음
dotenv.load_dotenv(dotenv_file)

# mysql
host = os.environ['host']
port = os.environ['port']
user = os.environ['user']
pw = os.environ['pw']

# mongodb
mogno_url = os.environ['mongo_url']
print(mogno_url)
