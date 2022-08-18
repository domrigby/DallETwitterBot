import pickle

title = 'Kanye_West_Lyrics.txt'

with open(title,"rb") as f:
    lines = f.readlines()
    with open("Kanye_West_Lyrics.pkl","wb") as pickledF:
        pickle.dump(lines,pickledF)