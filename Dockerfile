FROM threagile/threagile

USER root

WORKDIR /app

COPY --chown=1000:1000 build_data_assets.py /app/
COPY --chown=1000:1000 build_tech_assets.py /app/
COPY --chown=1000:1000 build_tm_from_azure_data.py /app/
COPY --chown=1000:1000 produce_risk_tracker.py /app/
COPY --chown=1000:1000 data_assets_template.yaml /app/
COPY --chown=1000:1000 technical_asset_template.yaml /app/
COPY --chown=1000:1000 threagile-example-model-template.yaml /app/

COPY --chown=1000:1000 test-data.json /app/

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

RUN python3 -m ensurepip

RUN pip3 install --no-cache --upgrade pip setuptools

RUN pip3 install jinja2

USER 1000:1000
