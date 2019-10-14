import pickle
import Orange
import sys

def predict(val):
    # print(val)
    age ,sex,everSmoker,everDrinker,sputum,coughWeeks,fever,nightSweats,weightLoss,chestPain,hardBreath,height,weight = list(val.split(','))
    with open("model_orange_neural_network.pkcls", "rb") as f:
        model = pickle.load(f)
        test = [age, sex, height, weight, everSmoker,	everDrinker, sputum,	coughWeeks,	fever,	nightSweats,weightLoss,	chestPain,	hardBreath]
        prob = model(test, model.Probs)
        print(prob[1])

predict(sys.argv[1])
# 50.39178082,	2,	168,	62,	0,	1,	0,	2,	0,	0,	1,	1,	1
