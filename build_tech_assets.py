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
    key_vault_dict = {
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
    key_vault_asset_yaml = tech_asset_template.render(key_vault_dict)

    return key_vault_asset_yaml


def build_cache_tm(name: str, asset_type: str) -> str:
    redis_cache_dict = {
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
    redis_cache_asset_yaml = tech_asset_template.render(redis_cache_dict)

    return redis_cache_asset_yaml

def build_app_service_tm(name: str, asset_type: str, kind: str) -> str:

    kind_ref = ""
    technology = ""
    machine = ""
    match kind:
        case "app":
            kind_ref = "Windows Web App"
            technology = "web-application"
            machine = "virtual"
        case "app,linux":
            kind_ref = "Linux Web App"
            technology = "web-application"
            machine = "virtual"
        case "app,linux,container":
            kind_ref = "Linux Container Web App"
            technology = "web-application"
            machine = "container"
        case "hyperV" | "app,container,windows":
            kind_ref = "Windows Container Web App"
            technology = "web-application"
            machine = "container"
        case "app,linux,kubernetes":
            kind_ref = "Linux Web App on ARC"
            technology = "web-application"
            machine = "container"
        case "app,linux,container,kubernetes":
            kind_ref = "Linux Container Web App on ARC"
            technology = "web-application"
            machine = "container"
        case "functionapp":
            kind_ref = "Function Code App"
            technology = "function"
            machine = "serverless"
        case "functionapp,linux":
            kind_ref = "Linux Consumption Function App"
            technology = "function"
            machine = "serverless"
        case "functionapp,linux,container,kubernetes":
            kind_ref = "Function Container App on ARC"
            technology = "function"
            machine = "container"
        case "functionapp,linux,kubernetes":
            kind_ref = "Function Code App on ARC"
            technology = "function"
            machine = "container"

    app_service_dict = {
        "name": name,
        "type": "App Service",
        "description": f"An app service plan, used to deploy a {kind_ref}",
        "size": "service",
        "technology": technology,
        "machine": machine
    }
    template_file = open("technical_asset_template.yaml")
    template_str = template_file.read()
    tech_asset_template = Template(template_str)
    app_service_asset_yaml = tech_asset_template.render(app_service_dict)

    return app_service_asset_yaml


def build_storage_tm(name: str, asset_type: str):
    storage_dict = {
        "name": name,
        "type": asset_type.split('/')[0],
        "description": "An Azure Storage account holding storage blobs.",
        "size": "service",
        "technology": "block-storage",
        "machine": "virtual"
    }
    template_file = open("technical_asset_template.yaml")
    template_str = template_file.read()
    tech_asset_template = Template(template_str)
    storage_asset_yaml = tech_asset_template.render(storage_dict)

    return storage_asset_yaml