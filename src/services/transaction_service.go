package services

import (
	"chronochain/src/config"
	"chronochain/src/models"
	"crypto/sha256"
	"encoding/hex"
	"math"
	"time"
)

func CreateTransactionFromGross(from, to string, grossAmount int64) models.Transaction {
	feeFloat := float64(grossAmount) * config.TxFeePercent
	fee := int64(math.Round(feeFloat))
	if fee < 0 {
		fee = 0
	}

	net := grossAmount - fee
	if net < 0 {
		net = 0
	}

	raw := from + to + time.Now().UTC().Format(time.RFC3339Nano)
	sum := sha256.Sum256([]byte(raw))
	txid := hex.EncodeToString(sum[:])

	return models.Transaction{
		TxID:      txid,
		From:      from,
		To:        to,
		Amount:    net,
		Fee:       fee,
		Timestamp: time.Now().UTC(),
		Status:    "pending",
	}
}

func ConfirmTransaction(tx *models.Transaction) {
	tx.Status = "confirmed"
}
