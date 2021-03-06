from Database.DatabaseManager import DataBase
from Packets.Commands.Server.LogicUnlockSkinServerCommand import LogicUnlockSkinServerCommand
from Utils.Reader import BSMessageReader
from Files.CsvLogic.Cards import Cards

class LogicUnlockSkinCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.skin_id = self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.brawler_id = self.read_Vint()


    def process(self, crypter):
        LogicUnlockSkinServerCommand(self.client, self.player).send(crypter)
        #print("SkinID", self.player.skin_id)
        #print(self.player.brawler_id)
        
