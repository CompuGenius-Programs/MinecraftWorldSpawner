import json
import os
import shutil

import yaml


def get_server_name():
    return input("Enter the server name: ")


def duplicate_folder(src, dest):
    shutil.copytree(src, dest)


def edit_docker_compose(file_path, server_name, new_port):
    with open(file_path, 'r') as file:
        docker_compose = yaml.safe_load(file)

    docker_compose['name'] = server_name
    docker_compose['services']['mc']['ports'][0] = f"{new_port}:{new_port}"

    with open(file_path, 'w') as file:
        yaml.safe_dump(docker_compose, file)


def edit_server_properties(file_path, new_port, server_name):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.startswith("query.port"):
                file.write(f"query.port={new_port}\n")
            elif line.startswith("server-port"):
                file.write(f"server-port={new_port}\n")
            elif line.startswith("level-name"):
                file.write(f"level-name={server_name}\n")
            else:
                file.write(line)


def main():
    server_name = get_server_name()

    if not os.path.exists("config.json"):
        print("Config file not found. Creating a new one.")
        with open("config.json", 'w') as file:
            json.dump(
                {"template_path": "D:/Minecraft/template", "servers_path": "D:/Minecraft/", "current_port": 25564, "max_port": 25564},
                file)

    with open("config.json", 'r') as file:
        config = json.load(file)

    src_folder = config["template_path"]
    dest_folder = os.path.join(config["servers_path"], server_name)
    new_port = config["current_port"] + 1
    max_port = config["max_port"]

    duplicate_folder(src_folder, dest_folder)

    docker_compose_path = os.path.join(dest_folder, 'docker-compose.yml')
    server_properties_path = os.path.join(dest_folder, 'data', 'server.properties')

    if new_port > max_port:
        print("Remember to open more ports on the router")

    config["current_port"] = new_port
    with open("config.json", 'w') as file:
        json.dump(config, file)

    edit_docker_compose(docker_compose_path, server_name, new_port)
    edit_server_properties(server_properties_path, new_port, server_name)

    os.system(f"docker-compose -f {docker_compose_path} up -d")


if __name__ == "__main__":
    main()
