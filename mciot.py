import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "mcrcon"))
sys.path.append(os.path.join(os.path.dirname(__file__), "mcstatus"))

from mcrcon import MCRcon
from minecraft_query import MinecraftQuery


class ServerConnection(object):

    def __init__(self, host, password, query_port=25565, rcon_port=25575):
        self.query_port = query_port
        self.rcon_port = rcon_port
        self.host = host
        self.password = password

    def run_command(self, command):
        rcon = MCRcon(self.host, self.rcon_port, self.password)
        rcon.send(command)
        rcon.close()

    def query(self):
        query = MinecraftQuery(self.host, self.query_port)
        full_info = query.get_rules()
        query.socket.close()
        return full_info


