import sqlite3
import constants as constants
import functools



# conn = None
# def connector(f):
#     def with_connection_(*args, **kwargs):
#         global conn
#         if not conn:
#             conn = sqlite3.connect(constants.SQLALCHEMY_DATABASE)
#         try:
#             rv = f(conn, *args, **kwargs)
#         except Exception:
#             raise "Something wrong happened in the DAO function."
#         else:
#             conn.commit() # or maybe not  
#         finally:
#             conn.close()
#         return rv

#     return with_connection_


class ConnectionDecorator(object):

    @staticmethod
    def open_conn(f):
        @functools.wraps(f)
        def decorated(self, *args, **kwargs):  
            self.open_connection()
            try:
                returned = f(self, *args, **kwargs)
                return returned
            except Exception as e:
                print(e)
                raise e
            finally:
                self.close_connection()

        return decorated


class BasicDAO(object):

    def __init__(self) -> None:
        super().__init__()
        self.conn = None

    def open_connection(self):
        if self.conn is None:
            self.conn = sqlite3.connect(constants.SQLALCHEMY_DATABASE)


    def close_connection(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
