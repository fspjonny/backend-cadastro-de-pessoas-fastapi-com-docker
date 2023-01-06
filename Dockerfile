FROM python:3.11.1
RUN pip3 install fastapi uvicorn httpx pytest
COPY ./ /proj
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]