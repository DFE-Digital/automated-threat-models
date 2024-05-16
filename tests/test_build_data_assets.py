import unittest

from build_data_assets import (
    build_teacher_pii_data_asset,
    build_student_pii_data_asset,
    build_client_app_data_asset,
    build_server_app_data_asset,
    build_vulnerable_children_data_asset,
    build_job_information_data_asset,
    build_school_data_asset,
    build_payment_details_asset,
    build_secrets_asset,
)


def lists_are_equal(expected_tag_list: list, tag_list: list) -> bool:
    return expected_tag_list == tag_list


class TestDataAssets(unittest.TestCase):

    maxDiff = None

    def test_build_teacher_pii_data_asset(self):
        data_asset_yaml, tag_list = build_teacher_pii_data_asset()

        expected_yaml = """  teacher-pii:
    name: teacher-pii
    id: teacher-pii
    description: Teachers personal information.
    usage: business # values: business, devops
    tags:
      - teacher-pii
      - database
      - azure
      - sensitive
      - pii
    origin: customer
    owner: DfE
    quantity: many # values: very-few, few, many, very-many
    confidentiality: confidential # values: public, internal, restricted, confidential, strictly-confidential
    integrity: critical # values: archive, operational, important, critical, mission-critical
    availability: operational # values: archive, operational, important, critical, mission-critical
    justification_cia_rating: >
      Teacher data might contain personally identifiable information (PII). The integrity and availability of teacher data is required for functioning of the service."""

        expected_tag_list = ["teacher-pii", "database", "azure", "sensitive", "pii"]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))

        self.assertEqual(expected_yaml, data_asset_yaml)

    def test_build_student_pii_data_asset(self):
        data_asset_yaml, tag_list = build_student_pii_data_asset()

        expected_yaml = """  student-pii:
    name: student-pii
    id: student-pii
    description: Students personal information.
    usage: business # values: business, devops
    tags:
      - student-pii
      - database
      - azure
      - sensitive
      - pii
    origin: customer
    owner: DfE
    quantity: many # values: very-few, few, many, very-many
    confidentiality: confidential # values: public, internal, restricted, confidential, strictly-confidential
    integrity: critical # values: archive, operational, important, critical, mission-critical
    availability: operational # values: archive, operational, important, critical, mission-critical
    justification_cia_rating: >
      Student data might contain personally identifiable information (PII). The integrity and availability of student data is required for functioning of the service."""

        expected_tag_list = ["student-pii", "database", "azure", "sensitive", "pii"]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))

        self.assertEqual(expected_yaml, data_asset_yaml)

    def test_build_client_app_data_asset(self):
        data_asset_yaml, tag_list = build_client_app_data_asset()

        expected_yaml = """  client-application-code:
    name: client-application-code
    id: client-application-code
    description: Client application code such as JavaScript and HTML.
    usage: devops # values: business, devops
    tags:
      - client-application-code
      - github
      - git
      - code
      - html
      - javascript
    origin: DfE
    owner: DfE
    quantity: very-few # values: very-few, few, many, very-many
    confidentiality: public # values: public, internal, restricted, confidential, strictly-confidential
    integrity: critical # values: archive, operational, important, critical, mission-critical
    availability: important # values: archive, operational, important, critical, mission-critical
    justification_cia_rating: >
      The integrity of the application code is critical to avoid reputational damage and the availability is important on the long-term scale (but not critical) to ensure users are able to access the service."""

        expected_tag_list = [
            "client-application-code",
            "github",
            "git",
            "code",
            "html",
            "javascript",
        ]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))

        self.assertEqual(expected_yaml, data_asset_yaml)

    def test_build_server_app_data_asset(self):
        data_asset_yaml, tag_list = build_server_app_data_asset()

        expected_yaml = """  server-application-code:
    name: server-application-code
    id: server-application-code
    description: Server application code such as JavaScript and HTML.
    usage: devops # values: business, devops
    tags:
      - server-application-code
      - github
      - git
      - code
      - ruby
    origin: DfE
    owner: DfE
    quantity: very-few # values: very-few, few, many, very-many
    confidentiality: public # values: public, internal, restricted, confidential, strictly-confidential
    integrity: mission-critical # values: archive, operational, important, critical, mission-critical
    availability: important # values: archive, operational, important, critical, mission-critical
    justification_cia_rating: >
      The integrity of the API code is critical to avoid reputational damage and the availability is important on the long-term scale (but not critical) to ensure users are able to access the service."""

        expected_tag_list = ["server-application-code", "github", "git", "code", "ruby"]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))

        self.assertEqual(expected_yaml, data_asset_yaml)

    def test_build_vulnerable_children_data_asset(self):
        data_asset_yaml, tag_list = build_vulnerable_children_data_asset()

        expected_yaml = """  vulnerable-children-data:
    name: vulnerable-children-data
    id: vulnerable-children-data
    description: Names, addresses and sensitive details of vulnerable children.
    usage: business # values: business, devops
    tags:
      - vulnerable-children-data
      - database
      - azure
      - sensitive
      - pii
    origin: Customer
    owner: DfE
    quantity: many # values: very-few, few, many, very-many
    confidentiality: strictly-confidential # values: public, internal, restricted, confidential, strictly-confidential
    integrity: mission-critical # values: archive, operational, important, critical, mission-critical
    availability: critical # values: archive, operational, important, critical, mission-critical
    justification_cia_rating: >
      The data of vulnerable children is strictly confidential, and would cause serious harm if made public."""

        expected_tag_list = [
            "vulnerable-children-data",
            "database",
            "azure",
            "sensitive",
            "pii",
        ]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))

        self.assertEqual(expected_yaml, data_asset_yaml)

    def test_build_job_information_data_asset(self):
        data_asset_yaml, tag_list = build_job_information_data_asset()

        expected_yaml = """  job-information:
    name: job-information
    id: job-information
    description: Names, addresses and sensitive details of vulnerable children.
    usage: business # values: business, devops
    tags:
      - job-information
      - database
      - azure
      - public
    origin: DfE
    owner: DfE
    quantity: many # values: very-few, few, many, very-many
    confidentiality: public # values: public, internal, restricted, confidential, strictly-confidential
    integrity: important # values: archive, operational, important, critical, mission-critical
    availability: operational # values: archive, operational, important, critical, mission-critical
    justification_cia_rating: >
      Job information is important but is public information in it's nature."""

        expected_tag_list = ["job-information", "database", "azure", "public"]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))

        self.assertEqual(expected_yaml, data_asset_yaml)

    def test_build_school_data_asset(self):
        data_asset_yaml, tag_list = build_school_data_asset()

        expected_yaml = """  school-data:
    name: school-data
    id: school-data
    description: School data, insights, statistics, and records.
    usage: business # values: business, devops
    tags:
      - school-data
      - database
      - azure
      - internal
    origin: Schools
    owner: DfE
    quantity: very-many # values: very-few, few, many, very-many
    confidentiality: internal # values: public, internal, restricted, confidential, strictly-confidential
    integrity: critical # values: archive, operational, important, critical, mission-critical
    availability: operational # values: archive, operational, important, critical, mission-critical
    justification_cia_rating: >
      School data is collected to provide useful insights in how schools are doing from a social, financial and academic point of view, but most of this information is either already public or can be made available on request."""

        expected_tag_list = ["school-data", "database", "azure", "internal"]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))

        self.assertEqual(expected_yaml, data_asset_yaml)

    def test_build_payment_details_asset(self):
        data_asset_yaml, tag_list = build_payment_details_asset()

        expected_yaml = """  payment-details:
    name: payment-details
    id: payment-details
    description: Payment details to receive or send money to/from users.
    usage: business # values: business, devops
    tags:
      - payment-details
      - database
      - azure
      - sensitive
      - pci
      - bank-account-details
    origin: Customer
    owner: DfE
    quantity: many # values: very-few, few, many, very-many
    confidentiality: strictly-confidential # values: public, internal, restricted, confidential, strictly-confidential
    integrity: critical # values: archive, operational, important, critical, mission-critical
    availability: important # values: archive, operational, important, critical, mission-critical
    justification_cia_rating: >
      Payment details could be PCI or bank account details, either to take payments or to send money to/from the customer."""

        expected_tag_list = [
            "payment-details",
            "database",
            "azure",
            "sensitive",
            "pci",
            "bank-account-details",
        ]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))

        self.assertEqual(expected_yaml, data_asset_yaml)

    def test_build_secrets_asset(self):
        data_asset_yaml, tag_list = build_secrets_asset()
        expected_yaml = """  secrets-and-api-keys:
    name: secrets-and-api-keys
    id: secrets-and-api-keys
    description: Payment details to receive or send money to/from users.
    usage: business # values: business, devops
    tags:
      - secrets-and-api-keys
      - keyvault
      - azure
      - sensitive
      - azure-key-vault
    origin: DfE
    owner: DfE
    quantity: many # values: very-few, few, many, very-many
    confidentiality: strictly-confidential # values: public, internal, restricted, confidential, strictly-confidential
    integrity: critical # values: archive, operational, important, critical, mission-critical
    availability: operational # values: archive, operational, important, critical, mission-critical
    justification_cia_rating: >
      Secrets and API keys are critical and would result in serious breach and reputational damage if found."""

        expected_tag_list = [
            "secrets-and-api-keys",
            "keyvault",
            "azure",
            "sensitive",
            "azure-key-vault",
        ]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))

        self.assertEqual(expected_yaml, data_asset_yaml)


if __name__ == "__main__":
    unittest.main()
