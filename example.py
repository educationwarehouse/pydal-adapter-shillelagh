from pydal import DAL

# noinspection PyUnresolvedReferences
# import is required, even though pacakge is not used, to set up rqlite:// for pyDAL
import pydal_rqlite

db = DAL("shillelagh://:memory:", folder="/tmp/database")

rows = db.executesql(
    """
    SELECT * FROM 'https://dummyjson.com/test';
    """
)

print(rows)
