FROM python:3.9

WORKDIR /app

RUN pip install streamlit==0.84.2 requests==2.26.0

COPY ./app.py .

CMD ["streamlit", "run", "app.py"]