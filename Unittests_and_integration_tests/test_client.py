#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
        "expected_repos": expected_repos},
    {"org_payload": org_payload, "repos_payload": repos_payload,
        "expected_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')

        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = [
            org_payload,
            repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient("testorg")
        repos = client.public_repos()

        self.assertEqual(repos, self.expected_repos)
