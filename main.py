from pyairtable import Api
from pyairtable.formulas import match
import os


def load_open_jobs(api: Api, table_id: str):
    # formula = match({"Status": "Active"})
    table = api.table(os.environ["BASE_ID"], table_id)
    return table.all()


def main() -> int:
    airtable_api = Api(os.environ["AIRTABLE_AUTH"])
    open_jobs = load_open_jobs(airtable_api, "tblPOlCzOHDiu2NYC")
    return open_jobs


if __name__ == "__main__":
    print(main())
