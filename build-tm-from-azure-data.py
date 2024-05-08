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


def produce_assets():
    assets_list = temp_file_read()

    for asset in assets_list:
        name = asset["result"]["name"]
        asset_type = asset["result"]["type"]

        if asset_type == "microsoft.app/containerapps":
            container_app_asset_yaml = build_container_app_tm(name, asset_type)
            print(container_app_asset_yaml)



if __name__ == '__main__':
    produce_assets()