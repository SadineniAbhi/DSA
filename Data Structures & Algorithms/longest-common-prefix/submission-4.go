func longestCommonPrefix(strs []string) string {
	prefix_rune := []rune(strs[0])
	for i:= 1; i < len(strs); i++ {
        word := strs[i]
        new_prefix_rune := []rune{}
		for j:=0; j<len(prefix_rune); j++{
			if j > len(word) -1 || rune(word[j]) != prefix_rune[j]{
                break
            }
            new_prefix_rune = append(new_prefix_rune, rune(word[j]))
		}
        prefix_rune = new_prefix_rune
	}    
    return string(prefix_rune)
}
