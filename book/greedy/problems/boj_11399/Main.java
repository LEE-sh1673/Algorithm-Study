package problems.boj_11399;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        List<Integer> periods = Stream.of(br.readLine().trim().split(" "))
            .map(Integer::parseInt)
            .sorted(Integer::compareTo)
            .collect(Collectors.toList());

        int answer = IntStream.range(0, periods.size())
            .map(idx -> (n - idx) * periods.get(idx))
            .sum();

        System.out.println(answer);
        br.close();
    }
}
