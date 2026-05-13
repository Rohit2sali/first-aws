FROM python:3.9-slim

WORKDIR /code

# 1. Install dependencies first (caches this step to save time)
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

# 2. Copy the application code
COPY ./app /code/app
COPY ./templates /code/templates

# 3. Copy the entrypoint script AND make it executable
COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

# 4. Run the script
CMD ["/code/entrypoint.sh"]