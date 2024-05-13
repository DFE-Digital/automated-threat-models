from jinja2 import Template


def build_teacher_pii_data_asset() -> tuple:
    data_asset_dict = {
        "name": "teacher-pii",
        "description": "Teachers personal information.",
        "usage": "business",
        "tags_list": ["teacher-pii","database", "azure", "sensitive", "pii"],
        "origin": "customer",
        "owner": "DfE",
        "quantity": "many",
        "confidentiality": "confidential",
        "integrity": "critical",
        "availability": "operational",
        "justification": "Teacher data might contain personally identifiable information (PII). The integrity and availability of teacher data is required for functioning of the service."
    }
    template_file = open("data_assets_template.yaml")
    template_str = template_file.read()
    data_asset_template = Template(template_str)
    data_asset_yaml = data_asset_template.render(data_asset_dict)

    teacher_pii_tags = data_asset_dict["tags_list"]

    return data_asset_yaml, teacher_pii_tags


def build_student_pii_data_asset() -> tuple:
    data_asset_dict = {
        "name": "student-pii",
        "description": "Students personal information.",
        "usage": "business",
        "tags_list": ["student-pii","database", "azure", "sensitive", "pii"],
        "origin": "customer",
        "owner": "DfE",
        "quantity": "many",
        "confidentiality": "confidential",
        "integrity": "critical",
        "availability": "operational",
        "justification": "Student data might contain personally identifiable information (PII). The integrity and availability of student data is required for functioning of the service."
    }
    template_file = open("data_assets_template.yaml")
    template_str = template_file.read()
    data_asset_template = Template(template_str)
    data_asset_yaml = data_asset_template.render(data_asset_dict)

    student_pii_tags = data_asset_dict["tags_list"]

    return data_asset_yaml, student_pii_tags


def build_client_app_data_asset() -> tuple:
    data_asset_dict = {
        "name": "client-application-code",
        "description": "Client application code such as JavaScript and HTML.",
        "usage": "devops",
        "tags_list": ["client-application-code","github", "git", "code", "html", "javascript"],
        "origin": "DfE",
        "owner": "DfE",
        "quantity": "very-few",
        "confidentiality": "public",
        "integrity": "critical",
        "availability": "important",
        "justification": "The integrity of the application code is critical to avoid reputational damage and the availability is important on the long-term scale (but not critical) to ensure users are able to access the service."
    }
    template_file = open("data_assets_template.yaml")
    template_str = template_file.read()
    data_asset_template = Template(template_str)
    data_asset_yaml = data_asset_template.render(data_asset_dict)

    client_app_tags = data_asset_dict["tags_list"]

    return data_asset_yaml, client_app_tags


def build_server_app_data_asset() -> tuple:
    data_asset_dict = {
        "name": "server-application-code",
        "description": "Server application code such as JavaScript and HTML.",
        "usage": "devops",
        "tags_list": ["server-application-code","github", "git", "code", "ruby"],
        "origin": "DfE",
        "owner": "DfE",
        "quantity": "very-few",
        "confidentiality": "public",
        "integrity": "mission-critical",
        "availability": "important",
        "justification": "The integrity of the API code is critical to avoid reputational damage and the availability is important on the long-term scale (but not critical) to ensure users are able to access the service."
    }
    template_file = open("data_assets_template.yaml")
    template_str = template_file.read()
    data_asset_template = Template(template_str)
    data_asset_yaml = data_asset_template.render(data_asset_dict)

    server_app_tags = data_asset_dict["tags_list"]

    return data_asset_yaml, server_app_tags


def build_vulnerable_children_data_asset() -> tuple:
    data_asset_dict = {
        "name": "vulnerable-children-data",
        "description": "Names, addresses and sensitive details of vulnerable children.",
        "usage": "business",
        "tags_list": ["vulnerable-children-data","database", "azure", "sensitive", "pii"],
        "origin": "Customer",
        "owner": "DfE",
        "quantity": "many",
        "confidentiality": "strictly-confidential",
        "integrity": "mission-critical",
        "availability": "critical",
        "justification": "The data of vulnerable children is strictly confidential, and would cause serious harm if made public."
    }
    template_file = open("data_assets_template.yaml")
    template_str = template_file.read()
    data_asset_template = Template(template_str)
    data_asset_yaml = data_asset_template.render(data_asset_dict)

    vulnerable_children_data_tags = data_asset_dict["tags_list"]

    return data_asset_yaml, vulnerable_children_data_tags


def build_job_information_data_asset() -> tuple:
    data_asset_dict = {
        "name": "job-information",
        "description": "Names, addresses and sensitive details of vulnerable children.",
        "usage": "business",
        "tags_list": ["job-information","database", "azure", "public"],
        "origin": "DfE",
        "owner": "DfE",
        "quantity": "many",
        "confidentiality": "public",
        "integrity": "important",
        "availability": "operational",
        "justification": "Job information is important but is public information in it's nature."
    }
    template_file = open("data_assets_template.yaml")
    template_str = template_file.read()
    data_asset_template = Template(template_str)
    data_asset_yaml = data_asset_template.render(data_asset_dict)

    job_info_tags = data_asset_dict["tags_list"]

    return data_asset_yaml, job_info_tags


def build_school_data_asset() -> tuple:
    data_asset_dict = {
        "name": "school-data",
        "description": "School data, insights, statistics, and records.",
        "usage": "business",
        "tags_list": ["school-data","database", "azure", "internal"],
        "origin": "Schools",
        "owner": "DfE",
        "quantity": "very-many",
        "confidentiality": "internal",
        "integrity": "critical",
        "availability": "operational",
        "justification": "School data is collected to provide useful insights in how schools are doing from a social, financial and academic point of view, but most of this information is either already public or can be made available on request."
    }
    template_file = open("data_assets_template.yaml")
    template_str = template_file.read()
    data_asset_template = Template(template_str)
    data_asset_yaml = data_asset_template.render(data_asset_dict)

    school_data_tags = data_asset_dict["tags_list"]

    return data_asset_yaml, school_data_tags

def build_payment_details_asset() -> tuple:
    data_asset_dict = {
        "name": "payment-details",
        "description": "Payment details to receive or send money to/from users.",
        "usage": "business",
        "tags_list": ["payment-details","database", "azure", "sensitive", "pci", "bank-account-details"],
        "origin": "Customer",
        "owner": "DfE",
        "quantity": "many",
        "confidentiality": "strictly-confidential",
        "integrity": "critical",
        "availability": "important",
        "justification": "Payment details could be PCI or bank account details, either to take payments or to send money to/from the customer."
    }
    template_file = open("data_assets_template.yaml")
    template_str = template_file.read()
    data_asset_template = Template(template_str)
    data_asset_yaml = data_asset_template.render(data_asset_dict)

    teacher_pii_tags = data_asset_dict["tags_list"]

    return data_asset_yaml, teacher_pii_tags


def build_secrets_asset() -> tuple:
    data_asset_dict = {
        "name": "secrets-and-api-keys",
        "description": "Payment details to receive or send money to/from users.",
        "usage": "business",
        "tags_list": ["secrets-and-api-keys","keyvault", "azure", "sensitive", "azure-key-vault"],
        "origin": "DfE",
        "owner": "DfE",
        "quantity": "many",
        "confidentiality": "strictly-confidential",
        "integrity": "critical",
        "availability": "operational",
        "justification": "Secrets and API keys are critical and would result in serious breach and reputational damage if found."
    }
    template_file = open("data_assets_template.yaml")
    template_str = template_file.read()
    data_asset_template = Template(template_str)
    data_asset_yaml = data_asset_template.render(data_asset_dict)

    teacher_pii_tags = data_asset_dict["tags_list"]

    return data_asset_yaml, teacher_pii_tags