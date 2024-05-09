from jinja2 import Template


def build_container_app_tm(name: str, asset_type: str) -> str:
    container_app_dict = {
        "name": name,
        "type": asset_type.split('/')[0],
        "description": "A container app running a web application for the public.",
        "size": "application",
        "technology": "web-application",
        "machine": "container"
    }
    template_file = open("technical_asset_template.yaml")
    template_str = template_file.read()
    tech_asset_template = Template(template_str)
    container_app_asset_yaml = tech_asset_template.render(container_app_dict)

    return container_app_asset_yaml


def build_key_vault_tm(name: str, asset_type: str) -> str:
    container_app_dict = {
        "name": name,
        "type": asset_type.split('/')[0],
        "description": "A key vault used to hold sensitive keys, secrets, and config.",
        "size": "service",
        "technology": "vault",
        "machine": "virtual"
    }
    template_file = open("technical_asset_template.yaml")
    template_str = template_file.read()
    tech_asset_template = Template(template_str)
    container_app_asset_yaml = tech_asset_template.render(container_app_dict)

    return container_app_asset_yaml


def build_cache_tm(name: str, asset_type: str) -> str:
    container_app_dict = {
        "name": name,
        "type": asset_type.split('/')[0],
        "description": "A redis cache for holding data for reliability.",
        "size": "service",
        "technology": "database",
        "machine": "virtual"
    }
    template_file = open("technical_asset_template.yaml")
    template_str = template_file.read()
    tech_asset_template = Template(template_str)
    container_app_asset_yaml = tech_asset_template.render(container_app_dict)

    return container_app_asset_yaml