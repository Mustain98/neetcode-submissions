class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        set<int>s;
        int m=0;
        for(int num:nums){
            m=max(m,num);
            if(num>0){
                s.insert(num);
            }
        }

        for(int i=1;i<=m+1;i++){
            if(s.find(i)==s.end()){
                return i;
            }
        }
    }
};