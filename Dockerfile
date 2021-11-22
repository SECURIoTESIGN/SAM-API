FROM python:3.7-alpine
COPY . /api
WORKDIR /api
# Install OS dependencies
RUN apk add build-base libffi-dev openssl-dev
# Install app dependencies 
RUN pip3 install -r /api/requirements.txt
# Run command after container init.
CMD flask run