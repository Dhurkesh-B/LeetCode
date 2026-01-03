class Solution {
public:
    int numOfWays(int n) {
        const int MOD = 1e9 + 7;
        
        long long same = 6;  // ABA patterns
        long long diff = 6;  // ABC patterns
        
        for (int i = 2; i <= n; i++) {
            long long new_same = (same * 3 + diff * 2) % MOD;
            long long new_diff = (same * 2 + diff * 2) % MOD;
            
            same = new_same;
            diff = new_diff;
        }
        
        return (same + diff) % MOD;
    }
};
