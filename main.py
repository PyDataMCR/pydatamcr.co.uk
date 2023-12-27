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
    return (open_jobs, airtable_api)


if __name__ == "__main__":
    print(main())
