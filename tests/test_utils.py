import pytest
import json
import re
from pathlib import Path
from cron_parser.utils import expand_field

TEST_DATA_PATH = Path(__file__).parent.parent / "test_data" / "expand_fields.json"
with open(TEST_DATA_PATH, "r") as file:
    test_cases = json.load(file)

class TestExpandField:
    """Test cases for the expand_field function."""

    @pytest.mark.parametrize("field_name, field_value, expected_output", [
        (case["field_name"], case["field_value"], case["expected_output"])
        for case in test_cases["valid"]
    ])
    def test_valid_expand_field(self, field_name, field_value, expected_output):
        assert expand_field(field_value, field_name) == expected_output

    @pytest.mark.parametrize("field_name, field_value, expected_exception, error_message", [
        (case["field_name"], case["field_value"], eval(case["expected_exception"]), case["error_message"])
        for case in test_cases["invalid"]
    ])
    def test_invalid_expand_field(self, field_name, field_value, expected_exception, error_message):
        with pytest.raises(expected_exception, match=re.escape(error_message)):
            expand_field(field_value, field_name)
