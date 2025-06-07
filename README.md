# Store Search Performance Tester

This repository contains a simple benchmarking script for PostgreSQL. It can be used to measure insert and query performance using custom SQL statements.
This project provides microbenchmarks for common Java collections using JMH.
It measures insertion and lookup performance for `HashMap`, `TreeMap`, and
`ArrayList`.

## Running Benchmarks
## Requirements

- Python 3.8+
- PostgreSQL server
- Dependencies from `requirements.txt`

Install dependencies:
Make sure Maven is installed, then build the shaded JAR and run it:

```bash
mvn package
java -jar target/store-search-performance-tester-1.0-SNAPSHOT.jar
pip install -r requirements.txt
```

## Usage

```
python postgres_benchmark.py \
    --conn "postgres://user:pass@localhost:5432/dbname" \
    --setup "CREATE TABLE IF NOT EXISTS items (id serial primary key, data text);" \
    --insert "INSERT INTO items (data) VALUES (%s)" \
    --query "SELECT id, data FROM items WHERE id = %s" \
    --num-inserts 1000 \
    --num-queries 1000
```

JMH will execute the benchmarks and report the results.
The script will output the time taken for insert and query operations along with throughput in operations per second.
