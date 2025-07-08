
class Solution {
    public int maxValue(int[][] events, int k) {
        // Sort by end day
        Arrays.sort(events, (a, b) -> Integer.compare(a[1], b[1]));
        int n = events.length;

        // Extract start days to binary search later
        int[] ends = new int[n];
        for (int i = 0; i < n; i++) ends[i] = events[i][1];

        // DP table: dp[i][j] = max value using first i events and attending j
        int[][] dp = new int[n + 1][k + 1];

        for (int i = 1; i <= n; i++) {
            int[] curr = events[i - 1];
            int start = curr[0], end = curr[1], val = curr[2];

            // Find the last event that ends < start (non-overlapping)
            int l = binarySearch(events, i - 1, start);

            for (int j = 1; j <= k; j++) {
                // Option 1: skip current event
                dp[i][j] = Math.max(dp[i][j], dp[i - 1][j]);

                // Option 2: take current event + best before it
                dp[i][j] = Math.max(dp[i][j], dp[l + 1][j - 1] + val);
            }
        }

        return dp[n][k];
    }

    // Binary search to find last event that ends < start
    private int binarySearch(int[][] events, int right, int target) {
        int low = 0, high = right - 1;
        int res = -1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (events[mid][1] < target) {
                res = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return res;
    }
}
