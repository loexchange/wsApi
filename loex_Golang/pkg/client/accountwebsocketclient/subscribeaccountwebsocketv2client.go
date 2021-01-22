package accountwebsocketclient

import (
	"fmt"
	"loex_golang/logging/applogger"
	"loex_golang/pkg/client/websocketclientbase"
)

// Responsible to handle account asset request from WebSocket
// This need authentication version 2
type SubscribeAccountWebSocketV2Client struct {
	websocketclientbase.WebSocketV2ClientBase
}

// Initializer
func (p *SubscribeAccountWebSocketV2Client) Init(accessKey string, secretKey string, host string) *SubscribeAccountWebSocketV2Client {
	p.WebSocketV2ClientBase.Init(accessKey, secretKey, host)
	return p
}

// Set callback handler
func (p *SubscribeAccountWebSocketV2Client) SetHandler(
	authHandler websocketclientbase.AuthenticationV2ResponseHandler,
	responseHandler websocketclientbase.ResponseHandler) {
	p.WebSocketV2ClientBase.SetHandler(authHandler, p.handleMessage, responseHandler)
}

// Subscribe all balance updates of the current account
// 0: Only update when account balance changed
// 1: Update when either account balance changed or available balance changed
func (p *SubscribeAccountWebSocketV2Client) Subscribe(clientId string) {
	channel := fmt.Sprintf("accounts_update")
	sub := fmt.Sprintf("{\"action\":\"sub\", \"ch\":\"%s\", \"cid\": \"%s\"}", channel, clientId)

	p.Send(sub)

	applogger.Info("WebSocket subscribed, channel=%s, clientId=%s", channel, clientId)
}

// Unsubscribe balance updates
func (p *SubscribeAccountWebSocketV2Client) UnSubscribe(clientId string) {
	channel := fmt.Sprintf("accounts_update")
	unsub := fmt.Sprintf("{\"action\":\"unsub\", \"ch\":\"%s\", \"cid\": \"%s\"}", channel, clientId)

	p.Send(unsub)

	applogger.Info("WebSocket unsubscribed, channel=%s, clientId=%s", channel, clientId)
}

func (p *SubscribeAccountWebSocketV2Client) handleMessage(msg string) (interface{}, error) {
	return msg, nil
}
