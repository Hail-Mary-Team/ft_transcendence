# Commits :

We are working on GitHub day to day and pushing the full history to Vogsphere when it's time for the evaluation. Following one simple commit style keeps the history readable for the team and avoids messy surprises during defense.

---

## 1. Setup Your Local Identity First :

Before making your first commit in this repo, set your 42 intra login as the name name and email **locally** (this only affects this folder where you clone the repository, not your other GitHub projects):

```bash
git config user.name "your_intra_login"
git config user.email "your_intra_login@student.1337.ma"
```

> **Note:** Don't put the date, time, or your name inside the commit message itself. Git already tracks the exact timestamp and author automatically on every commit.

---

## 2. The Format :

Every commit should follow this pattern:

```text
<type>(<scope>): <what you changed>
```

Keep it short, lowercase, and written like a command ("add", "fix", "update" not "added" or "fixed"). No period at the end.

If a commit needs extra context, leave one blank line and explain **why** below it:

```text
feat(infra): switch postgres password to docker secrets

Mounts the password at /run/secrets/postgres_password instead of
exposing it in plain environment variables.
```

---

## 3. Types :

| Type | When to use it |
| :--- | :--- |
| `feat` | Adding a new feature, service, or capability |
| `fix` | Fixing a bug or broken config |
| `docs` | Editing `README.md`, `HOW_TO.md`, or anything inside `docs/` |
| `refactor` | Cleaning up or restructuring code without changing how it works |
| `chore` | Tooling, `Makefile`, `justfile`, `.gitignore`, or maintenance work |
| `style` | Formatting, indentation, or naming tweaks (no logic change) |
| `test` | Adding or updating tests |

---

## 4. Scopes

The scope tells everyone *which part* of the project you touched. Right now, our main scopes are:

- `infra` — Lua generator (`setup.lua`), `config.example.lua`, Docker setup
- `db` — PostgreSQL setup, schemas, or migrations
- `pav` — anything inside `core/pav/`
- `docs` — documentation files
- `tooling` — `justfile`, `Makefile`, `.gitignore`

> **Heads up : scopes will change as the project grows.**  
> We are still early, so this list is not locked. As we add new services inside `core/` (like `backend`, `frontend`, `worker`, `auth`, `chat`, etc.), just use that folder or service name as your scope and update this list. If a commit touches multiple places at once, you can skip the scope: `chore: update root gitignore`.

---

## 5. Examples

**Good:**

```text
feat(infra): generate per-service envs and secrets from config.lua
fix(db): use POSTGRES_PASSWORD_FILE so postgres reads docker secret
docs(howto): add no-sudo install steps for lua and just
chore(tooling): add clean and check recipes to justfile
```

**Avoid:**

```text
update
fix stuff
wip
22/11/2026 - fixed the database finally
```

---

## 6. Rules to Keep Vogsphere Happy

Vogsphere scans the **entire** Git history when we push, not just the latest commit. One bad commit today can block our push on evaluation day.

- **Never commit secrets or generated files.** Make sure `config.lua`, `build/`, `.env`, and any password/API key files stay ignored.
- **No heavy binaries or build junk.** Don't commit `node_modules/`, compiled files, or huge uncompressed assets.
- **One logical change per commit.** Don't mix a Docker config change, a docs rewrite, and a backend bug fix into one giant commit — split them up so they're easy to review and revert if something breaks.
