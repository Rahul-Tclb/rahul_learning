##################################
import os
from datetime import date, datetime, time, timedelta, timezone
from decimal import Decimal
from uuid import UUID
import json
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from databricks.sdk import WorkspaceClient
w = WorkspaceClient()  # Uses your configured Databricks authentication
# for wh in w.warehouses.list():
#     print(wh.name)  # Find your serverless warehouse
# wh = w.warehouses.get(dbutils.secrets.get( catalog='fast_api',schema= 'sql_alchemy',key= 'serverless_starter_warehouse'))
# HOST = wh.odbc_params.hostname
# HTTP_PATH = wh.odbc_params.path

# host = HOST
# http_path = HTTP_PATH
# access_token = dbutils.secrets.get(    catalog="fast_api",    schema="sql_alchemy",    key="sql_aclhemy_access_token")
def read_uc_secret(full_name: str) -> str:
    # full_name = "catalog.schema.secret"
    resp = w.api_client.do(
        "GET",
        f"/api/2.1/unity-catalog/secrets/{full_name}",
        query={"include_value": "true"},
    )
    return resp["effective_value"]

catalog = "fast_api"
schema = "sql_alchemy"

access_token = read_uc_secret(f"{catalog}.{schema}.sql_aclhemy_access_token")
warehouse_id = read_uc_secret(f"{catalog}.{schema}.serverless_starter_warehouse")

wh = w.warehouses.get(warehouse_id)
host = wh.odbc_params.hostname
http_path = wh.odbc_params.path
catalog = 'fast_api'
schema = 'sql_alchemy'
##################################


##################################
from databricks.sqlalchemy import TIMESTAMP, TINYINT, DatabricksVariant
from sqlalchemy import (
	BigInteger,      # BIGINT
	Boolean,         # BOOLEAN
	Column,
	Date,            # DATE
	DateTime,        # TIMESTAMP_NTZ
	Integer,         # INTEGER
	Numeric,         # DECIMAL
	String,          # STRING
	Time,            # STRING
	Uuid,            # STRING
	create_engine,
	select,
)
from sqlalchemy.orm import DeclarativeBase, Session

extra_connect_args = {
	"_tls_verify_hostname": True,
	"user_agent_entry": "PySQL Example Script",
}


engine = create_engine(
	f"databricks://token:{access_token}@{host}?http_path={http_path}&catalog={catalog}&schema={schema}",
	connect_args=extra_connect_args, echo=True,
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

print('completed')
