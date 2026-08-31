class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n=(int)cost.size();
        vector<int>c(n+1);
        c[0]=0;
        vector<int>dp(n+2);
        for(int i=1;i<=n;i++){
            c[i]=cost[i-1];
        }
        dp[0]=0;
        dp[1]=0;
        for(int i=2;i<=n+1;i++){
            cout<<c[i-1]<<c[i-2]<<endl;
            dp[i]=min((c[i-1]+dp[i-1]),(c[i-2]+dp[i-2]));
            cout<<dp[i]<<endl;
        }
        return dp[n+1];
    }
};
