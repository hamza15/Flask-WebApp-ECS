FROM ubuntu:16.04

MAINTAINER Your Name "sardan5@vt.edu"

RUN apt-get install -y python-pip python-dev nano

COPY ./templates/index.html /app/templates/index.html

COPY ./templates/solver.html /app/templates/solver.html

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "anagram.py" ]
