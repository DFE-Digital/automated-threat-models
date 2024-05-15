FROM threagile/threagile

USER root

WORKDIR /app

RUN mkdir /app/yaml-templates && chown 1000:1000 /app/yaml-templates

COPY --chown=1000:1000 build_data_assets.py /app/
COPY --chown=1000:1000 build_tech_assets.py /app/
COPY --chown=1000:1000 dfe_threagile.py /app/
COPY --chown=1000:1000 produce_risk_tracker.py /app/
COPY --chown=1000:1000 yaml-templates/data_assets_template.yaml /app/yaml-templates
COPY --chown=1000:1000 yaml-templates/technical_asset_template.yaml /app/yaml-templates
COPY --chown=1000:1000 yaml-templates/threagile-example-model-template.yaml /app/yaml-templates
COPY --chown=1000:1000 yaml-templates/risks_template.yaml /app/yaml-templates

COPY --chown=1000:1000 test-data.json /app/

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

RUN python3 -m ensurepip

RUN pip3 install --no-cache --upgrade pip setuptools

RUN pip3 install jinja2

USER 1000:1000
