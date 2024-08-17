FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf /root/.cache/pip

RUN useradd -m myuser
USER myuser
EXPOSE 5000

CMD ["python", "app.py"]