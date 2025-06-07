import csv
import random
import time
from datetime import datetime
from typing import List, Dict


def generate_dataset(size: int) -> List[str]:
    return [f"item_{i}" for i in range(size)]


def search_list(dataset: List[str], target: str) -> bool:
    return target in dataset


def search_dict(dataset: Dict[str, bool], target: str) -> bool:
    return target in dataset


BACKENDS = {
    "list": search_list,
    "dict": search_dict,
}


def run_test(backend: str, dataset_size: int, iterations: int) -> Dict[str, float]:
    dataset = generate_dataset(dataset_size)
    if backend == "dict":
        dataset = {item: True for item in dataset}

    search_func = BACKENDS[backend]
    times = []
    for _ in range(iterations):
        target = random.choice(list(dataset))
        start = time.perf_counter()
        search_func(dataset, target)
        end = time.perf_counter()
        times.append((end - start) * 1000)

    return {
        "timestamp": datetime.now().isoformat(),
        "backend": backend,
        "dataset_size": dataset_size,
        "iterations": iterations,
        "avg_ms": sum(times) / len(times),
        "min_ms": min(times),
        "max_ms": max(times),
    }


def export_csv(results: List[Dict[str, float]], path: str) -> None:
    if not results:
        return
    headers = list(results[0].keys())
    with open(path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in results:
            writer.writerow(row)


def main() -> None:
    configs = [
        ("list", 1000, 1000),
        ("dict", 1000, 1000),
    ]
    results = [
        run_test(backend, size, iters) for backend, size, iters in configs
    ]
    export_csv(results, "benchmark_results.csv")
    print("Results exported to benchmark_results.csv")


if __name__ == "__main__":
    main()
