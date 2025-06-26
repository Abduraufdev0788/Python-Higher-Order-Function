emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

def domen(gmails:str):
    if gmails.endswith("@gmail.com") :
        return gmails

gmail = list(filter(domen, emails))

print(gmail)