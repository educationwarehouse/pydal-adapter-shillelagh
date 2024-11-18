import warnings
from sqlite3 import PARSE_DECLTYPES

from pydal.adapters import SQLite, adapters
from shillelagh.backends.apsw import db as shillelagh

PREFIX = "shillelagh"


@adapters.register_for(PREFIX)
class Shillelagh(SQLite):
    # todo: postgres variant via multicorn
    drivers = (shillelagh,)

    def _initialize_(self):
        self.pool_size = 0
        # skip _initialize_ of SQLite, but do init it's super:
        super(SQLite, self)._initialize_()

        if "detect_types" not in self.driver_args:
            self.driver_args["detect_types"] = PARSE_DECLTYPES

    def find_driver(self):
        self.driver_name = self.drivers[0]
        self.driver = shillelagh

    def _create_function_not_supported(self, *a, **kw):
        warnings.warn("`create_function` used but `shillelagh` does not support this!")

    def create_sequence_and_triggers(self, query, table, **args):
        uri = table._rname
        try:
            self.cursor._create_table(uri)
        except Exception:
            # maybe don't ignore?
            pass

    def select(self, query, fields, attributes):
        print(f"{query = }; {fields = }; {attributes =}")
        return super().select(query, fields, attributes)


    def connector(self):
        uri: str = self.uri.removeprefix(f"{PREFIX}://")
        if self.folder:
            uri = f"{self.folder}/{uri}"

        connection = shillelagh.connect(uri)
        connection.create_function = self._create_function_not_supported
        return connection
