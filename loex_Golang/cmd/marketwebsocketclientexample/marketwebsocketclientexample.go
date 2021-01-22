package marketwebsocketclientexample

import (
	"fmt"
	"loex_golang/config"
	"loex_golang/logging/applogger"
	"loex_golang/pkg/client/marketwebsocketclient"
	"loex_golang/pkg/model/market"
)

func RunAllExamples() {
	reqAndSubscribeCandlestick()
	reqAndSubscribeDepth()
	reqAndSubscribeTrade()
	reqAndSubscribeLast24hCandlestick()
}

func reqAndSubscribeCandlestick() {

	client := new(marketwebsocketclient.CandlestickWebSocketClient).Init(config.Host)

	client.SetHandler(
		func() {
			client.Request("btcusdt", "1day", 0, 0, "j4ecd3s9rj.1610623898018.1.111")

			//client.Subscribe("btcusdt", "1day", "j4ecd3s9rj.1610623898018.1.111")
		},
		func(response interface{}) {
			applogger.Info("WebSocket Resp : %s", response)
		})

	client.Connect(true)

	fmt.Println("Press ENTER to unsubscribe and stop...")
	fmt.Scanln()

	client.UnSubscribe("btcusdt", "1day", "2118")

	client.Close()
	applogger.Info("Client closed")
}

func reqAndSubscribeDepth() {

	client := new(marketwebsocketclient.DepthWebSocketClient).Init(config.Host)

	client.SetHandler(
		func() {
			client.Subscribe("btcusdt", market.STEP1, "")
		},
		func(resp interface{}) {
			applogger.Info("[Resp]: %s", resp)
		})

	client.Connect(true)

	fmt.Println("Press ENTER to unsubscribe and stop...")
	fmt.Scanln()

	client.UnSubscribe("btcusdt", market.STEP4, "")

	client.Close()
	applogger.Info("Client closed")
}

func reqAndSubscribeTrade() {

	client := new(marketwebsocketclient.TradeWebSocketClient).Init(config.Host)

	client.SetHandler(
		func() {
			client.Request("btcusdt", "")

			client.Subscribe("btcusdt", "")
		},
		func(resp interface{}) {
			applogger.Info("[Resp]: %s", resp)
		})

	client.Connect(true)

	fmt.Println("Press ENTER to unsubscribe and stop...")
	fmt.Scanln()

	client.UnSubscribe("btcusdt", "")

	client.Close()
	applogger.Info("Client closed")
}

func reqAndSubscribeLast24hCandlestick() {
	// Initialize a new instance
	client := new(marketwebsocketclient.Last24hCandlestickWebSocketClient).Init(config.Host)

	// Set the callback handlers
	client.SetHandler(
		// Connected handler
		func() {
			client.Request("", "")

			client.Subscribe("", "")
		},
		// Response handler
		func(resp interface{}) {
			applogger.Info("[Resp]: %s", resp)
		})

	// Connect to the server and wait for the handler to handle the response
	client.Connect(true)

	fmt.Println("Press ENTER to unsubscribe and stop...")
	fmt.Scanln()

	client.UnSubscribe("", "")

	client.Close()
	applogger.Info("Client closed")
}
