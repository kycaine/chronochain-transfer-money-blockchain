package rewards

import "chronochain/src/models"

func AddFee(rp *models.RewardPool, fee float64) {
	rp.Fees += fee
	rp.Balance += fee
}

func AddBonus(rp *models.RewardPool, bonus float64) {
	rp.Bonus += bonus
	rp.Balance += bonus
}

func ResetPool(rp *models.RewardPool) {
	rp.Balance = 0
	rp.Fees = 0
	rp.Bonus = 0
}
