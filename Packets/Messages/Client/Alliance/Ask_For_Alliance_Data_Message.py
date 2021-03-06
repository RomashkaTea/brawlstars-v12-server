from Packets.Messages.Server.Alliance.Alliance_Data_Message import AllianceDataMessage
from random import choice
from string import ascii_uppercase
import json
from Utils.Reader import BSMessageReader


class AskForAllianceDataMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.clubHighID = self.read_int()
        self.clubLowID = self.read_int()

    def process(self, crypter):
        AllianceDataMessage(self.client, self.player, self.clubHighID, self.clubLowID).send(crypter)