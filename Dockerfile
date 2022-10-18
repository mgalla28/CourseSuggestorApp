FROM python:3.8
WORKDIR /backend
COPY ./requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir -r /backend/requirements.txt
COPY . /backend
CMD ["python", "/backend/api.py"]