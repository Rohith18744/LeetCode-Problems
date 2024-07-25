class Solution {
    public void moveZeroes(int[] nums) {
        int size=nums.length;
        if(size==0||size==1){
            return;
        }
        int l=0,r=0;
        while(r<size){
            if(nums[r]!=0){
                int temp=nums[r];
                nums[r]=nums[l];
                nums[l]=temp;
                l++;
                r++;
            }
            else{
                r++;
            }
        }
    }
}