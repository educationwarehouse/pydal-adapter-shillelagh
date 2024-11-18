from pydal import DAL, Field

# noinspection PyUnresolvedReferences
# import is required, even though pacakge is not used, to set up rqlite:// for pyDAL
import pydal_shillelagh


def test_json():
    # db = DAL("rqlite://user:pass@localhost:4001", folder="database", driver_args={'https': False})
    db = DAL("shillelagh://:memory:", folder="database")
    # or with basic auth/custom port/https:
    # db = DAL("rqlite://user:pass@localhost:4001", folder="database", driver_args={'https': True})
    # db now works similarly to sqlite:
    # db = DAL("sqlite://:memory:", folder="database")

    db.define_table(
        'products',
        Field('title', 'string'),
        Field('description', 'text'),
        Field('category', 'string'),
        Field('price', 'double'),
        Field('discount_percentage', 'double'),
        Field('rating', 'double'),
        Field('stock', 'integer'),
        Field('tags', 'list:string'),
        Field('brand', 'string'),
        Field('sku', 'string'),
        Field('weight', 'double'),
        Field('dimensions_width', 'double'),
        Field('dimensions_height', 'double'),
        Field('dimensions_depth', 'double'),
        Field('warranty_information', 'text'),
        Field('shipping_information', 'text'),
        Field('availability_status', 'string'),
        Field('return_policy', 'text'),
        Field('minimum_order_quantity', 'integer'),
        Field('meta_created_at', 'datetime'),
        Field('meta_updated_at', 'datetime'),
        Field('meta_barcode', 'string'),
        Field('meta_qr_code', 'string'),
        Field('images', 'list:string'),
        Field('thumbnail', 'string')
    )

    rows = db.executesql(
        """
        SELECT * FROM 'https://dummyjson.com/products';
        """
    )

    print(rows)
