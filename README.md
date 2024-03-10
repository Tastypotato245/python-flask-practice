# python-flask-practice

 - Python flask 사용 예제를 연습하기 위한 repository 입니다. 해당 app.py를 docker container에서 실행되도록 테스트하였습니다.

 - This is a repository for practicing using the python flask framework. the Dockerfile was written to test app.py in docker containers.

Base Image : Alpine

## Docker Image Build
```bash
sudo docker build -t <custom_image_name> .
```

## Test
```bash
sudo docker run -it -rm <custom_image_name> /app/venv/bin/python3 app.py
```
