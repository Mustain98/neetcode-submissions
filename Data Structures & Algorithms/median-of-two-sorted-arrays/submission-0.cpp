class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        // Always binary search on the smaller array
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.size();
        int n = nums2.size();

        int l = 0;
        int r = m;

        while (l <= r) {

            // Number of elements taken from nums1
            int i = (l + r) / 2;

            // Number of elements taken from nums2
            int j = (m + n + 1) / 2 - i;

            int leftA = (i == 0) ? INT_MIN : nums1[i - 1];
            int rightA = (i == m) ? INT_MAX : nums1[i];

            int leftB = (j == 0) ? INT_MIN : nums2[j - 1];
            int rightB = (j == n) ? INT_MAX : nums2[j];

            // Correct partition
            if (leftA <= rightB && leftB <= rightA) {

                // Even number of elements
                if ((m + n) % 2 == 0) {
                    return (max(leftA, leftB) +
                            min(rightA, rightB)) / 2.0;
                }

                // Odd number of elements
                return max(leftA, leftB);
            }

            // We took too many elements from nums1
            else if (leftA > rightB) {
                r = i - 1;
            }

            // We took too few elements from nums1
            else {
                l = i + 1;
            }
        }

        return 0.0;
    }
};