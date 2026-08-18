package io.github.chrisvdalen.benchmark;

import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.OptionsBuilder;

public final class BenchmarkRunner {
    private BenchmarkRunner() {
    }

    public static void main(String[] args) throws RunnerException {
        var options = new OptionsBuilder()
                .include(CollectionsBenchmark.class.getSimpleName())
                .forks(1)
                .build();
        new Runner(options).run();
    }
}
