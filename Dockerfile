FROM python:3.5

ENV PYTHONUNBUFFERED=1 \
    UMAP_SETTINGS=/srv/umap/settings.py

RUN chown -R 10001:10001 /srv/umap && \
    groupadd --gid 10001 umap && \
    useradd --no-create-home --uid 10001 --gid 10001 --home-dir /srv/umap umap

RUN apt-get update && apt-get install -y gdal-bin

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /srv/umap

COPY docker-entrypoint.sh uwsgi.ini /srv/umap/

RUN chown umap:umap /srv/umap/*
RUN chmod u+x /srv/umap/docker-entrypoint.sh

USER umap

EXPOSE 5000

CMD ["/srv/umap/docker-entrypoint.sh"]
