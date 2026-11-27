import json
import os
from pathlib import Path
import sys

"""
Global variables for building the build and docker compose file.
"""

CONFIG_FILE = Path("config.json")
BUILD_DIR = Path("build")
ENVS_DIR = BUILD_DIR / "envs"
SECRETS_DIR = BUILD_DIR / "secrets"

def load_config()->dict:
    if (not CONFIG_FILE.exists()):
        raise SystemExit(
            "Error : config.json file is missing\n"
            "Fix : cp infra/config.example.json config.json"
            )

    with open(CONFIG_FILE, "r", encoding="utf-8") as file_obj:
        return (json.load(file_obj))

def create_secret_files(secrets: dict)-> None:

    SECRETS_DIR.mkdir(parents=True, exist_ok=True)

    for name, value in secrets.items():
        path = SECRETS_DIR / f"{name}.txt"
        path.write_text(str(value), encoding="utf-8")
        os.chmod(path, 0o600)

def create_env_file(service_name: str, env_vars: dict)-> None:

    ENVS_DIR.mkdir(parents=True, exist_ok=True)

    path = ENVS_DIR / f"{service_name}.env"
    buffer = []
    for key, value in env_vars.items():
        buffer.append(f"{key}={value}")

    path.write_text("\n".join(buffer) + "\n", encoding="utf-8")

def build_service_block(name: str, service: dict, valid_secrets: dict, valid_networks: list)-> list:
    buffer = [f"  {name}:"]

    for field in ["image", "build", "container_name", "restart"]:
        if field in service:
            buffer.append(f"    {field}: {service[field]}")

    if "ports" in service:
        buffer.append("    ports:")
        for port in service["ports"]:
            buffer.append(f'      - "{port}"')

    if "volumes" in service:
        buffer.append("    volumes:")
        for volume in service["volumes"]:
            buffer.append(f"      - {volume}")

    if "env" in service and service["env"]:
        create_env_file(name, service["env"])
        buffer.append(f"    env_file:")
        buffer.append(f"      - ./envs/{name}.env")

    if "secrets" in service:
        buffer.append("    secrets:")
        for secret_name in service["secrets"]:
            if secret_name not in valid_secrets:
                raise SystemExit(
                    f"Error: service '{name}' uses unknown secret '{secret_name}'."
                )
            buffer.append(f"      - {secret_name}")

    if "depends_on" in service:
        buffer.append("    depends_on:")
        for dependency in service["depends_on"]:
            buffer.append(f"      - {dependency}")

    if "networks" in service:
        buffer.append("    networks:")
        for net_name in service["networks"]:
            if net_name not in valid_networks:
                raise SystemExit(
                    f"Error: service '{name}' uses unknown network '{net_name}'"
                )
            buffer.append(f"      - {net_name}")

    return buffer

def build_docker_compose_file(config: dict)-> None:
    buffer = []

    secrets = config.get("secrets", {})
    networks = config.get("networks", [])
    volumes = config.get("volumes", [])
    services = config.get("services", {})

    if "project_name" in config:
        buffer.append(f"name: {config['project_name']}")
        buffer.append("")

    buffer.append("services:")
    for service_name, service_data in services.items():
        block  = build_service_block(service_name, service_data, secrets, networks)
        buffer.extend(block)

    if networks:
        buffer.append("")
        buffer.append("networks:")
        for net_name in networks:
            buffer.append(f"  {net_name}:")
            buffer.append("    driver: bridge")

    if volumes:
        buffer.append("")
        buffer.append("volumes:")

        for vol_name in volumes:
            buffer.append(f"  {vol_name}:")


    if secrets:
        buffer.append("")
        buffer.append("secrets:")

        for secret_name in secrets:
            buffer.append(f"  {secret_name}:")
            buffer.append(f"    file: ./secrets/{secret_name}.txt")

    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    compose_path = BUILD_DIR / "docker-compose.yml"
    compose_path.write_text("\n".join(buffer) + "\n", encoding="utf-8")


def main():
    config = load_config()

    create_secret_files(config.get("secrets", {}))

    build_docker_compose_file(config)

    print("[ok] build/ is ready")

if (__name__ == "__main__"):
    main()

