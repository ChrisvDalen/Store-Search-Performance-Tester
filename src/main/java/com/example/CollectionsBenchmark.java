package com.example;

import java.util.*;
import org.openjdk.jmh.annotations.*;

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
        for (int i = 0; i < size; i++) {
            data[i] = i;
        }
        hashMap = new HashMap<>(size);
        treeMap = new TreeMap<>();
        arrayList = new ArrayList<>(size);
        for (int value : data) {
            hashMap.put(value, value);
            treeMap.put(value, value);
            arrayList.add(value);
        }
    }

    @Benchmark
    public Map<Integer, Integer> hashMapInsertion() {
        Map<Integer, Integer> map = new HashMap<>(size);
        for (int value : data) {
            map.put(value, value);
        }
        return map;
    }

    @Benchmark
    public Map<Integer, Integer> treeMapInsertion() {
        Map<Integer, Integer> map = new TreeMap<>();
        for (int value : data) {
            map.put(value, value);
        }
        return map;
    }

    @Benchmark
    public List<Integer> arrayListInsertion() {
        List<Integer> list = new ArrayList<>(size);
        for (int value : data) {
            list.add(value);
        }
        return list;
    }

    @Benchmark
    public int hashMapLookup() {
        int sum = 0;
        for (int value : data) {
            Integer v = hashMap.get(value);
            if (v != null) {
                sum += v;
            }
        }
        return sum;
    }

    @Benchmark
    public int treeMapLookup() {
        int sum = 0;
        for (int value : data) {
            Integer v = treeMap.get(value);
            if (v != null) {
                sum += v;
            }
        }
        return sum;
    }

    @Benchmark
    public int arrayListLookup() {
        int sum = 0;
        for (int value : data) {
            if (arrayList.contains(value)) {
                sum += value;
            }
        }
        return sum;
    }
}

