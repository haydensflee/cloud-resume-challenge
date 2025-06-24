import unittest
from unittest.mock import patch
import app

class TestPutFunction(unittest.TestCase):
    @patch('app.table')
    def test_lambda_handler_success(self, mock_table):
        # Mock DynamoDB update_item response
        mock_table.update_item.return_value = {
            "Attributes": {"visitors": 5}
        }
        event = {}
        context = {}
        response = app.lambda_handler(event, context)
        self.assertEqual(response["statusCode"], 200)
        self.assertIn("count", response["body"])
        self.assertIn("Visitor count incremented", response["body"])

    @patch('app.table')
    def test_lambda_handler_missing_attributes(self, mock_table):
        # Simulate DynamoDB not returning Attributes
        mock_table.update_item.return_value = {}
        event = {}
        context = {}
        with self.assertRaises(KeyError):
            app.lambda_handler(event, context)

if __name__ == "__main__":
    unittest.main()