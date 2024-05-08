import json

from jinja2 import Template


def temp_file_read() -> list:
    data_list = []
    file = open("test-data.json", "r")
    lines = file.readlines()

    for line in lines:
        stripped_line = json.loads(line.strip())
        data_list.append(stripped_line)

    return data_list


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


def produce_assets() -> list:
    assets_list = temp_file_read()
    yaml_list = []

    for asset in assets_list:
        name = asset["result"]["name"]
        asset_type = asset["result"]["type"]

        if asset_type == "microsoft.app/containerapps":
            container_app_asset_yaml = build_container_app_tm(name, asset_type)
            yaml_list.append(container_app_asset_yaml)
            print(container_app_asset_yaml)
    
    return yaml_list


def write_assets_to_yaml():
    yaml_list = produce_assets()

    template_file = open("threagile-example-model-template.yaml")
    template_str = template_file.read()
    tech_asset_template = Template(template_str)
    final_yaml = tech_asset_template.render(yaml_list=yaml_list)
    print(final_yaml)
    


if __name__ == '__main__':
    write_assets_to_yaml()