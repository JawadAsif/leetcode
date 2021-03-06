class Solution {
    private int[] coins, count;

    public int coinChange(int[] coins, int amount) {
        this.coins = coins;
        this.count = new int[amount + 1];
        return dp(amount);
    }

    private int dp(int remainder) {
        if (remainder == 0)
            return 0;
        if (remainder < 0)
            return -1;
        if (count[remainder] != 0)
            return count[remainder];

        int min = Integer.MAX_VALUE;
        for (int coin : coins) {
            int res = dp(remainder - coin);
            if (res >= 0 && res < min) {
                min = 1 + res;
            }
        }
        if (min == Integer.MAX_VALUE) {
            count[remainder] = -1;
        } else {
            count[remainder] = min;
        }
        return count[remainder];
    }
}