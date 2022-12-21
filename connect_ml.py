import pickle
import numpy as np

def web_input(input_info):
    processed_data = []
    for k, v in input_info.items():
        if v == 'male':
            processed_data.append(0)
        elif v == 'female':
            processed_data.append(1)
        else:
            processed_data.append(v)
    processed_data = np.array(processed_data)
    return processed_data

def make_prediction(processed_data):
    with open('rf_reg.pkl', 'rb') as f:
        weights = pickle.load(f)
    return weights.predict(processed_data.reshape(1,-1))

if __name__ == '__main__':
    processed_data = np.array([0,76,3,3,4,5,19]).reshape(1,-1)
    print(make_prediction(processed_data))