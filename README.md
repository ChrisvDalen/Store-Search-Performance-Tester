# Store Search Performance Tester

This project provides microbenchmarks for common Java collections using JMH.
It measures insertion and lookup performance for `HashMap`, `TreeMap`, and
`ArrayList`.

## Running Benchmarks

Make sure Maven is installed, then build the shaded JAR and run it:

```bash
mvn package
java -jar target/store-search-performance-tester-1.0-SNAPSHOT.jar
```

JMH will execute the benchmarks and report the results.
