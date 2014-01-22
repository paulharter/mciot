mciot
=====
A simple wrapper around mcrcon and mcquery to support the Minecraft of Things project.

mciot uses submodules, to download them after cloning this repo you will need to run:

git submodule init

git submodule update

Usage
------

server = mciot.ServerConnection("localhost", "password")

server.run_command("kill paulharter")

players = server.query()["players"]


Server Properties
-----------------

To use this code with a Minecraft server the server has to be configured to accept query requests and remote connections. This is done by setting the following values in the server.properties file:

* enable-query=true
* enable-rcon=true
* rcon.password=*******

And optionally ports for query and rcon if you dont want to use the defaults

* query.port=25565
* rcon.port=25575



