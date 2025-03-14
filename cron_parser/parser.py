from cron_parser.utils import expand_field
from cron_parser.constants import FIELD_NAMES

class Parser:
    """Parses and expands cron expressions."""

    def __init__(self, cron_string: str):
        self.cron_string = cron_string
        self.parsed_fields = {}
        self.command = None

    def parse(self):
        """Parses the cron expression and expands each field."""
        parts = self.cron_string.split()

        # Validate number of fields
        if len(parts) < 6:
            raise ValueError(f"Invalid cron format! Expected 5 fields + command, got {len(parts)}.")

        cron_fields = parts[:5]
        self.command = " ".join(parts[5:])

        # Expand each field and print debug info
        for i, field in enumerate(cron_fields):
            try:
                expanded = expand_field(field, FIELD_NAMES[i])
                self.parsed_fields[FIELD_NAMES[i]] = expanded
            except Exception as e:
                raise ValueError(f"Invalid cron field '{field}' for {FIELD_NAMES[i]}: {e}")

    def format_output(self):
        """Formats the parsed fields as a table."""
        output = []
        for field_name, values in self.parsed_fields.items():
            output.append(f"{field_name:<14} {' '.join(map(str, values))}")

        output.append(f"{'command':<14} {self.command}")
        return "\n".join(output)

    def run(self):
        """Parses and prints the formatted output."""
        self.parse()
        print(self.format_output())
