import warnings
from sqlite3 import PARSE_DECLTYPES

from pydal.adapters import SQLite, adapters
from shillelagh.backends.apsw import db as shillelagh


@adapters.register_for("shillelagh")
class Shillelagh(SQLite):
    # todo: postgres variant via multicorn
    drivers = ("shillelagh",)

    def _initialize_(self):
        self.pool_size = 0
        # skip _initialize_ of SQLite, but do init it's super:
        super(SQLite, self)._initialize_()

        # self.dbpath = self.uri.split("://", 1)[1]

        if "detect_types" not in self.driver_args:
            self.driver_args["detect_types"] = PARSE_DECLTYPES

    def find_driver(self):
        self.driver_name = self.drivers[0]
        self.driver = shillelagh

    def _create_function_not_supported(self, *a, **kw):
        warnings.warn("create_function used but shillelagh does not support this!")

    def connector(self):
        connection = shillelagh.connect(self.uri.removeprefix("shillelagh://"))
        connection.create_function = self._create_function_not_supported
        return connection
