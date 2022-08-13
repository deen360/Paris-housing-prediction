import pickle

from flask import Flask, request, jsonify

with open('model-lin.b', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)



def prepare_features(house):
    features = {}
    features['squareMeters'] = house['squareMeters']
    return features


def predict(features):
    X = dv.transform(features)
    preds = model.predict(X)
    return f'{round(preds[0])} Є'


app = Flask('house-price-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)

    result = {
        'House price': pred
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)