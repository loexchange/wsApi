package orderwebsocketclient

import (
	"fmt"
	"loex_golang/logging/applogger"
	"loex_golang/pkg/client/websocketclientbase"
)

// Responsible to handle order subscription from WebSocket
// This need authentication version 2
type SubscribeOrderWebSocketV2Client struct {
	websocketclientbase.WebSocketV2ClientBase
}

// Initializer
func (p *SubscribeOrderWebSocketV2Client) Init(accessKey string, secretKey string, host string) *SubscribeOrderWebSocketV2Client {
	p.WebSocketV2ClientBase.Init(accessKey, secretKey, host)
	return p
}

// Set callback handler
func (p *SubscribeOrderWebSocketV2Client) SetHandler(
	authHandler websocketclientbase.AuthenticationV2ResponseHandler,
	responseHandler websocketclientbase.ResponseHandler) {
	p.WebSocketV2ClientBase.SetHandler(authHandler, p.handleMessage, responseHandler)
}

// Subscribe all order updates of the current account
func (p *SubscribeOrderWebSocketV2Client) Subscribe(symbol string, clientId string) {
	channel := fmt.Sprintf("orders_%s", symbol)
	sub := fmt.Sprintf("{\"action\":\"sub\", \"ch\":\"%s\"}", channel)

	p.Send(sub)

	applogger.Info("WebSocket subscribed, channel=%s, clientId=%s", channel, clientId)
}

// Unsubscribe order updates
func (p *SubscribeOrderWebSocketV2Client) UnSubscribe(symbol string, clientId string) {
	channel := fmt.Sprintf("orders_%s", symbol)
	unsub := fmt.Sprintf("{\"action\":\"unsub\", \"ch\":\"%s\"}", channel)

	p.Send(unsub)

	applogger.Info("WebSocket unsubscribed, channel=%s, clientId=%s", channel, clientId)
}

func (p *SubscribeOrderWebSocketV2Client) handleMessage(msg string) (interface{}, error) {
	return msg, nil
}
