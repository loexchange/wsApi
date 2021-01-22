package orderwebsocketclientexample

import (
	"fmt"
	"loex_golang/config"
	"loex_golang/logging/applogger"
	"loex_golang/pkg/client/orderwebsocketclient"
	"loex_golang/pkg/model/auth"
)

func RunAllExamples() {
	subOrderUpdate()
}

func subOrderUpdate() {
	// Initialize a new instance
	client := new(orderwebsocketclient.SubscribeOrderWebSocketV2Client).Init(config.AccessKey, config.SecretKey, config.Host)

	// Set the callback handlers
	client.SetHandler(
		// Connected handler
		func(resp *auth.WebSocketV2AuthenticationResponse) {
			if resp.IsSuccess() {
				// Subscribe if authentication passed
				client.Subscribe("btcusdt", "")
			} else {
				applogger.Error("Authentication error, code: %d, message:%s", resp.Code, resp.Message)
			}
		},
		// Response handler
		func(resp interface{}) {
			applogger.Info("WebSocket Resp : %s", resp)
		})

	// Connect to the server and wait for the handler to handle the response
	client.Connect(true)

	fmt.Println("Press ENTER to unsubscribe and stop...")
	fmt.Scanln()

	client.UnSubscribe("1", "1250")

	client.Close()
	applogger.Info("Client closed")
}
