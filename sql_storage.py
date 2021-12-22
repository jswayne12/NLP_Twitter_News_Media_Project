import ibm_db
import ibm_db_sa
from sqlalchemy import create_engine
class Ibm_sql:
    #For privacy reasons, these portions will be left out
    def __init__(self):
        self.dsn_hostname = ""
        self.dsn_uid = ""
        self.dsn_pwd = ""
        self.dsn_driver = ""
        self.dsn_database = ""
        self.dsn_port = ""
        self.dsn_protocol = ""
        self.dsn_security = ""
    def database_connection_str(self):
        dsn = (
            "DRIVER={0};"
            "DATABASE={1};"
            "HOSTNAME={2};"
            "PORT={3};"
            "PROTOCOL={4};"
            "UID={5};"
            "PWD={6};"
            "SECURITY={7};").format(self.dsn_driver, self.dsn_database, self.dsn_hostname, self.dsn_port, self.dsn_protocol,
                                    self.dsn_uid, self.dsn_pwd, self.dsn_security)
        return dsn
    def create_database_connection(self):
        dsn = self.database_connection_str()
        try:
            self.conn = ibm_db.connect(dsn, "", "")
            print("Connected to database: ", self.dsn_database, "as user: ", self.dsn_uid, "on host: ", self.dsn_hostname)
            return self.conn
        except:
            print("Unable to connect: ", ibm_db.conn_errormsg())
            return self.conn
    def make_query(self, string):
        query = string
        conn = self.create_database_connection()
        try:
            stmt = ibm_db.prepare(conn, query)
            ibm_db.execute(stmt)
            print('Query successful')
        except:
            print('Query was not successful',  ibm_db.stmt_errormsg())
    def insert_data_to_sql(self, df):
        data = df
        engine = create_engine('ibm_db_sa://'+self.dsn_uid+':'+self.dsn_pwd +'@'+self.dsn_hostname+':'+self.dsn_port+'/'+self.dsn_database)
        data.to_sql(name="TWITTER_DATA", con=engine, if_exists='append', index=False)
    def close_connection(self):
        try:
            ibm_db.close(self.conn)
            print('You have successfully disconnected from database')
        except:
            print('You have not successfully disconnected from database')