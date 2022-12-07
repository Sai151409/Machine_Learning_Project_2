FROM python:3.7
RUN apt update -y && apt install awscli -y
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["app.py"]

