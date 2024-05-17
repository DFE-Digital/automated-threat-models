import json
import datetime
import argparse

from jinja2 import Template


def print_yaml(risk_dict: dict):
    print(f"  {risk_dict['name']}:")
    print(f"    status: {risk_dict['status']}")
    print("    justification: ")
    print("    ticket: ")
    print(f"    date: \"{risk_dict['date']}\"")
    print("    checked_by: ")


def build_risk(risk_dict: dict):
    with open("yaml-templates/risks_template.yaml") as template_file:
        template_str = template_file.read()
    risk_template = Template(template_str, autoescape=True)
    risk_yaml = risk_template.render(risk_dict)

    return risk_yaml


def read_risks_json(file_path: str) -> list:
    with open(file_path) as file:
        data = json.load(file)

    date_today_obj = datetime.datetime.now()
    date_today_fmt = date_today_obj.strftime("%Y-%m-%d")

    print("risk_tracking:")

    risks = []

    for risk in data:
        risk_dict = {
            "name": risk["synthetic_id"],
            "status": risk["risk_status"],
            "justification": "Enter justification here.",
            "ticket": "Enter ticket number relating to your risk and mitigations here.",
            "date": date_today_fmt,
            "checked_by": "Enter name of owner/ reviewer here.",
        }

        print_yaml(risk_dict)
        risk_yaml = build_risk(risk_dict)
        risks.append(risk_yaml)

    return risks


def template_inject_risks(risks: list) -> str:
    # change to the output from asset builder
    with open("yaml-templates/threagile-pre-risks.yaml") as template_file:
        template_str = template_file.read()
    risks_template = Template(template_str, autoescape=True)
    final_yaml = risks_template.render(risks=risks)
    print(final_yaml)
    return final_yaml


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--file",
        nargs="?",
        default="risks.json",
        help="The file path for you risks json file",
    )

    args = parser.parse_args()

    risks = read_risks_json(args.file)

    risks_output = template_inject_risks(risks)

    print(risks_output)
