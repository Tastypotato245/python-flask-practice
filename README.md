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
sudo docker run -it --rm -p 8080:8080 <custom_image_name> /app/venv/bin/python3 app.py
```

/
![image](https://github.com/Tastypotato245/python-flask-practice/assets/63251068/71ff0eff-f4bd-41e6-9e06-0734c18e7f4f)

/get_data
<img width="528" alt="image" src="https://github.com/Tastypotato245/python-flask-practice/assets/63251068/7d4f7e78-d6b7-4950-bf2b-e7c56960fe98">
