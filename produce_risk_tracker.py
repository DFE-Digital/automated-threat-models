import json
import datetime
import argparse


def print_yaml(risk_dict: dict):
    print(f"  {risk_dict['name']}:")
    print(f"    status: {risk_dict['status']}")
    print(f"    justification: ")
    print(f"    ticket: ")
    print(f"    date: \"{risk_dict['date']}\"")
    print(f"    checked_by: ")


def read_risks_json(file_path: str):
    file = open(file_path)
    data = json.load(file)

    date_today_obj = datetime.datetime.now()
    date_today_fmt = date_today_obj.strftime("%Y-%m-%d")

    print("risk_tracking:")

    for risk in data:
        risk_dict = {
            "name": risk["synthetic_id"],
            "status": risk["risk_status"],
            "date": date_today_fmt,
        }

        print_yaml(risk_dict)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('--file', nargs='?', default='risks.json', help='The file path for you risks json file')

    args = parser.parse_args()

    read_risks_json(args.file)