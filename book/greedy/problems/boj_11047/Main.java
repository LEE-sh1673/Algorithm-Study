package problems.boj_11047;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

class Result {

    public static int calculateNumberOfCoins(final int money, final List<Integer> coins) {
        int minCoinIdx = coins.indexOf(getMinCoin(money, coins));
        int numberOfCoins = 0;
        int currMoney = money;

        for (int i = minCoinIdx; i >= 0; i--) {
            int coin = coins.get(i);
            numberOfCoins += currMoney / coin;
            currMoney %= coin;
        }
        return numberOfCoins;
    }

    private static int getMinCoin(final int money, final List<Integer> coins) {
        return coins.stream()
            .filter(coin -> coin <= money)
            .max(Integer::compareTo)
            .orElseThrow(NoSuchElementException::new);
    }
}

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        List<Integer> input = Stream.of(br.readLine().split(" "))
            .map(Integer::parseInt)
            .collect(Collectors.toList());

        List<Integer> coins = new ArrayList<>();
        IntStream.range(0, input.get(0)).forEach(i -> {
            try {
                coins.add(Integer.parseInt(br.readLine().trim()));
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        int result = Result.calculateNumberOfCoins(input.get(1), coins);
        System.out.println(result);
        br.close();
    }
}
