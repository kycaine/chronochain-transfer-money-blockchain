package models

import "time"

type Transaction struct {
	TxID      string    `json:"txid"`
	From      string    `json:"from"`
	To        string    `json:"to"`
	Amount    int64     `json:"amount"`
	Fee       float64   `json:"fee"`
	Timestamp time.Time `json:"timestamp"`
	Status    string    `json:"status"`
}
