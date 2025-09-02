package models

import "time"

type Block struct {
	Height       int           `json:"height"`
	Timestamp    time.Time     `json:"timestamp"`
	PreviousHash string        `json:"previous_hash"`
	Hash         string        `json:"hash"`
	Transactions []Transaction `json:"transactions"`
}
