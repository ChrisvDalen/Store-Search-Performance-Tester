# Store Search Performance Tester

This repository provides simple benchmarking utilities for evaluating search backends.

## Elasticsearch Benchmark
This repository contains a simple benchmarking script for PostgreSQL. It can be used to measure insert and query performance using custom SQL statements.

`elasticsearch_benchmark.py` allows you to measure full-text search performance of an Elasticsearch cluster.

### Requirements
## Requirements

- Python 3.8+
- PostgreSQL server
- Dependencies from `requirements.txt`
- `elasticsearch` Python package (`pip install elasticsearch`)
- An accessible Elasticsearch server

### Usage

Prepare JSON files for the index mapping, documents to index, and search queries.
Install dependencies:

```bash
python3 elasticsearch_benchmark.py \
  --host http://localhost:9200 \
  --index test-index \
  --mapping mapping.json \
  --documents documents.json \
  --queries queries.json \
  --runs 5
pip install -r requirements.txt
```

## Usage
The script creates the index (deleting an existing one if present), bulk inserts the provided documents, refreshes the index, and then executes each query multiple times, reporting the average execution time.

```
python postgres_benchmark.py \
    --conn "postgres://user:pass@localhost:5432/dbname" \
    --setup "CREATE TABLE IF NOT EXISTS items (id serial primary key, data text);" \
    --insert "INSERT INTO items (data) VALUES (%s)" \
    --query "SELECT id, data FROM items WHERE id = %s" \
    --num-inserts 1000 \
    --num-queries 1000
```

The script will output the time taken for insert and query operations along with throughput in operations per second.
You can configure analyzers and mappings in the mapping JSON file to suit your documents.
