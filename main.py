from typing import Dict
from pyairtable import Api
from pyairtable.formulas import match
import os


def load_airtable_data(api: Api, table_id: str, formula: match):
    table = api.table(os.environ["BASE_ID"], table_id)
    return table.all(formula=formula)


def generate_jobs_formula() -> match:
    return match({"Status": "Active"})


def generate_events_formula() -> match:
    return match({"Status": "Published"})


def main() -> int:
    airtable_api = Api(os.environ["AIRTABLE_AUTH"])
    open_jobs = load_airtable_data(
        airtable_api, "tblPOlCzOHDiu2NYC", generate_jobs_formula()
    )
    upcoming_events = load_airtable_data(
        airtable_api, "tblzcEGAmSqFskbae", generate_events_formula()
    )
    return open_jobs


BUFFER_PATH = os.environ["GITHUB_OUTPUT"]


def write_to_output(context: Dict[str, str]) -> None:
    """writes the keys (as variables) and values (as values) to the output buffer

    Args:
        context: variables and values

    Examples:
        In your project, use this function like:

        >>> write_to_output({"name": "John", ...})

        ``name`` will be the variable name and ``John`` is the value.
    """

    with open(BUFFER_PATH, "a") as _buffer:
        for var, val in context.items():
            _buffer.write(f"{var}={val}\r\n")


if __name__ == "__main__":
    # open_jobs = main()
    write_to_output({"Name": "John"})
