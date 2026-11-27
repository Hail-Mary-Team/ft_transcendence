## Team Member:

This file works as a general rules file for the working team member on this project.
Here you can find anything you need as a member from the general rules, commit policies, documentation habits, and how to run the project live.

Follow the table of content below:

### TOC :

- [General Rules](#general-rules)
- [Commits Policies](#commits-policies)
- [How to run the project step by step](#how-to-run-the-project-step-by-step)
- [Branches & Pull Requests Workflow](#branches--pull-requests-workflow)

---

### General Rules :

1. **Ship in small chunks, not giant feature dumps.** Break features into small, working pieces (for example: database schema first, then one API endpoint, then the UI hookup). Small changes are easier to review, test, and roll back if something breaks.
2. **Never push secrets, build artifacts, or heavy dependencies.** Always verify `git status` before committing so `config.json`, `build/` (generated compose file, envs, and secrets), `.env` files, `node_modules/`, and large binaries are never tracked.
3. **Document tools in `HOW_TO.md` and code explanations under `docs/project_documentation/<your_login>/`.**
   - If you introduce a new tool, CLI, or setup step that teammates need (especially without `sudo` on 42 machines), add a guide in [`HOW_TO.md`](./HOW_TO.md) and mention it in your PR/commit.
   - When you build a feature, service, or module, add a clear explanation of how your code works inside `docs/team_members/project_documentation/<your_login>/` so teammates and evaluators can follow it easily.
4. **Keep `infra/config.example.json` in sync when adding config keys.** Never put real passwords or secrets in `infra/config.example.json` use clear placeholders like `REPLACE_WITH_...` and generate your real values locally in your gitignored `config.json`.
5. Link the pull request link to the Jira work item in the comment section.
6. Anytime you add a change to the repository make a explaning in the documentation section labled with your login, so other members will understand what you did.

---

### Commits Policies :

Follow [`COMMITS.md`](./COMMITS.md) on every commit:

- **Configure your local Git identity first:** Use your 42 intra login and `@student.1337.ma` email locally in this repo.
- **Use Conventional Commits format:** `<type>(<scope>): <short imperative summary>` in lowercase, no period at the end (e.g., `feat(backend): add health endpoint`, `fix(infra): quote port mappings in compose`).
- **One logical change per commit:** Keep unrelated edits (like Docker changes, docs, and feature code) in separate commits so Vogsphere history stays clean.

---

### How to run the project step by step

1. **Install prerequisites (if not already installed):** Make sure Docker, Docker Compose, and `just` (or `make`) are available on your machine see [`HOW_TO.md`](./HOW_TO.md) for step-by-step instructions on both personal Linux machines and 42 workstations (without `sudo`).
2. **Create your local `config.json`:** Copy the example template at the repo root and replace the placeholder secrets with your own local values (keep `config.json` out of Git):
   ```bash
   cp infra/config.example.json config.json
   ```
3. **Generate `build/` and start the containers:** Run `just up` (or `make up`). This first runs build (`python3 infra/setup.py`) to generate `build/docker-compose.yml`, `build/envs/`, and `build/secrets/`, and then starts the containers (nginx, frontend, backend, postgres):

   ```bash
   just up
   ```
   Or run (make up)
4. **View the live project in your browser:** Open http://localhost:8080 to see index.html served through Nginx, and test http://localhost:8080/api/ to check the backend route.

---

### Branches & Pull Requests Workflow :

To keep `main` stable and always ready for Vogsphere evaluation, direct pushes to `main` are blocked by branch protection rules. Everyone works on their own branch named after their 42 login and merges through Pull Requests.

1. **Switch to your personal branch before writing code:**
   ```bash
   git checkout <your_login>
   git pull origin main
   ```
> (If your branch hasn't been created locally yet: git fetch origin && git checkout <your_login>)

2. **Work in small chunks and push to your own branch:**

   ```bash
   git add <files>
   git commit -m "<type>(<scope>): <short description>"
   git push origin <your_login>
   ```
3. **Open a Pull Request (PR) to main:**

- Go to the repository on GitHub and open a PR from <your_login> -> main.
- Make sure your PR contains no secrets (`config.json`, `build/`, `.env`), follows `COMMITS.md`, and includes doc updates in `HOW_TO.md` or `docs/team_members/project_documentation/<your_login>/` if needed.

4. **Review & Merge:**

- Only the repository maintainer reviews and merges PRs into `main`.
- Once your PR is merged, pull `main` back into your branch before starting your next task:

   ```bash
   git checkout <your_login>
   git pull origin main
   ```
