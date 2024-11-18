from pydal import DAL, Field

# noinspection PyUnresolvedReferences
# import is required, even though pacakge is not used, to set up rqlite:// for pyDAL
import pydal_shillelagh
import shillelagh

if __name__ == '__main__':
    db = DAL("shillelagh://temp.db", folder="/tmp/database")

    query = """
        SELECT stream.id, review.*
         FROM 'https://dummyjson.com/products#.products[*]' stream,  
             json_each(reviews) review
         WHERE stream.id > 25 LIMIT 1;
        """

    rows = db.executesql(
        query
    )
    print(rows)

    # or:
    db.define_table(
        'product',
        Field('title', 'string'),
        Field('description', 'text'),
        Field('category', 'string'),
        Field('price', 'double'),
        # ...
        rname="https://dummyjson.com/products#.products[*]"
    )

    rows = db(db.product.price > 10).select()

    print(rows)

    # or:
    from typedal import TypeDAL, TypedTable, TextField

    db = TypeDAL("shillelagh://temp.db", folder="/tmp/database")

    @db.define(rname="https://dummyjson.com/products#.products[*]")
    class TypedalProducts(TypedTable):
        title: str
        description = TextField()
        category: str
        price: float

    print(
        TypedalProducts.where(TypedalProducts.price > 10).collect()
    )
