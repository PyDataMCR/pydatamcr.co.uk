from pyairtable import Api
import os


def main() -> int:
    airtable_api = Api(os.environ["AIRTABLE_AUTH"])
    return airtable_api.whoami()


if __name__ == "__main__":
    print(main())
