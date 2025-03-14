import pytest
import json
from cron_parser.parser import Parser
from pathlib import Path

TEST_DATA_PATH = Path(__file__).parent.parent / "test_data" / "crons.json"

with open(TEST_DATA_PATH, "r") as file:
    test_cases = json.load(file)


class TestParser:
    """Test cases for the Parser class."""

    @pytest.mark.parametrize("test_data", test_cases["valid"])
    def test_valid_cron(self, test_data):
        cron_string = test_data["cron"]
        expected_output = test_data["expected"]

        parser = Parser(cron_string)
        parser.parse()

        assert parser.parsed_fields == {k: v for k, v in expected_output.items() if k != "command"}
        assert parser.command == expected_output["command"]

    @pytest.mark.parametrize("cron_string", test_cases["invalid"])
    def test_invalid_cron(self, cron_string):
        with pytest.raises(ValueError):
            parser = Parser(cron_string)
            parser.parse()

