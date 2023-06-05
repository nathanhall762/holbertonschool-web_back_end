#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from utils import access_nested_map, get_json, memoize


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    def test_org(self, org_name):
        expected_result = {"org": org_name}

        with patch('client.get_json') as mock_get_json:
            mock_get_json.return_value = expected_result

            client = GithubOrgClient(org_name)
            result = client.org

            mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")
            self.assertEqual(result, expected_result)

    def test_public_repos_url(self):
        org_name = "testorg"
        expected_url = f"https://api.github.com/orgs/{org_name}/repos"

        with patch('client.GithubOrgClient.org', return_value={"login": org_name}):
            client = GithubOrgClient(org_name)
            result = client._public_repos_url

            self.assertEqual(result, expected_url)
