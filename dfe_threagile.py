import json
import argparse
import os
import sys

from jinja2 import Template

from build_tech_assets import (
    build_container_app_tm,
    build_key_vault_tm,
    build_cache_tm,
    build_app_service_tm,
    build_storage_tm,
)
from build_data_assets import (
    build_client_app_data_asset,
    build_job_information_data_asset,
    build_payment_details_asset,
    build_school_data_asset,
    build_secrets_asset,
    build_server_app_data_asset,
    build_student_pii_data_asset,
    build_teacher_pii_data_asset,
    build_vulnerable_children_data_asset,
)
from produce_risk_tracker import read_risks_json, template_inject_risks


def temp_file_read() -> list:
    data_list = []
    # temp: I want to prove we can run threagile in multiple ways in GitHub Actions before the feature is built
    try:
        file = open("/app/work/test-data.json", "r")
    except FileNotFoundError:
        print(
            "test-data.json file not found, this file is for testing purposes - automated Azure resource collection feature not yet implemented."
        )
        sys.exit(0)
    lines = file.readlines()

    for line in lines:
        stripped_line = json.loads(line.strip())
        data_list.append(stripped_line)

    return data_list


def produce_assets() -> list:
    assets_list = temp_file_read()
    yaml_list = []
    all_tech_tags = []

    for asset in assets_list:
        name = asset["result"]["name"].lower()
        asset_type = asset["result"]["type"]

        match asset_type:
            case "microsoft.app/containerapps":
                container_app_asset_yaml, tag_list = build_container_app_tm(
                    name, asset_type
                )
                yaml_list.append(container_app_asset_yaml)

                for tag in tag_list:
                    all_tech_tags.append(tag)

                print(container_app_asset_yaml)
            case "microsoft.keyvault/vaults":
                key_vault_asset_yaml, tag_list = build_key_vault_tm(name, asset_type)
                yaml_list.append(key_vault_asset_yaml)

                for tag in tag_list:
                    all_tech_tags.append(tag)

                print(key_vault_asset_yaml)
            case "microsoft.cache/redis":
                redis_cache_asset_yaml, tag_list = build_cache_tm(name, asset_type)
                yaml_list.append(redis_cache_asset_yaml)

                for tag in tag_list:
                    all_tech_tags.append(tag)

                print(redis_cache_asset_yaml)
            case "microsoft.web/sites":
                kind = asset["result"]["kind"]
                app_service_yaml, tag_list = build_app_service_tm(
                    name, asset_type, kind
                )
                yaml_list.append(app_service_yaml)

                for tag in tag_list:
                    all_tech_tags.append(tag)

                print(app_service_yaml)
            case "microsoft.storage/storageaccounts":
                storage_yaml, tag_list = build_storage_tm(name, asset_type)
                yaml_list.append(storage_yaml)

                for tag in tag_list:
                    all_tech_tags.append(tag)

                print(storage_yaml)

    return yaml_list, all_tech_tags


def data_assets() -> list:
    answers = ["y", "n"]
    dicts = []

    teacher_pii = ""
    while teacher_pii.lower() not in answers:
        teacher_pii = (
            input("Does your app handle teacher Personal Information? (Y/N): ") or "y"
        )
    if teacher_pii.lower() == "y":
        teacher_pii = True
    else:
        teacher_pii = False
    dicts.append(dict(name="teacher-pii", present=teacher_pii))

    student_pii = ""
    while student_pii.lower() not in answers:
        student_pii = (
            input("Does your app handle student Personal Information? (Y/N): ") or "y"
        )
    if student_pii.lower() == "y":
        student_pii = True
    else:
        student_pii = False
    dicts.append(dict(name="student-pii", present=student_pii))

    client_app_code = ""
    while client_app_code.lower() not in answers:
        client_app_code = (
            input("Does your app include client side code (JavaScript/HTML)? (Y/N): ")
            or "y"
        )

    if client_app_code.lower() == "y":
        client_app_code = True
    else:
        client_app_code = False
    dicts.append(dict(name="client-application-code", present=client_app_code))

    server_app_code = ""
    while server_app_code.lower() not in answers:
        server_app_code = (
            input(
                "Does your app include server side code (Ruby/C#/Python/Rust/etc)? (Y/N): "
            )
            or "y"
        )
    if server_app_code.lower() == "y":
        server_app_code = True
    else:
        server_app_code = False
    dicts.append(dict(name="server-application-code", present=server_app_code))

    vulnerable_children_data = ""
    while vulnerable_children_data.lower() not in answers:
        vulnerable_children_data = (
            input(
                "Does your app handle the data relating to vulnerable children? (Y/N): "
            )
            or "y"
        )
    if vulnerable_children_data.lower() == "y":
        vulnerable_children_data = True
    else:
        vulnerable_children_data = False
    dicts.append(
        dict(name="vulnerable-children-data", present=vulnerable_children_data)
    )

    job_information = ""
    while job_information.lower() not in answers:
        job_information = (
            input("Does your app handle information relating to jobs? (Y/N): ") or "y"
        )
    if job_information.lower() == "y":
        job_information = True
    else:
        job_information = False
    dicts.append(dict(name="job-information", present=job_information))

    school_data = ""
    while school_data.lower() not in answers:
        school_data = (
            input("Does your app handle data relating to schools? (Y/N): ") or "y"
        )
    if school_data.lower() == "y":
        school_data = True
    else:
        school_data = False
    dicts.append(dict(name="school-data", present=school_data))

    payment_details = ""
    while payment_details.lower() not in answers:
        payment_details = (
            input(
                "Does your app handle payment information such a credit card of bank account details? (Y/N): "
            )
            or "y"
        )
    if payment_details.lower() == "y":
        payment_details = True
    else:
        payment_details = False
    dicts.append(dict(name="payment-details", present=payment_details))

    secrets_and_keys = ""
    while secrets_and_keys.lower() not in answers:
        secrets_and_keys = (
            input(
                "Does your app utilise keys, secrets, and a vault to store them? (Y/N): "
            )
            or "y"
        )
    if secrets_and_keys.lower() == "y":
        secrets_and_keys = True
    else:
        secrets_and_keys = False
    dicts.append(dict(name="secrets-and-api-keys", present=secrets_and_keys))

    return dicts


def template_inject(
    yaml_list: list, data_list: list, all_tags: list, risks: list = []
) -> str:
    template_file = open("yaml-templates/threagile-example-model-template.yaml")
    template_str = template_file.read()
    tech_asset_template = Template(template_str)

    final_yaml = tech_asset_template.render(
        yaml_list=yaml_list, data_list=data_list, all_tags=all_tags, risks=risks
    )

    return final_yaml


def produce_data_assets(chosen_data_asset_dicts: list) -> list:
    built_data_assets = []
    all_data_tags = []
    for data_asset in chosen_data_asset_dicts:
        if data_asset["present"]:
            match data_asset["name"]:
                case "teacher-pii":
                    teacher_pii, teacher_pii_tags = build_teacher_pii_data_asset()
                    built_data_assets.append(teacher_pii)
                    for tags in teacher_pii_tags:
                        all_data_tags.append(tags)
                case "student-pii":
                    student_pii, student_pii_tags = build_student_pii_data_asset()
                    built_data_assets.append(student_pii)
                    for tags in student_pii_tags:
                        all_data_tags.append(tags)
                case "client-application-code":
                    client_application_code, client_app_tags = (
                        build_client_app_data_asset()
                    )
                    built_data_assets.append(client_application_code)
                    for tags in client_app_tags:
                        all_data_tags.append(tags)
                case "server-application-code":
                    server_application_code, server_app_tags = (
                        build_server_app_data_asset()
                    )
                    built_data_assets.append(server_application_code)
                    for tags in server_app_tags:
                        all_data_tags.append(tags)
                case "vulnerable-children-data":
                    vulnerable_children_data, vulnerable_children_data_tags = (
                        build_vulnerable_children_data_asset()
                    )
                    built_data_assets.append(vulnerable_children_data)
                    for tags in vulnerable_children_data_tags:
                        all_data_tags.append(tags)
                case "job-information":
                    job_information, job_info_tags = build_job_information_data_asset()
                    built_data_assets.append(job_information)
                    for tags in job_info_tags:
                        all_data_tags.append(tags)
                case "school-data":
                    school_data, school_data_tags = build_school_data_asset()
                    built_data_assets.append(school_data)
                    for tags in school_data_tags:
                        all_data_tags.append(tags)
                case "payment-details":
                    payment_details, payment_details_tags = (
                        build_payment_details_asset()
                    )
                    built_data_assets.append(payment_details)
                    for tags in payment_details_tags:
                        all_data_tags.append(tags)
                case "secrets-and-api-keys":
                    secrets_and_api_keys, secrets_and_api_keys_tags = (
                        build_secrets_asset()
                    )
                    built_data_assets.append(secrets_and_api_keys)
                    for tags in secrets_and_api_keys_tags:
                        all_data_tags.append(tags)

    return built_data_assets, all_data_tags


def produce_asset_lists() -> tuple:
    yaml_list, all_tech_tags = produce_assets()

    chosen_data_assets_dicts = data_assets()

    data_list, all_data_tags = produce_data_assets(chosen_data_assets_dicts)

    all_tags = all_tech_tags + all_data_tags

    all_tags = list(dict.fromkeys(all_tags))

    return yaml_list, data_list, all_tags


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--risks-only",
        help="Only produce risk tracker.",
        action="store_true",
        required=False,
    )
    parser.add_argument(
        "--risks-json",
        nargs="?",
        default="output/risks.json",
        help="The file path for you risks json file.",
    )

    args = parser.parse_args()

    if args.risks_only:
        risks = read_risks_json(args.risks_json)
        risks_output = template_inject_risks(risks)
        print(risks_output)
    else:

        # Writes initial threat model and produces risks.json

        yaml_list, data_list, all_tags = produce_asset_lists()

        final_yaml = template_inject(yaml_list, data_list, all_tags)

        print(final_yaml)

        try:
            with open("/app/yaml-templates/threagile-pre-risks.yaml", "x") as yaml_file:
                yaml_file.write(final_yaml)
        except FileExistsError:
            print("File exists, overwriting...")
            with open("/app/yaml-templates/threagile-pre-risks.yaml", "w") as yaml_file:
                yaml_file.write(final_yaml)

        os.system(
            "threagile -verbose -model /app/yaml-templates/threagile-pre-risks.yaml -output /app/work/output"
        )

        # Writes final version, with risks from risks.json added to the yaml for automated mitigation tracking

        risks = read_risks_json("/app/work/output/risks.json")

        final_with_risks = template_inject(yaml_list, data_list, all_tags, risks)

        try:
            with open(
                "/app/work/yaml-templates/dfe-threagile-final.yaml", "x"
            ) as yaml_file:
                yaml_file.write(final_with_risks)
        except FileExistsError:
            print("File exists, overwriting...")
            with open(
                "/app/work/yaml-templates/dfe-threagile-final.yaml", "w"
            ) as yaml_file:
                yaml_file.write(final_with_risks)

        os.system(
            "threagile -verbose -model /app/work/yaml-templates/dfe-threagile-final.yaml -output /app/work/output"
        )
