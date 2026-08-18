import csv
import random
import time
from collections.abc import Callable
from datetime import UTC, datetime
from pathlib import Path

BenchmarkResult = dict[str, str | int | float]


def generate_dataset(size: int) -> list[str]:
    return [f"item_{i}" for i in range(size)]


def search_list(dataset: list[str], target: str) -> bool:
    return target in dataset


def search_dict(dataset: dict[str, bool], target: str) -> bool:
    return target in dataset


BACKENDS: dict[str, Callable[[list[str] | dict[str, bool], str], bool]] = {
    "list": search_list,
    "dict": search_dict,
}


def run_test(backend: str, dataset_size: int, iterations: int) -> BenchmarkResult:
    if backend not in BACKENDS:
        raise ValueError(f"Unknown backend: {backend}")
    if dataset_size < 1 or iterations < 1:
        raise ValueError("Dataset size and iterations must be positive")

    dataset = generate_dataset(dataset_size)
    if backend == "dict":
        dataset = {item: True for item in dataset}

    choices = list(dataset)
    search_func = BACKENDS[backend]
    random_generator = random.Random(42)
    times: list[float] = []
    for _ in range(iterations):
        target = random_generator.choice(choices)
        start = time.perf_counter()
        search_func(dataset, target)
        end = time.perf_counter()
        times.append((end - start) * 1000)

    return {
        "timestamp": datetime.now(UTC).isoformat(),
        "backend": backend,
        "dataset_size": dataset_size,
        "iterations": iterations,
        "avg_ms": sum(times) / len(times),
        "min_ms": min(times),
        "max_ms": max(times),
    }


def export_csv(results: list[BenchmarkResult], path: str | Path) -> None:
    if not results:
        return
    headers = list(results[0].keys())
    with Path(path).open("w", newline="", encoding="utf-8") as csvfile:
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
