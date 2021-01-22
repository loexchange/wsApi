package marketwebsocketclient

import (
	"fmt"
	"loex_golang/logging/applogger"
	"loex_golang/pkg/client/websocketclientbase"
)

// Responsible to handle Trade data from WebSocket
type TradeWebSocketClient struct {
	websocketclientbase.WebSocketClientBase
}

// Initializer
func (p *TradeWebSocketClient) Init(host string) *TradeWebSocketClient {
	p.WebSocketClientBase.Init(host)
	return p
}

// Set callback handler
func (p *TradeWebSocketClient) SetHandler(
	connectedHandler websocketclientbase.ConnectedHandler,
	responseHandler websocketclientbase.ResponseHandler) {
	p.WebSocketClientBase.SetHandler(connectedHandler, p.handleMessage, responseHandler)
}

// Request latest 300 trade data
func (p *TradeWebSocketClient) Request(symbol string, clientId string) {
	topic := fmt.Sprintf("market_%s_trade_ticker", symbol)
	req := fmt.Sprintf("{\"action\": \"%s\", \"ch\": \"%s\",\"id\": \"%s\" }", "req", topic, clientId)

	p.Send(req)

	applogger.Info("WebSocket requested, topic=%s, clientId=%s", topic, clientId)
}

// Subscribe latest completed trade in tick by tick mode
func (p *TradeWebSocketClient) Subscribe(symbol string, clientId string) {
	topic := fmt.Sprintf("market_%s_trade_ticker", symbol)
	sub := fmt.Sprintf("{\"action\": \"%s\",  \"ch\": \"%s\",\"id\": \"%s\" }", "sub", topic, clientId)

	p.Send(sub)

	applogger.Info("WebSocket subscribed, topic=%s, clientId=%s", topic, clientId)
}

// Unsubscribe trade
func (p *TradeWebSocketClient) UnSubscribe(symbol string, clientId string) {
	topic := fmt.Sprintf("market_%s_trade_ticker", symbol)
	unsub := fmt.Sprintf("{\"action\": \"%s\",  \"ch\": \"%s\",\"id\": \"%s\" }", "unsub", topic, clientId)

	p.Send(unsub)

	applogger.Info("WebSocket unsubscribed, topic=%s, clientId=%s", topic, clientId)
}

func (p *TradeWebSocketClient) handleMessage(msg string) (interface{}, error) {
	return msg, nil
}
