# Store Search Performance Tester

Reproducible benchmarks for Java collections, PostgreSQL and Elasticsearch.

## Requirements

- Java 25
- Python 3.14
- PostgreSQL or Elasticsearch 9.5 when running their integration benchmarks

## Verify the project

```bash
./mvnw verify
python -m venv .venv
source .venv/bin/activate
python -m pip install --requirement requirements-dev.txt
python -m ruff check .
python -m unittest discover --verbose
```

## Java collections benchmark

```bash
./mvnw package
java -jar target/store-search-performance-tester-1.0-SNAPSHOT.jar
```

## PostgreSQL benchmark

```bash
python postgres_benchmark.py \
  --conn "postgres://user:pass@localhost:5432/dbname" \
  --setup "CREATE TABLE IF NOT EXISTS items (id serial primary key, data text)" \
  --insert "INSERT INTO items (data) VALUES (%s)" \
  --query "SELECT id, data FROM items WHERE id = %s"
```

## Elasticsearch benchmark

```bash
python elasticsearch_benchmark.py \
  --host http://localhost:9200 \
  --index test-index \
  --mapping mapping.json \
  --documents documents.json \
  --queries queries.json \
  --runs 5
```

The Elasticsearch benchmark deletes and recreates the selected index. Use a disposable index.
