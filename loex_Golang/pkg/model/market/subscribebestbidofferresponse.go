package market

import (
	"loex_golang/pkg/model/base"
	"github.com/shopspring/decimal"
)

type SubscribeBestBidOfferResponse struct {
	base.WebSocketResponseBase
	Tick *struct {
		QuoteTime int64           `json:"quoteTime"`
		Symbol    string          `json:"symbol"`
		Bid       decimal.Decimal `json:"bid"`
		BidSize   decimal.Decimal `json:"bidSize"`
		Ask       decimal.Decimal `json:"ask"`
		AskSize   decimal.Decimal `json:"askSize"`
	}
}
