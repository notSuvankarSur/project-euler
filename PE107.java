package com.euler.defaultpackage;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class PE107 {

    private static final int vertices = 40;

    public int getMinimumVertex(boolean[] mst, int[] key) {
        int min = Integer.MAX_VALUE;
        int minVertex = -1;
        for (int i = 0; i < vertices; ++i) {
            if (!mst[i] && key[i] < min) {
                min = key[i];
                minVertex = i;
            }
        }
        return minVertex;
    }

    public int[] primMST(int[][] graph) {
        boolean[] mst = new boolean[vertices];
        int[] key = new int[vertices];
        int[] parent = new int[vertices];

        for (int i = 0; i < vertices; ++i) {
            key[i] = Integer.MAX_VALUE;
        }

        key[0] = 0;
        parent[0] = -1;

        for (int i = 0; i < vertices; ++i) {
            int minVertex = getMinimumVertex(mst, key);
            mst[minVertex] = true;
            for (int j = 0; j < vertices; ++j) {
                if (graph[minVertex][j] > 0) {
                    if (!mst[j] && key[j] > graph[minVertex][j]) {
                        key[j] = graph[minVertex][j];
                        parent[j] = minVertex;
                    }
                }
            }
        }
        return key;
    }

    public static void main(String[] args) {

        PE107 mst = new PE107();
        int[][] adjMatrix = new int[vertices][vertices];
        int x = 0, y = 0;
        try {
            BufferedReader br = new BufferedReader(new FileReader("G:\\Java\\p107_network.txt"));
            String line;
            while ((line = br.readLine()) != null) {
                String[] lineSplit = line.split(",");
                for (String s : lineSplit) {
                    if (s.equals("-")) {
                        adjMatrix[x][y] = 0;
                    } else {
                        adjMatrix[x][y] = Integer.parseInt(s);
                    }
//                    System.out.print(adjMatrix[x][y] + " ");
                    y++;
                }
                x++;
                y = 0;
//                System.out.println();
            }
            br.close();
        } catch (FileNotFoundException e) {
            System.out.println("Not Found");
        } catch (IOException e) {
            return;
        }
        int[] keys = mst.primMST(adjMatrix);
        int minimalWeight = 0, totalWeight = 0;
        for (int i : keys) {
            minimalWeight += i;
        }
        for (int i = 0; i < adjMatrix.length; ++i) {
            for (int j = i + 1; j < adjMatrix[i].length; ++j) {
                totalWeight += adjMatrix[i][j];
            }
        }
        System.out.println(minimalWeight + " " + totalWeight + " " + (totalWeight - minimalWeight));

    }
}
