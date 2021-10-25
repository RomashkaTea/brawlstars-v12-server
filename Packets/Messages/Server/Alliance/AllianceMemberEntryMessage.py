from Database.DatabaseManager import DataBase
from Utils.Writer import Writer
import json

class AllianceMemberEntryMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24308
        self.player = player

    def encode(self):
        self.writeInt(0) # Club HighID
        self.writeInt(self.player.ClubID) # Club LowID
        
        self.writeInt(self.player.HighID)
        self.writeInt(self.player.LowID)
        self.writeString(self.player.name) # Player name
        self.writeVint(0)
        self.writeVint(28)
        self.writeVint(self.player.profileIcon) # Profile icon
        self.writeHexa('''7F''')