import pytest
from cron_parser.constants import FIELD_NAMES, FIELD_RANGES

class TestConstants:
    """Test cases for the constants """

    @pytest.mark.parametrize("expected_name", ["minute", "hour", "day of month", "month", "day of week"])
    def test_field_names(self, expected_name):
        assert expected_name in FIELD_NAMES

    @pytest.mark.parametrize("field_name, expected_range", [
        ("minute", (0, 59)),
        ("hour", (0, 23)),
        ("day of month", (1, 31)),
        ("month", (1, 12)),
        ("day of week", (0, 6))
    ])
    def test_field_ranges(self, field_name, expected_range):
        assert FIELD_RANGES[field_name] == expected_range

    def test_field_names_order(self):
        expected_order = ["minute", "hour", "day of month", "month", "day of week"]
        assert FIELD_NAMES == expected_order

    def test_field_ranges_keys_match_field_names(self):
        assert set(FIELD_NAMES) == set(FIELD_RANGES.keys())

