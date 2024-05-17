from jinja2 import Template


def build_container_app_tm(name: str, asset_type: str) -> tuple:
    container_app_dict = {
        "name": name,
        "type": asset_type.split("/")[0],
        "description": "A container app running a web application for the public.",
        "size": "application",
        "technology": "web-application",
        "machine": "container",
        "tags": [name, "azure", "azure-container-app", asset_type],
    }
    with open("yaml-templates/technical_asset_template.yaml") as template_file:
        template_str = template_file.read()
    tech_asset_template = Template(template_str, autoescape=True)
    container_app_asset_yaml = tech_asset_template.render(container_app_dict)

    tag_list = container_app_dict["tags"]

    return container_app_asset_yaml, tag_list


def build_key_vault_tm(name: str, asset_type: str) -> tuple:
    key_vault_dict = {
        "name": name,
        "type": asset_type.split("/")[0],
        "description": "A key vault used to hold sensitive keys, secrets, and config.",
        "size": "service",
        "technology": "vault",
        "machine": "virtual",
        "tags": [
            name,
            "azure",
            "azure-key-vault",
            "vault",
            "secrets",
            "keys",
            asset_type,
        ],
    }
    with open("yaml-templates/technical_asset_template.yaml") as template_file:
        template_str = template_file.read()
    tech_asset_template = Template(template_str, autoescape=True)
    key_vault_asset_yaml = tech_asset_template.render(key_vault_dict)

    tag_list = key_vault_dict["tags"]

    return key_vault_asset_yaml, tag_list


def build_cache_tm(name: str, asset_type: str) -> tuple:
    redis_cache_dict = {
        "name": name,
        "type": asset_type.split("/")[0],
        "description": "A redis cache for holding data for reliability.",
        "size": "service",
        "technology": "database",
        "machine": "virtual",
        "tags": [name, "azure", "azure-redis-cache", "cache", asset_type],
    }
    with open("yaml-templates/technical_asset_template.yaml") as template_file:
        template_str = template_file.read()
    tech_asset_template = Template(template_str, autoescape=True)
    redis_cache_asset_yaml = tech_asset_template.render(redis_cache_dict)

    tag_list = redis_cache_dict["tags"]

    return redis_cache_asset_yaml, tag_list


def build_app_service_tm(name: str, asset_type: str, kind: str) -> tuple:

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
        "type": asset_type.split("/")[0],
        "description": f"An app service plan, used to deploy a {kind_ref}",
        "size": "service",
        "technology": technology,
        "machine": machine,
        "tags": [name, "azure", "azure-app-service", machine, technology, asset_type],
    }
    with open("yaml-templates/technical_asset_template.yaml") as template_file:
        template_str = template_file.read()
    tech_asset_template = Template(template_str, autoescape=True)
    app_service_asset_yaml = tech_asset_template.render(app_service_dict)

    tag_list = app_service_dict["tags"]

    return app_service_asset_yaml, tag_list


def build_storage_tm(name: str, asset_type: str) -> tuple:
    storage_dict = {
        "name": name,
        "type": asset_type.split("/")[0],
        "description": "An Azure Storage account holding storage blobs.",
        "size": "service",
        "technology": "block-storage",
        "machine": "virtual",
        "tags": [name, "azure", "azure-storage", "blob", asset_type],
    }
    with open("yaml-templates/technical_asset_template.yaml") as template_file:
        template_str = template_file.read()
    tech_asset_template = Template(template_str, autoescape=True)
    storage_asset_yaml = tech_asset_template.render(storage_dict)

    tag_list = storage_dict["tags"]

    return storage_asset_yaml, tag_list
