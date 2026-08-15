class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size();

        vector<int>left(n);
        vector<int>right(n);
        int left_max=0;
        int right_max=0;
        
        for(int i=0;i<n;i++){
            left_max=max(left_max,height[i]);
            right_max=max(right_max,height[n-i-1]);
            left[i]=left_max;
            right[n-i-1]=right_max;
        }
        int sum=0;
        for(int i=0;i<n;i++){
            sum+=min(left[i],right[i])-height[i];
        }
        return sum;
    }
};
