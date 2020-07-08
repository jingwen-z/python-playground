from unittest.mock import Mock

mock = Mock()
print(mock)
print(mock.some_attribute)

# Patch the json library
json = mock
print(json.dumps())
