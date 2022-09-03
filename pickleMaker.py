import pickle

title = 'signInDetails.pkl'

logIn = {"api_key":"", "api_secret_key":"",
"access_token":"", "access_secret":""}

with open(title,"wb") as pickledF:
    pickle.dump(logIn,pickledF)