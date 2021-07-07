package main

// go run lessons\5-arrays\OddOccurrencesInArray.go

import "fmt"



func Solution(A []int) (Result int) {
	Result = 0
	for _, num := range A {
		Result ^= num
	}
	return
}

func main() {
	a := []int{9, 3, 9, 3, 9, 7, 9}
	res := Solution(a)

	fmt.Printf("The odd digit out in %v is %d.\n", a, res)
}