from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

class TeamGameroomDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player
        self.playerCount = 1

    def encode(self):
        DataBase.loadGameroom(self)
        if self.player.room_id != 0:
            self.writeVint(1) #mode
            self.writeByte(0)
            self.writeVint(1)
            self.writeInt(0)
            self.writeInt(self.player.room_id)
            self.writeVint(1557129593)
            self.writeByte(0)
            self.writeByte(0)
            self.writeVint(0)

            self.writeScId(15, self.mapID)               # MapID
            print("MAP", self.mapID)

            self.writeVint(self.playerCount)

            for player,values in self.playersdata.items():
                # Player
                self.writeVint(self.playersdata[player]["IsHost"])       # Gameroom owner boolean
                self.writeInt(0) # High ID
                self.writeInt(self.player.low_id)         # LowID
                self.writeString(self.playersdata[player]["name"])                  # Player name
                self.writeVint(3)

                self.writeScId(16, self.playersdata[player]["brawlerID"])             # BrawlerID
                self.writeVint(0)
                self.writeVint(99999)                                    # Unknown
                self.writeVint(99999)                                    # Unknown
                self.writeVint(10)                                   # Power level

                self.writeVint(3)                                   # Player State | 11: Events, 10: Brawlers, 9: Writing..., 8: Training, 7: Spectactor, 6: Offline, 5: End Combat Screen, 4: Searching, 3: Not Ready, 2: AFK, 1: In Combat, 0: OffLine
                self.writeVint(self.playersdata[player]["Ready"])    # Is ready
                self.writeVint(self.playersdata[player]["Team"])     # Team | 0: Blue, 1: Red
                self.writeVint(0)

                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(0)

            self.writeVint(0)
            self.writeVint(0)

            self.writeBoolean(False)
        else:
            print(self.player.room_id)
