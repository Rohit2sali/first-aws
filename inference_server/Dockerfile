FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir \
torch --index-url https://download.pytorch.org/whl/cpu

COPY . .

RUN chmod +x /code/entrypoint.sh

CMD ["/code/entrypoint.sh"]
