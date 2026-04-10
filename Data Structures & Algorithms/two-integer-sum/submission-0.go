func twoSum(nums []int, target int) []int {
    m := map[int]int{}
	for i , num := range nums {
		val, ok := m[num]
		if ok{
			return []int{val, i}
		}
		m[target-num] = i
	}
	return []int{}
}
