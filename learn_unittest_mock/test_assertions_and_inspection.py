import unittest
from unittest.mock import Mock, call

# Create a mock object
json = Mock()
json.loads({'key': 'value'})
print(json)


class AssertionsTests(unittest.TestCase):
    def test_assertions(self):
        self.assertEqual(1, json.loads.call_count)
        self.assertEqual(call({'key': 'value'}), json.loads.call_args)
        self.assertEqual([call({'key': 'value'})], json.loads.call_args_list)
        self.assertEqual([call.loads({'key': 'value'})], json.method_calls)

        json.loads.assert_called()
        json.loads.assert_called_once()
        json.loads.assert_called_with({'key': 'value'})
        json.loads.assert_called_once_with({'key': 'value'})


if __name__ == '__main__':
    unittest.main()
