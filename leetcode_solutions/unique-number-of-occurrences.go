func uniqueOccurrences(arr []int) bool {

    count := make(map[int]int)
    st := make(map[int]bool)
    N := len(arr)

    for i := 0; i < N; i++{
        count[arr[i]] += 1
    }

    valid := true
    for _, val := range count{
        if st[val] == true{
            valid = false
        }
        st[val] = true
    }
    
    return valid
}