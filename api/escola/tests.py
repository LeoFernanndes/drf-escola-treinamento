import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.core.management import call_command


class TestCreateEscola(TestCase):
    @classmethod
    def setUpClass(cls):
        call_command("loaddata", "endereco")
        call_command("loaddata", "escola")
        pass

    def setUp(self):
        pass

    def test_create_escola_201(self):
        url = reverse('escolas-list')

        payload = {
            "endereco": {
                "logradouro": "string",
                "endereco": "string",
                "numero": 0,
                "complemento": "string",
                "cep": "string",
                "bairro": "string",
                "cidade": "string",
                "estado": "string"
            },
            "nome": "string"
        }

        expected_result = {'endereco': {'id': 4, 'logradouro': 'string', 'endereco': 'string', 'numero': 0,
                                                 'complemento': 'string', 'cep': 'string', 'bairro': 'string',
                                                 'cidade': 'string', 'estado': 'string'}, 'nome': 'string'}

        response = self.client.post(url, payload, content_type="application/json")
        json_response = json.loads(response.content)
        json_response.pop('id')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response, expected_result)

    def test_list_escolas_200(self):
        url = reverse('escolas-list')

        expected_result = [
            {'id': 1,
             'endereco': {'id': 1, 'logradouro': 'Avenida', 'endereco': 'Paulista', 'numero': 1301,
                          'complemento': '', 'cep': '00000-000', 'bairro': 'Centro',
                          'cidade': 'São Paulo', 'estado': 'SP'}, 'nome': 'string'},
            {'id': 2,
             'endereco': {
                 'id': 2,
                 'logradouro': 'Rua',
                 'endereco': 'XV de novembro',
                 'numero': 32,
                 'complemento': 'sala 11',
                 'cep': '00000-000',
                 'bairro': 'Alto da XV',
                 'cidade': 'Curitiba',
                 'estado': 'PR'},
             'nome': 'string'},
            {'id': 3,
             'endereco': {'id': 3, 'logradouro': 'Avenida', 'endereco': '7 de setembro', 'numero': 1034,
                          'complemento': '', 'cep': '00000-000', 'bairro': 'Centro',
                          'cidade': 'Guarulhos', 'estado': 'SP'}, 'nome': 'string'}
        ]

        response = self.client.get(url, content_type="application/json")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response, expected_result)

    def test_update_escola_200(self):
        url = reverse('escolas-detail', kwargs={'pk': 2})

        payload = {
            "endereco": {
                "logradouro": "string",
                "endereco": "string",
                "numero": 1,
                "complemento": "string",
                "cep": "string",
                "bairro": "string",
                "cidade": "string",
                "estado": "string"
            },
            "nome": "string"
        }

        expected_result = {'id': 2, 'endereco': {'id': 2, 'logradouro': 'string', 'endereco': 'string', 'numero': 1,
                                                 'complemento': 'string', 'cep': 'string', 'bairro': 'string',
                                                 'cidade': 'string', 'estado': 'string'}, 'nome': 'string'}

        response = self.client.put(url, payload, content_type="application/json")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response, expected_result)

    def test_partial_update_escola_200(self):
        url = reverse('escolas-detail', kwargs={'pk': 1})

        payload = {
            "endereco": {
                "logradouro": "string",
                "endereco": "string",
                "numero": 1,
                "complemento": "string",
                "cep": "string"
            },
            "nome": "string"
        }

        expected_result = {'id': 1, 'endereco': {'id': 1, 'logradouro': 'string', 'endereco': 'string', 'numero': 1,
                                                 'complemento': 'string', 'cep': 'string', 'bairro': 'Centro',
                                                 'cidade': 'São Paulo', 'estado': 'SP'}, 'nome': 'string'}

        response = self.client.patch(url, payload, content_type="application/json")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response, expected_result)

    def test_delete_escola_204(self):
        url = reverse('escolas-detail', kwargs={'pk': 1})
        response = self.client.delete(url, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    @classmethod
    def tearDownClass(cls):
        pass
