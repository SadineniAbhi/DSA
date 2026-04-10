func checkAnagrams(str1 string, str2 string) bool{
    count_map := map[rune]int{}
    for _, char := range str1{
        count_map[char] ++
    }
    for _, char := range str2{
        count_map[char] --
    }
    for _, val := range count_map {
        if val != 0 {
            return false
        }
    }
    return true
}

func groupAnagrams(strs []string) [][]string {
    res := [][]string{}
    vis_ind := map[int]bool{} 
    for i, word := range strs {
        current := []string{}
        _, ok := vis_ind[i]
        if ok {
            continue
        } 
        vis_ind[i] = true
        current = append(current, word)
        for j := i+1; j < len(strs); j ++{
            check := checkAnagrams(word, strs[j])
            if check  {
                current = append(current, strs[j])
                vis_ind[j] = true
            }
        }
        res = append(res, current)
    }
    return res
}
