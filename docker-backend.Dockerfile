FROM python:3.10-slim-buster

COPY ./proto /src/proto
COPY ./backend /src/backend
COPY ./_utils/proto-build-py.sh /usr/local/bin/proto-build-py

WORKDIR /src/backend

RUN pip install --upgrade pip \
    && pip install grpcio-tools==1.43.0 \
    && pip install -r requirements.txt \
    && /usr/local/bin/proto-build-py

CMD /usr/local/bin/proto-build-py \
    && /bin/bash

# CMD uvicorn http_server:app --reload --host=0.0.0.0 --port=8000
# CMD python grcp_server.py

