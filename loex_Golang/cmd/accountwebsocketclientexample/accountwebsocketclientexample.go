package accountwebsocketclientexample

import (
	"fmt"
	"loex_golang/config"
	"loex_golang/logging/applogger"
	"loex_golang/pkg/client/accountwebsocketclient"
	"loex_golang/pkg/model/auth"
)

func RunAllExamples() {
	subAccountUpdate()
}

func subAccountUpdate() {
	// Initialize a new instance
	client := new(accountwebsocketclient.SubscribeAccountWebSocketV2Client).Init(config.AccessKey, config.SecretKey, config.Host)

	// Set the callback handlers
	client.SetHandler(
		// Authentication response handler
		func(resp *auth.WebSocketV2AuthenticationResponse) {
			if resp.IsSuccess() {
				client.Subscribe("")
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

	// Unsubscribe the topic
	client.UnSubscribe("")

	// Close the connection
	client.Close()
	applogger.Info("Client closed")
}
