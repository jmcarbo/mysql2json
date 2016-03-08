# mysql2python

Connects to a MySQL database and returns JSON formatted records

### Usage
```
python ./app.py -h
usage: app.py [-h] [--host HOST] [--port PORT] --database DATABASE
              [--query QUERY] [--query_file QUERY_FILE] --user USER
              [--password PASSWORD] [--charset CHARSET]

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           MySQL server host
  --port PORT           server port
  --database DATABASE   default database
  --query QUERY         a SQL query
  --query_file QUERY_FILE
                        a SQL query file
  --user USER           username
  --password PASSWORD   password
  --charset CHARSET     character set 
```