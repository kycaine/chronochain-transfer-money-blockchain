package services

import (
	"chronochain/src/config"
	"chronochain/src/models"
	"time"
)

func UpdateHeartbeat(node *models.Node) {
	node.LastHeartbeat = time.Now().UTC()
	node.Status = "active"
}

func CalculateUptimeDays(node *models.Node, start time.Time) int64 {
	now := time.Now().UTC()
	duration := now.Sub(start)
	return int64(duration.Hours() / 24)
}

func IsNodeEligible(node models.Node) bool {
	if node.Status != "active" {
		return false
	}
	if node.StakeLocked < config.MinStakeTokens {
		return false
	}
	if node.UptimeDays < 30 {
		return false
	}
	return true
}

func MarkInactive(node *models.Node) {
	node.Status = "inactive"
}
