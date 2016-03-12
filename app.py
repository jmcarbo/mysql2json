#!/usr/bin/env python 

import argparse
import json
import datetime
import pymysql

# Define a class to encode values to a json representation
class CustomEncoder(json.JSONEncoder):
   def default(self, obj):
      if isinstance(obj, set):
         return list(obj)
      if isinstance(obj, datetime.datetime):
         return obj.isoformat()
      return json.JSONEncoder.default(self, obj)


# Define the cli flags
parser = argparse.ArgumentParser()
parser.add_argument("--host", help="MySQL server host", type=str, default='localhost')
parser.add_argument("--port", help="server port", type=int, default=3306)
parser.add_argument("--database", help="default database", required=True, type=str)
parser.add_argument("--query", help="a SQL query", type=str)
parser.add_argument("--query_file", help="a SQL query file", type=str)
parser.add_argument("--user", help="username", required=True, type=str)
parser.add_argument("--password", help="password", type=str)
parser.add_argument("--charset", help="character set", type=str, default='utf8mb4')

# Parse the cli flags
args = parser.parse_args()

# Initialize the connection parameters
params = {
   'host': args.host,
   'user': args.user,
   'port': args.port,
   'db': args.database,
   'charset': args.charset,
   'cursorclass': pymysql.cursors.SSDictCursor
}

# Set the password parameter if one was given
if args.password:
   params['password'] = args.password

# Define a query value
query = None

# Read the query file if one was given and assign it to `query`
if args.query_file:
   query = open(args.query_file).read();

# Set the direct query value if one was given
if args.query:
   query = args.query;

# Validate the query value
if query == None:
   raise ValueError("No query or query_file given")

# Instantiate connection
connection = pymysql.connect(**params)

# Execute the query and iterate over the results
with connection.cursor() as cursor:
   cursor.execute(query)
   for result in cursor:
      print(json.dumps(result, cls=CustomEncoder))

# Close the database connection
connection.close()