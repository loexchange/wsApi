package marketwebsocketclient

import (
	"fmt"
	"loex_golang/logging/applogger"
	"loex_golang/pkg/client/websocketclientbase"
)

// Responsible to handle last 24h candlestick data from WebSocket
type Last24hCandlestickWebSocketClient struct {
	websocketclientbase.WebSocketClientBase
}

// Initializer
func (p *Last24hCandlestickWebSocketClient) Init(host string) *Last24hCandlestickWebSocketClient {
	p.WebSocketClientBase.Init(host)
	return p
}

// Set callback handler
func (p *Last24hCandlestickWebSocketClient) SetHandler(
	connectedHandler websocketclientbase.ConnectedHandler,
	responseHandler websocketclientbase.ResponseHandler) {
	p.WebSocketClientBase.SetHandler(connectedHandler, p.handleMessage, responseHandler)
}

// Request full candlestick data
func (p *Last24hCandlestickWebSocketClient) Request(symbol string, clientId string) {

}

// Subscribe latest 24h market stats
func (p *Last24hCandlestickWebSocketClient) Subscribe(symbol string, clientId string) {
	var topic string = ""
	if symbol == "" {
		topic = "market_ticker"
	} else {
		topic = fmt.Sprintf("market_%s_ticker", symbol)
	}
	sub := fmt.Sprintf("{\"action\": \"%s\",\"ch\": \"%s\",\"id\": \"%s\" }", "sub", topic, clientId)

	p.Send(sub)

	applogger.Info("WebSocket subscribed, topic=%s, clientId=%s", topic, clientId)
}

// Unsubscribe latest 24 market stats
func (p *Last24hCandlestickWebSocketClient) UnSubscribe(symbol string, clientId string) {
	var topic string = ""
	if symbol == "" {
		topic = "market_ticker"
	} else {
		topic = fmt.Sprintf("market_%s_ticker", symbol)
	}
	unsub := fmt.Sprintf("{\"action\": \"%s\",\"ch\": \"%s\",\"id\": \"%s\" }", "unsub", topic, clientId)

	p.Send(unsub)

	applogger.Info("WebSocket unsubscribed, topic=%s, clientId=%s", topic, clientId)
}

func (p *Last24hCandlestickWebSocketClient) handleMessage(msg string) (interface{}, error) {
	return msg, nil
}
