class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        int l=0,r=0;
        for (int num:nums){
            l=max(l,num);
            r+=num;
        }
        int mid;
        int ans=INT_MAX;
        while(l<=r){
           mid=(l+r)/2;
           cout<<mid<<endl;
           int cnt=0;
           int sum=0;
           for(int i=0;i<(int)nums.size();i++){
              sum+=nums[i];
              if(sum>mid){
                cnt++;
                sum=nums[i];
              }
              cout<<"sum"<<sum<<endl;
           } 
           cout<<"sum"<<sum<<endl;
           if(sum>0){
            cnt++;
           }
           if(cnt>k){
            l=mid+1;
           }else{
            ans=min(ans,mid);
            r=mid-1;
           }
        }
        return ans;
    }
};