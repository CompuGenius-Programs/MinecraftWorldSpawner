This project is built to be used alongside a Minecraft Server Docker container. It is designed to be used with the [itzg/minecraft-server](https://hub.docker.com/r/itzg/minecraft-server) image, but can be used with any Minecraft server image that uses the same volume structure.

## Usage
Be sure to edit `config.json` to define the directory of the template Minecraft server files and the directory of the Minecraft server files. The template directory should be the directory of the Minecraft server files that you want to use as the template. The server directory should be the directory of the Minecraft server files that the server will use.
Also be sure to set the last used port and the max port opened on your router.

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