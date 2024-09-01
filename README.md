This project is built to be used alongside a Minecraft Server Docker container. It is designed to be used with the [itzg/minecraft-server](https://hub.docker.com/r/itzg/minecraft-server) image, but can be used with any Minecraft server image that uses the same volume structure.

## Usage
**TEMPLATE_PATH** - The path to the template server that will be copied to create new servers.<br />
**SERVERS_PATH** - The path to the folder that will contain all the servers.<br />
**CURRENT_PORT** - The most recent port that was used for a server.<br />
**MAX_PORT** - The maximum port opened on your router for the servers.

Sample `config.json`:
```json
{
    "template_path": "D:/Minecraft/template",
    "servers_path": "D:/Minecraft/",
    "current_port": 25568,
    "max_port": 25580
}
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.