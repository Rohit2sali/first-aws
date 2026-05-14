FROM python:3.11-slim

WORKDIR /code

RUN pip install torch --index-url https://download.pytorch.org/whl/cpu --no-cache-dir
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./app /code/app
COPY ./templates /code/templates
COPY entrypoint.sh /code/entrypoint.sh

RUN chmod +x /code/entrypoint.sh

CMD ["/code/entrypoint.sh"]