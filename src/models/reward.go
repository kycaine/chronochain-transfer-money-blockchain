package models

type RewardPool struct {
	Balance float64 `json:"balance"`
	Fees    float64 `json:"fees"`
	Bonus   float64 `json:"bonus"`
}

type RewardDistribution struct {
	Period              string             `json:"period"`
	TotalReward         float64            `json:"total_reward"`
	ElderRewardTotal    float64            `json:"elder_reward_total"`
	PartyRewardTotal    float64            `json:"party_reward_total"`
	PerNodeDistribution map[string]float64 `json:"per_node"`
}
