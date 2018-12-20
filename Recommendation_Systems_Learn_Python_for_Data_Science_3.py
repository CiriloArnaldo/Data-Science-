import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM
# SciPy es una biblioteca open source de herramientas y algoritmos matemáticos para Python que nació a partir de la colección original de Travis Oliphant que consistía de módulos de extensión para Python, lanzada en 1999 bajo el nombre de Multipack
# LightFM is a Python implementation of a number of popular recommendation algorithms for both implicit and explicit feedback, including efficient implementation of BPR and WARP ranking losses. It's easy to use, fast (via multithreaded model estimation), and produces high quality results.


# Fetch data and format it
data = fetch_movielens(min_rating = 3.0)

# Print training and testing data

print('------------DATA-----------')
print(data)

print('------------data["train"] & data["test"]-----------')
print(data['train'])
print('-----------')
print(data['test'])

print('-------type(data["train"]) & type(data["test"])-------')
print(type(data['train']))
print('-----------')
print(type(data['test']))

print('-------repr(data["train"]) & resp(data["test"])-------')
print(repr(data['train']))
print('-----------')
print(repr(data['test']))

# Create model
model = LightFM(loss="warp")
# Training model
model.fit(data['train'], epochs=30, num_threads=2)

# Generate recommendations for each user we input
def sample_recommendation(model, data, user_ids):
    #number of users and movies in training data
    n_users, n_items = data['train'].shape

    #generate recommendations for each user we input
    for user_id in user_ids:
        #movies they already like
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        #movies our model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))
        #rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        #print out the results
        print("User %s" % user_id)
        print("     Known positives:")

        for x in known_positives[:3]:
            print("        %s" % x)

        print("     Recommended:")

        for x in top_items[:3]:
            print("        %s" % x)

sample_recommendation(model, data, [3, 25, 450])
