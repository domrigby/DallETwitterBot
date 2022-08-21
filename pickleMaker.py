import pickle

title = 'signInDetails.pkl'

logIn = {"api_key":"2w0mcXMnplO2z6XgbKK4hN6Ar", "api_secret_key":"EmW6vu3jHMCH1uzvfGbF9ndeAbJY3sZiDMGID1Mg2ri1rjRFMU",
"access_token":"1560205890002747395-tHjCIyDmJksrmG4hi3uRJecmMfFsS9", "access_secret":"tsB3Ot9ZdcOhlrBfPg2FA7ORINz13FBvg76WYryB6h7U3"}

with open(title,"wb") as pickledF:
    pickle.dump(logIn,pickledF)