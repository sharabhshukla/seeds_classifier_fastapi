FROM tiangolo/uvicorn-gunicorn-fastapi:latest
COPY . ./app_api
WORKDIR ./app_api
RUN pip install -r requirements.txt
EXPOSE 8081
ENTRYPOINT uvicorn main_app:app --host=0.0.0.0 --port=8081
