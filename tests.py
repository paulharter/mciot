from mciot import ServerConnection

import unittest

class ServerTests(unittest.TestCase):

    def setUp(self):
        self.server = ServerConnection("localhost", "password")

    def tearDown(self):
        pass

    def test_players(self):
        players = self.server.query()["players"]
        
    def test_rcon(self):
        self.server.run_command("say hello")