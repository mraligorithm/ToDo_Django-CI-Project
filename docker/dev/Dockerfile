FROM aligorithm/todobackend-base:latest
MAINTAINER AliGorithm <alisher.coder@gmail.com>

# Install dev/builder dependencies
RUN apt-get update && \
    apt-get install -qy python-dev libmysqlclient-dev


# Activate virtual environment and install wheel support
RUN . /appenv/bin/activate && \
      pip install wheel --upgrade



# PIP environment variables
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache


# OUTPUT: Build artefacts(WHEELS) are output here
VOLUME /wheelhouse

# OUTPUT: Build cache
VOLUME /build

# OUTPUT: Test reports are output here
VOLUME /reports

# Add test entrypoint script
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

# Set defaults for entrypoint and command string
ENTRYPOINT ["test.sh"]
CMD ["python", "manage.py", "test", "--noinput"]


COPY src /application
WORKDIR  /application
