from cron_parser.constants import FIELD_RANGES

class CronFieldExpander:
    """Expands cron field values into a list of valid times."""

    def __init__(self, field_name, field_value):
        self.field_name = field_name
        self.field_value = field_value
        self.start, self.end = FIELD_RANGES[field_name]

    def expand(self):
        """Main function to expand the cron field."""
        if self.field_value == "*":
            return list(range(self.start, self.end + 1))

        result = set()
        for part in self.field_value.split(","):
            result.update(self._expand_part(part))

        return sorted(result)

    def _expand_part(self, part):
        """Expands individual components of the cron field."""
        if "-" in part:
            return self._expand_range(part)
        elif "/" in part:
            return self._expand_step(part)
        else:
            return self._expand_single_value(part)

    def _expand_range(self, part):
        """Handles range values (e.g., 1-5 or 5-20/5)."""

        # Check if range includes a step (e.g., 5-20/5)
        if "/" in part:
            range_part, step = part.split("/")
            step = int(step)
        else:
            range_part, step = part, 1  # Default step = 1 if no step is provided

        # Now safely split the range (e.g., 5-20)
        range_start, range_end = map(int, range_part.split("-"))

        if range_start > range_end:
            raise ValueError(f"Start ({range_start}) cannot be greater than end ({range_end}) in range.")

        if range_start < self.start or range_end > self.end:
            raise ValueError(f"Invalid range {range_start}-{range_end} for {self.field_name}.")

        return range(range_start, range_end + 1, step)

    def _expand_step(self, part):
        """Handles step values (e.g., */15 or 5-30/5)."""
        step_start, step = part.split("/")
        step = int(step)

        if step_start == "*":
            return range(self.start, self.end + 1, step)

        step_start = int(step_start)
        if step_start < self.start or step_start > self.end:
            raise ValueError(f"Start value {step_start} out of range for {self.field_name}.")
        return range(step_start, self.end + 1, step)

    def _expand_single_value(self, part):
        """Handles single integer values (e.g., 5)."""
        value = int(part)
        if value < self.start or value > self.end:
            raise ValueError(f"Value {value} out of range for {self.field_name}.")
        return {value}

# Usage Example
def expand_field(field_value, field_name):
    """Helper function to expand a cron field using CronFieldExpander."""
    return CronFieldExpander(field_name, field_value).expand()
