from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.Battle.PlayAgainStatusMessage import PlayAgainStatusMessage

from Utils.Reader import BSMessageReader


class PlayAgainMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, crypter):
        PlayAgainStatusMessage(self.client, self.player).send(crypter)
