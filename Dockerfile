FROM python:3.8-slim-buster

RUN mkdir /home/notebooks

RUN mkdir /home/notebooks/data

WORKDIR /home/notebooks

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8888

ENTRYPOINT ["jupyter", "notebook","--ip=0.0.0.0","--allow-root", "--no-browser"]