package io.github.chrisvdalen.benchmark;

import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Level;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Thread)
public class CollectionsBenchmark {
    @Param({"1000", "10000", "100000"})
    private int size;

    private int[] data;
    private Map<Integer, Integer> hashMap;
    private Map<Integer, Integer> treeMap;
    private List<Integer> arrayList;

    @Setup(Level.Iteration)
    public void setup() {
        data = new int[size];
        hashMap = HashMap.newHashMap(size);
        treeMap = new TreeMap<>();
        arrayList = new ArrayList<>(size);
        for (var index = 0; index < size; index++) {
            data[index] = index;
            hashMap.put(index, index);
            treeMap.put(index, index);
            arrayList.add(index);
        }
    }

    @Benchmark
    public Map<Integer, Integer> hashMapInsertion() {
        var map = HashMap.<Integer, Integer>newHashMap(size);
        for (var value : data) {
            map.put(value, value);
        }
        return map;
    }

    @Benchmark
    public Map<Integer, Integer> treeMapInsertion() {
        Map<Integer, Integer> map = new TreeMap<>();
        for (var value : data) {
            map.put(value, value);
        }
        return map;
    }

    @Benchmark
    public List<Integer> arrayListInsertion() {
        List<Integer> list = new ArrayList<>(size);
        for (var value : data) {
            list.add(value);
        }
        return list;
    }

    @Benchmark
    public int hashMapLookup() {
        return sumLookups(hashMap);
    }

    @Benchmark
    public int treeMapLookup() {
        return sumLookups(treeMap);
    }

    @Benchmark
    public int arrayListLookup() {
        var sum = 0;
        for (var value : data) {
            if (arrayList.contains(value)) {
                sum += value;
            }
        }
        return sum;
    }

    private int sumLookups(Map<Integer, Integer> map) {
        var sum = 0;
        for (var value : data) {
            var mapped = map.get(value);
            if (mapped != null) {
                sum += mapped;
            }
        }
        return sum;
    }
}
