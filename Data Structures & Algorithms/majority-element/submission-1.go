func majorityElement(nums []int) int {
    res := nums[0]
    count:= 1 
    for i := 1; i < len(nums) ; i ++ {
        if nums[i] != res{
            if count == 1{
                res = nums[i]
            }else{
                count--
            }
        }else{
            count++
        }
    }

    return res
}
