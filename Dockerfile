FROM searxng/searxng:latest

COPY ./settings.yml /etc/searxng/settings.yml
COPY ./uwsgi.ini /etc/searxng/uwsgi.ini

ENV SEARXNG_SETTINGS_PATH=/etc/searxng/settings.yml
ENV UWSGI_INI=/etc/searxng/uwsgi.ini
