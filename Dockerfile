FROM python:3.9-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile" , "Pipfile.lock", "./"]
RUN pipenv install --system --deploy
COPY ["app.py" , "model_C=1.0.bin" , "./"]
EXPOSE 5000
ENTRYPOINT ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
