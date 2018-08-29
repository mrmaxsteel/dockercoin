FROM python:3-alpine
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP="run.py"
ENV NODE_ADDRESS="0.0.0.0:5000"
ENTRYPOINT flask run --host=0.0.0.0