import unittest

from build_tech_assets import (
    build_container_app_tm,
    build_key_vault_tm,
    build_cache_tm,
    build_app_service_tm,
    build_storage_tm,
)


def lists_are_equal(expected_tag_list: list, tag_list: list) -> bool:
    return expected_tag_list == tag_list


def yaml_contains_correct_values(yaml: str, name: str, asset_type: str) -> bool:

    if f"id: {name}" in yaml and f"description: {asset_type.split('/')[0]}" in yaml:
        return True
    else:
        return False


def app_service_yaml_contains_correct_values(
    yaml: str, name: str, asset_type: str, machine: str, technology: str
) -> bool:

    if f"id: {name}" in yaml and f"description: {asset_type.split('/')[0]}" in yaml:
        print("ok")
    else:
        return False

    if f"machine: {machine}" in yaml and f"technology: {technology}" in yaml:
        return True
    else:
        return False


class TestDataAssets(unittest.TestCase):

    def test_build_container_app_tm(self):
        name = "test_container_app_name"
        asset_type = "test_container_app_asset_type/test"
        container_app_asset_yaml, tag_list = build_container_app_tm(name, asset_type)

        expected_tag_list = [
            "test_container_app_name",
            "azure",
            "azure-container-app",
            "test_container_app_asset_type/test",
        ]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))
        self.assertTrue(
            yaml_contains_correct_values(container_app_asset_yaml, name, asset_type)
        )

    def test_build_key_vault_tm(self):
        name = "test_key_vault_name"
        asset_type = "test_key_vault_asset_type/test"
        key_vault_asset_yaml, tag_list = build_key_vault_tm(name, asset_type)

        expected_tag_list = [
            "test_key_vault_name",
            "azure",
            "azure-key-vault",
            "vault",
            "secrets",
            "keys",
            "test_key_vault_asset_type/test",
        ]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))
        self.assertTrue(
            yaml_contains_correct_values(key_vault_asset_yaml, name, asset_type)
        )

    def test_build_cache_tm(self):
        name = "test_build_cache_name"
        asset_type = "test_build_cache_asset_type/test"
        build_cache_asset_yaml, tag_list = build_cache_tm(name, asset_type)

        expected_tag_list = [
            "test_build_cache_name",
            "azure",
            "azure-redis-cache",
            "cache",
            "test_build_cache_asset_type/test",
        ]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))
        self.assertTrue(
            yaml_contains_correct_values(build_cache_asset_yaml, name, asset_type)
        )

    def test_build_storage_tm(self):
        name = "test_build_storage_name"
        asset_type = "test_build_storage_asset_type/test"
        build_storage_asset_yaml, tag_list = build_storage_tm(name, asset_type)

        expected_tag_list = [
            "test_build_storage_name",
            "azure",
            "azure-storage",
            "blob",
            "test_build_storage_asset_type/test",
        ]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))
        self.assertTrue(
            yaml_contains_correct_values(build_storage_asset_yaml, name, asset_type)
        )

    def test_build_app_service_tm(self):
        name = "test_build_storage_name"
        asset_type = "test_build_storage_asset_type/test"
        kind = "functionapp,linux"
        machine = "serverless"
        technology = "function"
        app_service_asset_yaml, tag_list = build_app_service_tm(name, asset_type, kind)

        expected_tag_list = [
            "test_build_storage_name",
            "azure",
            "azure-app-service",
            "serverless",
            "function",
            "test_build_storage_asset_type/test",
        ]

        self.assertTrue(lists_are_equal(expected_tag_list, tag_list))
        self.assertTrue(
            app_service_yaml_contains_correct_values(
                app_service_asset_yaml, name, asset_type, machine, technology
            )
        )


if __name__ == "__main__":
    unittest.main()
