FROM python:3
EXPOSE 8000

WORKDIR app
COPY * /app/
RUN pip install -r requirements.txt
# Problem with migrations
#RUN ["python", "./manage.py", "db", "init"]
#RUN ["python", "./manage.py", "db", "migrate"]
#RUN ["python", "./manage.py", "db", "upgrade"]
CMD ["python", "./run.py" ]