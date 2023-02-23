#!/usr/bin/env python3
"This is a line of text"
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    "This is a line of text"
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, name, mock):
        "This is a line of text"
        client_url = GithubOrgClient(name)
        self.assertEqual(client_url.org, mock.return_value)
        mock.assert_called_once

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_public_repos_url(self, name):
        "This is a line of text"
        url = "https://api.github.com/orgs/{}/repos".format(name)
        result = {"repos_url": url}
        with patch("client.GithubOrgClient.org",
                   PropertyMock(return_value=result)):
            client_url = GithubOrgClient(name)
            self.assertEqual(client_url._public_repos_url, url)

    @patch("client.get_json")
    def test_public_repos(self, mock):
        "This is a line of text"
        res = [{"name": "google"}, {"name": "abc"}]
        mock.return_value = res
        with patch("client.GithubOrgClient._public_repos_url",
                   PropertyMock(return_value=res)) as public:
            client_url = GithubOrgClient("test")
            self.assertEqual(client_url.public_repos(), ["google", "abc"])
            mock.assert_called_once()
            public.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, check):
        "This is a line of text"
        client_url = GithubOrgClient("test")
        self.assertEqual(client_url.has_license(repo, key), check)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    "This is a line of text"
    @classmethod
    def setUpClass(cls):
        "This is a line of text"
        config = {
            "return_value.json.side_effect": [
                cls.org_payload, cls.repos_payload,
                cls.org_payload, cls.repos_payload
            ]
        }
        cls.get_patcher = patch("requests.get", **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        "This is a line of text"
        cls.get_patcher.stop()

    def test_public_repos(self):
        "This is a line of text"
        client_url = GithubOrgClient("test")
        self.assertEqual(client_url.org, self.org_payload)
        self.assertEqual(client_url.repos_payload, self.repos_payload)
        self.assertEqual(client_url.public_repos(), self.expected_repos)
        self.assertEqual(client_url.public_repos("test"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        "This is a line of text"
        client_url = GithubOrgClient("test")
        a = "apache-2.0"
        self.assertEqual(client_url.org, self.org_payload)
        self.assertEqual(client_url.repos_payload, self.repos_payload)
        self.assertEqual(client_url.public_repos(), self.expected_repos)
        self.assertEqual(client_url.public_repos("test"), [])
        self.assertEqual(client_url.public_repos(a), self.apache2_repos)
        self.mock.assert_called()
