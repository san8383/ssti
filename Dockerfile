FROM python:3.11.6-slim-bullseye
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./app.py ./app.py
COPY ./index.html ./index.html
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
