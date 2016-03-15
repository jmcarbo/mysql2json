# mysql2json

Connects to a MySQL database and returns JSON formatted records

### Usage
```
python app -h
usage: python app [-h] [--host HOST] [--port PORT] --database DATABASE
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

### Sample Usage
```bash
python app \
  --host="localhost" \
  --port="3306" \
  --database="my_database" \
  --user="root" \
  --password="$password" \
  --query="SELECT * FROM USERS WHERE ID >= 100" \
  --charset="utf8mb4"
```
