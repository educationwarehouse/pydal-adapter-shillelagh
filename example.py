from pydal import DAL

# noinspection PyUnresolvedReferences
# import is required, even though pacakge is not used, to set up rqlite:// for pyDAL
import pydal_rqlite

if __name__ == '__main__':
    db = DAL("shillelagh://:memory:", folder="/tmp/database")

    rows = db.executesql(
        """
        SELECT stream.id, review.*
         FROM 'https://dummyjson.com/products#.products[*]' stream,  
             json_each(reviews) review
         WHERE stream.id > 25 LIMIT 1;
        """
    )

    print(rows)
