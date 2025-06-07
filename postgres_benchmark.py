import argparse
import random
import string
import time

import psycopg2


def random_text(length=10):
    """Generate random alphanumeric text."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def main():
    parser = argparse.ArgumentParser(description="PostgreSQL benchmark tool")
    parser.add_argument("--conn", required=True, help="PostgreSQL connection string")
    parser.add_argument("--setup", help="SQL statement to run before benchmarking")
    parser.add_argument("--insert", required=True, help="Parameterized INSERT SQL")
    parser.add_argument("--query", required=True, help="Parameterized SELECT SQL")
    parser.add_argument("--num-inserts", type=int, default=1000, help="Number of rows to insert")
    parser.add_argument("--num-queries", type=int, default=1000, help="Number of queries to run")
    args = parser.parse_args()

    with psycopg2.connect(args.conn) as conn:
        with conn.cursor() as cur:
            if args.setup:
                cur.execute(args.setup)
                conn.commit()

            start = time.time()
            for _ in range(args.num_inserts):
                cur.execute(args.insert, (random_text(20),))
            conn.commit()
            insert_time = time.time() - start

            start = time.time()
            for _ in range(args.num_queries):
                idx = random.randint(1, args.num_inserts)
                cur.execute(args.query, (idx,))
                cur.fetchone()
            query_time = time.time() - start

    print(f"Inserted {args.num_inserts} rows in {insert_time:.2f}s ({args.num_inserts/insert_time:.2f} rows/s)")
    print(f"Executed {args.num_queries} queries in {query_time:.2f}s ({args.num_queries/query_time:.2f} q/s)")


if __name__ == "__main__":
    main()
