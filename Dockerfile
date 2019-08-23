FROM python:latest

COPY . /app
WORKDIR /app

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

ENTRYPOINT ["python"]
EXPOSE 8080
CMD ["app.py"]
