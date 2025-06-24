import unittest
from unittest.mock import patch, MagicMock
import app

class TestLambdaHandler(unittest.TestCase):
    @patch('app.table')
    def test_lambda_handler_success(self, mock_table):
        # Mock DynamoDB response
        mock_table.get_item.return_value = {'Item': {'visitors': 42}}
        event = {}
        context = {}
        response = app.lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('visitors', response['body'])

    @patch('app.table')
    def test_lambda_handler_no_item(self, mock_table):
        mock_table.get_item.return_value = {}
        event = {}
        context = {}
        response = app.lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 404)

    @patch('app.table')
    def test_lambda_handler_exception(self, mock_table):
        mock_table.get_item.side_effect = Exception("DynamoDB error")
        event = {}
        context = {}
        response = app.lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 500)
        self.assertIn('error', response['body'])

if __name__ == '__main__':
    unittest.main()