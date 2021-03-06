from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DatabaseManager import DataBase
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Cards import Cards

from Utils.Reader import BSMessageReader


class TeamChangeMemberSettingsMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.csv_id = self.read_Vint()
        if self.csv_id == 23:
            self.StarpowerID = self.read_Vint()
        else:
            self.csv_id = self.read_Vint()
            self.BrawlerSkinId = self.read_Vint()

    def process(self, crypter):
        if self.csv_id == 29:
            self.player.skin_id = Characters.get_brawler_by_skin_id(self, self.BrawlerSkinId)
            self.player.starpower = Cards.get_spg_by_brawler_id(self, self.player.brawler_id, 4)
        else:
            self.player.starpower = self.StarpowerID

        DataBase.replaceValue(self, 'starpower', self.player.starpower)

        DataBase.UpdateGameroomPlayerInfo(self, self.player.low_id)

        TeamGameroomDataMessage(self.client, self.player).send(crypter)