FROM python:3.11-slim
ENV TOKEN='6669607060:AAFeERcmEj8FbuNNvBb43om6VJaAWA3bUNA'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]