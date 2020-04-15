from flask_app import app
from unittest import TestCase
from graphene.test import Client
import requests
import json


class TestCovid19BackendApi(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.headers = {"content-type": "application/json"}
        self.root = '/'
        self.graphql = '/graphql'

    def test_root(self):
        response = self.app.get(self.root, headers=self.headers).get_data()
        assert b'Covid19 Tracker GraphQL' in response

    def test_total_confirmed_global_query(self):
        payload = '{"query": "{totalConfirmedGlobal}"}'
        response = self.app.get(self.graphql, headers=self.headers, data=payload).get_json()
        parsed_json = json.loads(json.dumps(response))
        assert parsed_json['data']['totalConfirmedGlobal'] > 0

    def test_total_deaths_global_query(self):
        payload = '{"query": "{totalDeathsGlobal}"}'
        response = self.app.get(
            self.graphql, headers=self.headers, data=payload).get_json()
        parsed_json = json.loads(json.dumps(response))
        assert parsed_json['data']['totalDeathsGlobal'] > 0

    def test_total_recovered_global_query(self):
        payload = '{"query": "{totalRecoveredGlobal}"}'
        response = self.app.get(
            self.graphql, headers=self.headers, data=payload).get_json()
        parsed_json = json.loads(json.dumps(response))
        assert parsed_json['data']['totalRecoveredGlobal'] > 0
