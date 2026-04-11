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
    res := map[[26]int][]string{}
    for _, str := range strs {
        counts := [26]int{}
        for _, char := range str {
            counts[char-'a'] ++
        }
        res[counts] = append(res[counts], str)
    }

    ans := [][]string{}
    for _, val := range res {
        ans = append(ans, val)
    }
    return ans
}
