import json

from jinja2 import Template
from build_tech_assets import build_container_app_tm, build_key_vault_tm, build_cache_tm, build_app_service_tm
from build_data_assets import build_client_app_data_asset, build_job_information_data_asset, build_payment_details_asset, build_school_data_asset, build_secrets_asset, build_server_app_data_asset, build_student_pii_data_asset, build_teacher_pii_data_asset, build_vulnerable_children_data_asset


def temp_file_read() -> list:
    data_list = []
    file = open("test-data.json", "r")
    lines = file.readlines()

    for line in lines:
        stripped_line = json.loads(line.strip())
        data_list.append(stripped_line)

    return data_list


def produce_assets() -> list:
    assets_list = temp_file_read()
    yaml_list = []

    for asset in assets_list:
        name = asset["result"]["name"]
        asset_type = asset["result"]["type"]

        match asset_type:
            case "microsoft.app/containerapps":
                container_app_asset_yaml = build_container_app_tm(name, asset_type)
                yaml_list.append(container_app_asset_yaml)
                print(container_app_asset_yaml)
            case "microsoft.keyvault/vaults":
                key_vault_asset_yaml = build_key_vault_tm(name, asset_type)
                yaml_list.append(key_vault_asset_yaml)
                print(key_vault_asset_yaml)
            case "microsoft.cache/redis":
                redis_cache_asset_yaml = build_cache_tm(name, asset_type)
                yaml_list.append(redis_cache_asset_yaml)
                print(redis_cache_asset_yaml)
            case "microsoft.web/sites":
                kind = asset["result"]["kind"]
                app_service_yaml = build_app_service_tm(name, asset_type, kind)
                yaml_list.append(app_service_yaml)
                print(app_service_yaml)


    return yaml_list


def data_assets() -> list:
    answers = ["y", "n"]
    dicts = []

    teacher_pii=""
    while teacher_pii.lower() not in answers:
        teacher_pii = input("Does your app handle teacher Personal Information? (Y/N): ") or "y"
    if teacher_pii.lower() == "y":
        teacher_pii = True
    else:
        teacher_pii = False
    dicts.append(dict(name="teacher-pii", present=teacher_pii))

    student_pii=""
    while student_pii.lower() not in answers:
        student_pii = input("Does your app handle student Personal Information? (Y/N): ")  or "y"
    if student_pii.lower() == "y":
        student_pii = True
    else:
        student_pii = False
    dicts.append(dict(name="student-pii", present=student_pii))

    client_app_code=""
    while client_app_code.lower() not in answers:
        client_app_code = input("Does your app include client side code (JavaScript/HTML)? (Y/N): ") or "y"
    
    if client_app_code.lower() == "y":
        client_app_code = True
    else:
        client_app_code = False
    dicts.append(dict(name="client-application-code", present=client_app_code))

    server_app_code=""
    while server_app_code.lower() not in answers:
        server_app_code = input("Does your app include server side code (Ruby/C#/Python/Rust/etc)? (Y/N): ") or "y"
    if server_app_code.lower() == "y":
        server_app_code = True
    else:
        server_app_code = False
    dicts.append(dict(name="server-application-code", present=server_app_code))

    vulnerable_children_data=""
    while vulnerable_children_data.lower() not in answers:
        vulnerable_children_data = input("Does your app handle the data relating to vulnerable children? (Y/N): ") or "y"
    if vulnerable_children_data.lower() == "y":
        vulnerable_children_data = True
    else:
        vulnerable_children_data = False
    dicts.append(dict(name="vulnerable-children-data", present=vulnerable_children_data))

    job_information=""
    while job_information.lower() not in answers:
        job_information = input("Does your app handle information relating to jobs? (Y/N): ") or "y" 
    if job_information.lower() == "y":
        job_information = True
    else:
        job_information = False
    dicts.append(dict(name="job-information", present=job_information))

    school_data=""
    while school_data.lower() not in answers:
        school_data = input("Does your app handle data relating to schools? (Y/N): ") or "y" 
    if school_data.lower() == "y":
        school_data = True
    else:
        school_data = False
    dicts.append(dict(name="school-data", present=school_data))

    payment_details=""
    while payment_details.lower() not in answers:
        payment_details = input("Does your app handle payment information such a credit card of bank account details? (Y/N): ") or "y" 
    if payment_details.lower() == "y":
        payment_details = True
    else:
        payment_details = False
    dicts.append(dict(name="payment-details", present=payment_details))

    secrets_and_keys=""
    while secrets_and_keys.lower() not in answers:
        secrets_and_keys = input("Does your app utilise keys, secrets, and a vault to store them? (Y/N): ") or "y" 
    if secrets_and_keys.lower() == "y":
        secrets_and_keys = True
    else:
        secrets_and_keys = False
    dicts.append(dict(name="secrets-and-api-keys", present=secrets_and_keys))

    return dicts


def template_inject(yaml_list: list, data_list: list) -> str:
    template_file = open("threagile-example-model-template.yaml")
    template_str = template_file.read()
    tech_asset_template = Template(template_str)
    final_yaml = tech_asset_template.render(yaml_list=yaml_list, data_list=data_list)
    return final_yaml


def produce_data_assets(chosen_data_asset_dicts: list) -> list:
    built_data_assets = []
    for data_asset in chosen_data_asset_dicts:
        if data_asset["present"]:
            match data_asset["name"]:
                case "teacher-pii":
                    teacher_pii = build_teacher_pii_data_asset()
                    built_data_assets.append(teacher_pii)
                case "student-pii":
                    student_pii = build_student_pii_data_asset()
                    built_data_assets.append(student_pii)
                case "client-application-code":
                    client_application_code = build_client_app_data_asset()
                    built_data_assets.append(client_application_code)
                case "server-application-code":
                    server_application_code = build_server_app_data_asset()
                    built_data_assets.append(server_application_code)
                case "vulnerable-children-data":
                    vulnerable_children_data = build_vulnerable_children_data_asset()
                    built_data_assets.append(vulnerable_children_data)
                case "job-information":
                    job_information = build_job_information_data_asset()
                    built_data_assets.append(job_information)
                case "school-data":
                    school_data = build_school_data_asset()
                    built_data_assets.append(school_data)
                case "vulnerable-children-data":
                    vulnerable_children_data = build_payment_details_asset()
                    built_data_assets.append(vulnerable_children_data)
                case "vulnerable-children-data":
                    vulnerable_children_data = build_secrets_asset()
                    built_data_assets.append(vulnerable_children_data)
    
    return built_data_assets


def write_assets_to_yaml():
    yaml_list = produce_assets()

    chosen_data_assets_dicts = data_assets()

    data_list = produce_data_assets(chosen_data_assets_dicts)

    final_yaml = template_inject(yaml_list, data_list)
    print(final_yaml)


if __name__ == '__main__':
    write_assets_to_yaml()