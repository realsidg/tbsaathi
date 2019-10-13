import pickle
import Orange

def predict(age, gender, height, weight, EverSmoke,	Everdrink, Sputum,	CoughWeeks,	Fever,	Nightsweats,Weightloss,	Chestpain,	Hardbreath):
    with open("model_orange_neural_network.pkcls", "rb") as f:
        model = pickle.load(f)
        test = [age, gender, height, weight, EverSmoke,	Everdrink, Sputum,	CoughWeeks,	Fever,	Nightsweats,Weightloss,	Chestpain,	Hardbreath]
        prob = model(test, model.Probs)
        print(prob[1])
