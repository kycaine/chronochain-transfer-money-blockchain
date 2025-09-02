package models

import "time"

type Node struct {
	NodeID        string    `json:"node_id"`
	UptimeDays    int       `json:"uptime_days"`
	StakeLocked   int64     `json:"stake_locked"`
	LastHeartbeat time.Time `json:"last_heartbeat"`
	Status        string    `json:"status"` // active or inactive
}
