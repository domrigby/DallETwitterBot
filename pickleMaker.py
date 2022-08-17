import pickle

list = ["Test"]

filename = "previous_mentions.pkl"

with open(filename,'wb') as file:
    pickle.dump(list, file)
file.close() 