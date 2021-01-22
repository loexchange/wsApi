package main

import (
	"loex_golang/cmd/accountwebsocketclientexample"
	"loex_golang/cmd/marketwebsocketclientexample"
	"loex_golang/cmd/orderwebsocketclientexample"
)

func main() {
	marketwebsocketclientexample.RunAllExamples()
	accountwebsocketclientexample.RunAllExamples()
	orderwebsocketclientexample.RunAllExamples()
}
