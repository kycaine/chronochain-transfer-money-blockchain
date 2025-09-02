package services

import (
	"chronochain/src/models"
	"crypto/sha256"
	"encoding/hex"
	"time"
)

type Blockchain struct {
	Blocks []models.Block
}

func NewBlockchain() *Blockchain {
	genesis := models.Block{
		Height:       1,
		Timestamp:    time.Now().UTC(),
		PreviousHash: "0x000000",
		Hash:         "",
		Transactions: []models.Transaction{},
	}
	genesis.Hash = calculateBlockHash(genesis)

	return &Blockchain{
		Blocks: []models.Block{genesis},
	}
}

func (bc *Blockchain) AddBlock(transactions []models.Transaction) models.Block {
	lastBlock := bc.Blocks[len(bc.Blocks)-1]

	newBlock := models.Block{
		Height:       lastBlock.Height + 1,
		Timestamp:    time.Now().UTC(),
		PreviousHash: lastBlock.Hash,
		Transactions: transactions,
	}
	newBlock.Hash = calculateBlockHash(newBlock)

	bc.Blocks = append(bc.Blocks, newBlock)
	return newBlock
}

func (bc *Blockchain) GetLatestBlock() models.Block {
	return bc.Blocks[len(bc.Blocks)-1]
}

func calculateBlockHash(block models.Block) string {
	raw := string(rune(block.Height)) +
		block.Timestamp.String() +
		block.PreviousHash

	sum := sha256.Sum256([]byte(raw))
	return hex.EncodeToString(sum[:])
}
