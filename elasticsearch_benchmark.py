import argparse
import json
import time
from typing import List, Dict, Any

from elasticsearch import Elasticsearch, helpers


def create_index(es: Elasticsearch, index: str, mapping: Dict[str, Any]) -> None:
    if es.indices.exists(index=index):
        es.indices.delete(index=index)
    es.indices.create(index=index, body=mapping)


def bulk_insert(es: Elasticsearch, index: str, docs: List[Dict[str, Any]]) -> None:
    actions = [{"_index": index, "_source": doc} for doc in docs]
    helpers.bulk(es, actions)


def benchmark_search(es: Elasticsearch, index: str, queries: List[Dict[str, Any]], runs: int) -> None:
    for q in queries:
        total_time = 0.0
        for _ in range(runs):
            start = time.time()
            es.search(index=index, body=q)
            total_time += time.time() - start
        avg = total_time / runs
        print(f"Query: {json.dumps(q)} took {avg:.4f}s on average over {runs} runs")


def load_json(path: str) -> Any:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main() -> None:
    parser = argparse.ArgumentParser(description="Elasticsearch full-text search benchmark")
    parser.add_argument('--host', default='http://localhost:9200', help='Elasticsearch host URL')
    parser.add_argument('--index', required=True, help='Index name to use for benchmarking')
    parser.add_argument('--mapping', required=True, help='Path to JSON mapping file')
    parser.add_argument('--documents', required=True, help='Path to JSON file with documents to index')
    parser.add_argument('--queries', required=True, help='Path to JSON file with search queries')
    parser.add_argument('--runs', type=int, default=5, help='Number of runs per query')
    args = parser.parse_args()

    es = Elasticsearch(args.host)

    mapping = load_json(args.mapping)
    docs = load_json(args.documents)
    queries = load_json(args.queries)

    create_index(es, args.index, mapping)
    bulk_insert(es, args.index, docs)
    es.indices.refresh(index=args.index)

    benchmark_search(es, args.index, queries, args.runs)


if __name__ == '__main__':
    main()
