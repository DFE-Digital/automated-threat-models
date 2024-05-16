import unittest

from produce_risk_tracker import build_risk


class TestRiskBuilder(unittest.TestCase):

    def test_build_risk(self):
        risk_dict = {
            "name": "test_asset@test_test",
            "status": "mitigated",
            "justification": "Because security.",
            "ticket": "XXX-YYY",
            "date": "2024-05-16",
            "checked_by": "pritchyspritch",
        }
        risk_yaml = build_risk(risk_dict)

        expected_yaml = """  test_asset@test_test: # wildcards "*" between the @ characters are possible
    status: mitigated # values: unchecked, in-discussion, accepted, in-progress, mitigated, false-positive
    justification: Because security.
    ticket: XXX-YYY
    date: 2024-05-16
    checked_by: pritchyspritch"""

        self.assertEqual(expected_yaml, risk_yaml)


if __name__ == "__main__":
    unittest.main()
