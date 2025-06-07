# Store Search Performance Tester

This repository provides simple benchmarking utilities for evaluating search backends.

## Elasticsearch Benchmark

`elasticsearch_benchmark.py` allows you to measure full-text search performance of an Elasticsearch cluster.

### Requirements

- Python 3.8+
- `elasticsearch` Python package (`pip install elasticsearch`)
- An accessible Elasticsearch server

### Usage

Prepare JSON files for the index mapping, documents to index, and search queries.

```bash
python3 elasticsearch_benchmark.py \
  --host http://localhost:9200 \
  --index test-index \
  --mapping mapping.json \
  --documents documents.json \
  --queries queries.json \
  --runs 5
```

The script creates the index (deleting an existing one if present), bulk inserts the provided documents, refreshes the index, and then executes each query multiple times, reporting the average execution time.

You can configure analyzers and mappings in the mapping JSON file to suit your documents.
