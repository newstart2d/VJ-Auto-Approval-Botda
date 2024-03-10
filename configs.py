# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28726816"))
    API_HASH = getenv("API_HASH", "45edf74203ecf6ff14b394a9e47dca34")
    BOT_TOKEN = getenv("BOT_TOKEN", "7168600940:AAEmzXh8luJnN1E7-Hfkye0DmBNd7p8rmT8")
    FSUB = getenv("FSUB", "born4movies7")
    CHID = int(getenv("CHID", "-1001654163482"))
    SUDO = list(map(int, getenv("SUDO", "5521380948").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://m0921594:Rohit44@cluster0.qbze22i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
