FROM debian:buster-slim
LABEL maintainer="takumiw"
ENV TZ Asia/Tokyo

RUN apt update && apt install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    curl \
    libbz2-dev \
    libreadline-dev \
    libssl-dev \
    libsqlite3-dev \
    tar \
    wget \
    xz-utils \
    zlib1g-dev \
    &&  apt clean \
    &&  rm -rf /var/lib/apt/lists/*

# install Python
WORKDIR /root/
RUN wget https://www.python.org/ftp/python/3.9.4/Python-3.9.4.tar.xz \
    && tar xvf Python-3.9.4.tar.xz \
    && cd Python-3.9.4 \
    && ./configure --enable-optimizations \
    && make install
RUN rm Python-3.9.4.tar.xz

WORKDIR /root/Python-3.9.4
RUN ln -fs /root/Python-3.9.4/python /usr/bin/python
RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python 

# install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV SHELL /bin/bash -l

ENV POETRY_CACHE ~/.cache/poetry
ENV PIP_CACHE_DIR ~/.cache/pip
RUN $HOME/.poetry/bin/poetry config virtualenvs.path /app/
ENV PATH ${PATH}:/root/.poetry/bin:/bin:/usr/local/bin:/usr/bin

# copy files into container
COPY ./pyproject.toml /app/
COPY ./poetry.lock /app/

# install libraries using poetry
WORKDIR /app
ENV PATH $PATH:/home/${USER_NAME}/.local/bin
RUN poetry install \
    && rm -rf ~/.cache/pip/*\
    && rm -rf ~/.cache/pypoetry/*

WORKDIR /app
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]