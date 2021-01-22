package account

import "loex_golang/pkg/model/base"

type SubscribeAccountV2Response struct {
	base.WebSocketV2ResponseBase
	Data *struct {
		Coin        string `json:"coin"`
		Account     int    `json:"account"`
		Balance     string `json:"balance"`
		ChangeType  string `json:"changeType"`
		AccountType string `json:"accountType"`
		ChangeTime  int64  `json:"changeTime"`
	}
}
