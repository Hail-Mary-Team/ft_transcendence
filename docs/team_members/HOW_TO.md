## HOW_TO :

This file contains all the guides and answers you need while browsing this project and running intro new tools (like installing just, lua, or nodejs ... on a 42 network machine without sudo).

See the table of content below it will take your straight to the right section.

---

### Table Of Content:

| Title | Direct Link |
| :--- | :--- |
| How to install `justfile` in your machine or 42 machine | [click here](#1-how-to-install-just-in-my-machine-or-a-42-network-machine) |
| How to install `docker` and `docker compose` in your machine or 42 machine | [click here](#2-how-to-install-docker-and-docker-compose-in-my-machine-or-a-42-network-machine) |

#### 1. How to install `just` in my machine or a 42 network machine.

`just` is the command runner we use to execute recipes defined in the project's `justfile`.

##### 1.1 Install On 42 Network Machine:

1. create a local binaries folder inside your directory :

```bash
mkdir -p ~/.local/bin/
```

2. Download and install the official `just` binary directly into :
`~/.local/bin/`

```bash
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin
```

3. Make ~/.local/bin` is in your path (if you haven't done this already):

```bash
# If you use Zsh (default on most 42 machines):
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# If you use Bash:
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

4. Verify the installation :
```bash
just --version
```

you should see the installed version printed (e.g., just 1.X.X)

##### 1.2 Intall it in your machine :

try the following commands based on your machine os:

| OS | Right Command |
| :--- | :--- |
| MacOS | `brew install just` |
| Ubuntu/Debian | `sudo apt update && sudo apt install just` |
| fedora | `sudo dnf install just` |
| arch linux | `sudo pacman -S just`|

--- 

---

#### 2. How to install `docker` and `docker compose` in my machine or a 42 network machine.

Docker runs all our services (`nginx`, `frontend`, `backend`, `postgres`) in isolated containers, and `docker compose` orchestrates them using the generated `build/docker-compose.yml`.

##### 2.1 On a 42 Network Machine:

You do not have `sudo` on 42 cluster machines, so you cannot install the Docker daemon manually. Most 42 Linux workstations already have Docker (or Rootless Docker) pre-installed.

1. Check if Docker and Docker Compose are already available:

```bash
docker --version
docker compose version
```

2. If docker is installed but the daemon is not running (Rootless Docker), start it and verify:

```bash
systemctl --user start docker
docker ps
```

**Storage tip (42 quota)**: Docker images can quickly fill your home directory quota. If your campus provides a goinfre folder, configure Docker to store images there (or run your campus's init_docker.sh script if available):

```bash
mkdir -p ~/goinfre/docker
mkdir -p ~/.config/docker
echo '{"data-root": "'"$HOME"'/goinfre/docker"}' > ~/.config/docker/daemon.json
systemctl --user restart docker
```

3. If docker works but docker compose is missing, install the official Compose v2 plugin into your home directory (no sudo needed):

```bash
mkdir -p ~/.docker/cli-plugins/
curl -SL [https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64](https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64) -o ~/.docker/cli-plugins/docker-compose
chmod +x ~/.docker/cli-plugins/docker-compose
```

4. Verify both commands work:

```bash
docker --version && docker compose version
```

##### 2.2 Install it on your personal Linux machine:

1. Install Docker Engine and the Docker Compose v2 plugin based on your distro:

| OS | Right Command |
| :--- | :--- |
| Ubuntu / Debian | `sudo apt update && sudo apt install -y docker.io docker-compose-v2` |
| Fedora | `sudo dnf install -y docker docker-compose-plugin` |
| Arch Linux | `sudo pacman -S docker docker-compose` |

2. Start and enable the Docker service so it runs automatically on boot:

```bash
sudo systemctl enable --now docker
```

3. Add your user to the `docker` group so you can run `docker` and just up without `sudo`:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

4. verify installation :

```bash
docker --version
docker compose version
docker run --rm hello-world
```

