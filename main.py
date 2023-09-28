"""
ETL-Query script
"""

from mylib.lib import extract
from mylib.lib import load
from mylib.lib import query

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query
print("Querying data...")
query()


# if __name__ == "__main__":
#     # pylint: disable=no-value-for-parameter
