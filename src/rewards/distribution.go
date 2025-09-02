package rewards

import (
	"chronochain/src/config"
	"chronochain/src/models"
	"sort"
)

func DistributeRewards(pool *models.RewardPool, nodes []models.Node, period string) models.RewardDistribution {
	eligible := []models.Node{}
	for _, node := range nodes {
		if node.Status == "active" &&
			node.StakeLocked >= config.MinStakeTokens &&
			node.UptimeDays >= 30 {
			eligible = append(eligible, node)
		}
	}

	if len(eligible) == 0 {
		return models.RewardDistribution{
			Period:              period,
			TotalReward:         0,
			ElderRewardTotal:    0,
			PartyRewardTotal:    0,
			PerNodeDistribution: map[string]float64{},
		}
	}

	sort.Slice(eligible, func(i, j int) bool {
		return eligible[i].UptimeDays > eligible[j].UptimeDays
	})

	elderCount := int(float64(len(eligible)) * 0.1)
	if elderCount < 1 {
		elderCount = 1
	}
	elders := eligible[:elderCount]

	total := pool.Balance
	elderTotal := total * config.ElderRewardPercent
	partyTotal := total * config.PartyRewardPercent

	result := models.RewardDistribution{
		Period:              period,
		TotalReward:         total,
		ElderRewardTotal:    elderTotal,
		PartyRewardTotal:    partyTotal,
		PerNodeDistribution: map[string]float64{},
	}

	perElder := elderTotal / float64(len(elders))
	for _, n := range elders {
		result.PerNodeDistribution[n.NodeID] += perElder
	}

	perParty := partyTotal / float64(len(eligible))
	for _, n := range eligible {
		result.PerNodeDistribution[n.NodeID] += perParty
	}

	ResetPool(pool)

	return result
}
