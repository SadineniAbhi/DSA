func longestCommonPrefix(strs []string) string {
	prefix_rune := []byte(strs[0])
	for i:= 1; i < len(strs); i++ {
        word := strs[i]
        new_prefix_rune := []byte{}
		for j:=0; j<len(prefix_rune); j++{
			if j > len(word) -1 || word[j] != prefix_rune[j]{
                break
            }
            new_prefix_rune = append(new_prefix_rune, word[j])
		}
        prefix_rune = new_prefix_rune
	}    
    return string(prefix_rune)
}
