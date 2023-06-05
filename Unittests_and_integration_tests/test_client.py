#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos(self):
        org_name = "testorg"
        repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        with patch('client.get_json') as mock_get_json, \
                patch('client.GithubOrgClient._public_repos_url',
                      new_callable=PropertyMock) as mock_public_repos_url:
            mock_get_json.return_value = repos_payload
            mock_public_repos_url.return_value = f"https://api.github.com/orgs/{org_name}/repos"

            client = GithubOrgClient(org_name)
            repos = client.public_repos

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                mock_public_repos_url.return_value)
            self.assertEqual(repos, repos_payload)
