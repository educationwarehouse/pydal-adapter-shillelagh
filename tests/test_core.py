from pydal import DAL

# noinspection PyUnresolvedReferences
# import is required, even though pacakge is not used, to set up rqlite:// for pyDAL
import pydal_rqlite


def test_json():
    # db = DAL("rqlite://user:pass@localhost:4001", folder="database", driver_args={'https': False})
    db = DAL("shillelagh://:memory:", folder="database")
    # or with basic auth/custom port/https:
    # db = DAL("rqlite://user:pass@localhost:4001", folder="database", driver_args={'https': True})
    # db now works similarly to sqlite:
    # db = DAL("sqlite://:memory:", folder="database")
    rows = db.executesql(
        """
        SELECT * FROM 'https://dummyjson.com/products';
        """
    )

    print(rows)
