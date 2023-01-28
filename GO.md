# Go cheatsheet

## Safe access map

```go
package main

import (
	"fmt"
	"strconv"
	"sync"
)

type MyMap struct {
	mx sync.RWMutex
	m  map[string]int
}

func (myMap *MyMap) Get(key string) (int, bool) {
	myMap.mx.RLock()
	defer myMap.mx.RUnlock()
	val, ok := myMap.m[key]
	return val, ok
}

func (myMap *MyMap) Set(key string, value int) {
	myMap.mx.Lock()
	defer myMap.mx.Unlock()
	myMap.m[key] = value
}

func NewMap() *MyMap {
	return &MyMap{m: make(map[string]int)}
}

func main() {
	myMap := NewMap()
	wg := sync.WaitGroup{}

	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func(num int) {
			defer wg.Done()
			myMap.Set(strconv.Itoa(num), num)
			n, _ := myMap.Get(strconv.Itoa(num))
			fmt.Println(n)
		}(i)
	}

	wg.Wait()
	fmt.Println(myMap.m)
}

```

## Channel and WaitGroup example

```go
package main

import (
	"io"
	"log"
	"net/http"
	"sync"
)

const TEST_URL = "https://gerbill.github.io/"

func main() {
	c := make(chan struct{}, 100)
	wg := sync.WaitGroup{}

	for i := 0; i < 100; i++ {
		c <- struct{}{}
		wg.Add(1)
		go func() {
			defer wg.Done()
			defer func() { <-c }()
			sendRequest(TEST_URL)
		}()
	}
	wg.Wait()
}

func sendRequest(url string) int {
	resp, err := http.Get(url)
	if err != nil {
		log.Fatalln(err)
	}
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}

	bodyLength := len(string(body))
	return bodyLength
}
```
