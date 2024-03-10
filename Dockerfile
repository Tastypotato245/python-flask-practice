# Alpine Linux를 기반 이미지로 사용
FROM alpine:latest

# Python과 pip 설치
RUN apk add --no-cache python3 py3-pip python3-dev py3-virtualenv

# 작업 디렉토리 설정
WORKDIR /app

# 가상 환경 생성
RUN python3 -m venv venv

# 가상 환경 내에서 Flask 설치
RUN . venv/bin/activate && pip3 install Flask

COPY . .

# 컨테이너가 시작될 때 실행될 명령어
CMD ["/app/venv/bin/python3", "app.py"]
