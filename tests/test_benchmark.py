import csv
import tempfile
import unittest
from pathlib import Path

from benchmark import export_csv, generate_dataset, run_test


class BenchmarkTest(unittest.TestCase):
    def test_generates_requested_dataset(self) -> None:
        self.assertEqual(["item_0", "item_1", "item_2"], generate_dataset(3))

    def test_runs_supported_backends(self) -> None:
        for backend in ("list", "dict"):
            with self.subTest(backend=backend):
                result = run_test(backend, dataset_size=10, iterations=3)
                self.assertEqual(backend, result["backend"])
                self.assertEqual(3, result["iterations"])

    def test_rejects_invalid_configuration(self) -> None:
        with self.assertRaises(ValueError):
            run_test("unknown", dataset_size=10, iterations=1)
        with self.assertRaises(ValueError):
            run_test("list", dataset_size=0, iterations=1)

    def test_exports_csv(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "results.csv"
            export_csv([run_test("dict", 5, 2)], output)

            with output.open(encoding="utf-8", newline="") as csv_file:
                rows = list(csv.DictReader(csv_file))
            self.assertEqual("dict", rows[0]["backend"])


if __name__ == "__main__":
    unittest.main()
