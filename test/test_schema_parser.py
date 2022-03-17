from src.publish_schema.schema_parser import add_numbers

def test_add_numbers():
    assert add_numbers(1, 3) == 4
