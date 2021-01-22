package marketwebsocketclient

import (
	"fmt"
	"loex_golang/logging/applogger"
	"loex_golang/pkg/client/websocketclientbase"
)

// Responsible to handle candlestick data from WebSocket
type CandlestickWebSocketClient struct {
	websocketclientbase.WebSocketClientBase
}

// Initializer
func (p *CandlestickWebSocketClient) Init(host string) *CandlestickWebSocketClient {
	p.WebSocketClientBase.Init(host)
	return p
}

// Set callback handler
func (p *CandlestickWebSocketClient) SetHandler(
	connectedHandler websocketclientbase.ConnectedHandler,
	responseHandler websocketclientbase.ResponseHandler) {
	p.WebSocketClientBase.SetHandler(connectedHandler, p.handleMessage, responseHandler)
}

// Request the full candlestick data according to specified criteria
func (p *CandlestickWebSocketClient) Request(symbol string, period string, from int64, to int64, clientId string) {
	topic := fmt.Sprintf("market_%s_kline_%s", symbol, period)
	if from == 0 && to == 0 {
		req := fmt.Sprintf("{\"action\": \"req\", \"ch\": \"%s\", \"params\": {}}", topic)
		p.Send(req)
	} else {
		req := fmt.Sprintf("{\"action\": \"req\", \"ch\": \"%s\", \"from\":%d, \"to\":%d}", topic, from, to)
		p.Send(req)
	}

	applogger.Info("WebSocket requested, topic=%s, clientId=%s", topic, clientId)
}

// Subscribe candlestick data
func (p *CandlestickWebSocketClient) Subscribe(symbol string, period string, clientId string) {
	topic := fmt.Sprintf("market_%s_kline_%s", symbol, period)
	sub := fmt.Sprintf("{\"action\": \"sub\", \"ch\": \"%s\"}", topic)

	p.Send(sub)

	applogger.Info("WebSocket subscribed, topic=%s, clientId=%s", topic, clientId)
}

// Unsubscribe candlestick data
func (p *CandlestickWebSocketClient) UnSubscribe(symbol string, period string, clientId string) {
	topic := fmt.Sprintf("market_%s_kline_%s", symbol, period)
	unsub := fmt.Sprintf("{\"action\": \"unsub\", \"ch\": \"%s\"}", topic)

	p.Send(unsub)

	applogger.Info("WebSocket unsubscribed, topic=%s, clientId=%s", topic, clientId)
}

func (p *CandlestickWebSocketClient) handleMessage(msg string) (interface{}, error) {
	return msg, nil
}
