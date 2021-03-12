FROM python:3.8-slim-buster

RUN mkdir /home/notebooks
WORKDIR /home/notebooks

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY Notebook.ipynb Notebook.ipynb

EXPOSE 8888

ENTRYPOINT ["jupyter","notebook","--ip=0.0.0.0","--allow-root","--no-browser"]