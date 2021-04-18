FROM python:3.7

RUN mkdir backend
COPY . ./backend
WORKDIR backend

RUN pip install -r req.txt

ENTRYPOINT ["python", "/backend/app.py"]