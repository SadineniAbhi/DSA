type MyHashSet struct {
	m map[int]bool
}

func Constructor() MyHashSet {
    return MyHashSet{
		m: map[int]bool{},
	}
}

func (this *MyHashSet) Add(key int) {
    this.m[key] = true
}

func (this *MyHashSet) Remove(key int) {
	this.m[key] = false
}

func (this *MyHashSet) Contains(key int) bool {
	v, ok := this.m[key]
	if ok && v == true{
		return true
	}	
	return false
    
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
 