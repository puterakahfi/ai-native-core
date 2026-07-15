# Native AI Runtime Ops Skill

## Purpose

Operate the canonical runtime host for a Native AI workspace: SSH access, cloud/VPS setup, Hermes profile bootstrap, project checkout, gateway/tmux/systemd operations, backups, and session-state safety.

This skill is for runtime operations, not domain architecture. Use `native-ai-engineer` first when deciding whether something belongs in core, app adapter, skill adapter, profile distribution, or runtime state.

## Boundary

```text
native-ai-runtime-ops = operate the host that runs the agent/runtime
native-ai-engineer    = decide architecture/contracts/layer placement
native-ai-runtime-agent = execute a product adapter once Hermes is running inside a workspace
```

Core defines the operational contract and safety gates. Runtime adapters provide concrete commands for Hermes, SSH, tmux, gateways, backups, and cloud-specific setup.

## When To Use

Use this skill when the work involves:

- connecting to a VPS/cloud host over SSH
- making a cloud machine the canonical Hermes runtime
- installing or updating a Hermes profile distribution on a remote host
- setting up `tmux`, gateway, cron, or systemd for always-on agent work
- cloning project repositories onto the runtime host
- designing backup/restore for Hermes session state
- enforcing single-writer policy for `state.db`, sessions, memories, and cron
- checking remote runtime health and readiness

Do not use for ordinary product feature work, UI implementation, or generic code review.

## Core Operating Model

```text
profile distribution repo
  -> installs reproducible config, SOUL, scripts, skills.lock.yaml

canonical runtime host
  -> owns live Hermes state: state.db, sessions, memories, cron, auth, .env

client devices
  -> connect to the canonical runtime through SSH, gateway, remote desktop, or another client surface

project repositories
  -> share source code through Git, independent of Hermes session state
```

Live runtime state must not be active-active synced through Git, Dropbox, Syncthing, or a profile distribution repo.

## Process

### 1. Identify Runtime Host

Collect only non-secret connection facts:

```text
provider: Tencent Cloud / VPS / local workstation / other
public_ip_or_host: provided by user
os_image: Ubuntu/Debian/CentOS/TencentOS/etc.
username: ubuntu/root/debian/etc.
login_method: ssh key / password / console
key_path: local path only, never private key content
```

Completion criterion: SSH target and login method are known without exposing secrets.

### 2. Verify Access Safely

Prefer read-only checks first:

```bash
ssh -i ~/.ssh/key.pem user@host 'hostname && whoami && uname -a'
```

For persistent use, create local SSH config:

```sshconfig
Host native-ai-runtime
  HostName <PUBLIC_IP_OR_DNS>
  User <USER>
  IdentityFile ~/.ssh/<KEY_FILE>
  IdentitiesOnly yes
  ServerAliveInterval 30
  ServerAliveCountMax 4
```

Completion criterion: the operator can run a harmless remote command and identify the host.

### 3. Bootstrap Canonical Hermes Profile

Install profile distribution on the runtime host:

```bash
hermes profile install <profile_distribution_repo> --name ai-native-engineering -y
~/.hermes/profiles/ai-native-engineering/scripts/install-skills.sh ai-native-engineering
hermes -p ai-native-engineering doctor
```

Then configure local-only auth and environment on the runtime host:

```bash
hermes -p ai-native-engineering model
hermes -p ai-native-engineering auth
hermes -p ai-native-engineering config check
```

Completion criterion: profile, skills, model/auth, and doctor checks are verified with actual command output.

### 4. Prepare Project Workspace

Clone or update the product/app repositories on the runtime host:

```bash
mkdir -p ~/projects
cd ~/projects
git clone <repo-url>
cd <repo>
```

Run project-specific dependency checks only after reading the repo manifest and instructions.

Completion criterion: the canonical runtime host has the project checkout needed for future sessions.

### 5. Operate Through a Durable Surface

For simple remote use:

```bash
ssh native-ai-runtime
tmux new -A -s hermes-ai
cd ~/projects/<repo>
hermes -p ai-native-engineering --continue
```

For always-on messaging/remote clients, use Hermes gateway or desktop remote login, but keep the canonical runtime as the only session state owner.

Completion criterion: client devices connect to the canonical runtime instead of creating independent state.

### 6. Backup and Restore Policy

Before treating a host as canonical, define backup:

```bash
hermes profile export ai-native-engineering -o ~/backups/hermes/ai-native-engineering-$(date +%F).tar.gz
```

Backups may contain secrets and live state. Store them encrypted and private, not in Git.

Completion criterion: backup target, retention, encryption, and restore test policy are known.

## Safety Rules

Never commit or sync these through profile/source repos:

```text
state.db
state.db-wal
state.db-shm
sessions/
memories/
cron/
auth.json
.env
.env.*
logs/
cache/
secrets/
tokens/
credentials/
```

Only one runtime should write to a given Hermes profile state at a time.

## Output Modes

### SSH Handoff

```markdown
## Target
## Local SSH Config
## First Connection Command
## Security Group / Firewall Check
## Verification Command
## Next Runtime Bootstrap Step
```

### Canonical Runtime Setup

```markdown
## Host
## Profile Distribution
## Install Commands
## Project Checkout
## Client Access Path
## Backup Policy
## Verification Evidence
```

### Runtime Healthcheck

```markdown
## Host Identity
## Hermes Version
## Profile Path
## Session Store Status
## Skills Installed
## Project Readiness
## Gateway/Cron Status
## Risks / Follow-ups
```

## Verification Checklist

- [ ] SSH access verified with harmless command output.
- [ ] Profile installed from distribution repo.
- [ ] Skill lockfile materialized installed skills.
- [ ] Secrets/auth configured locally only.
- [ ] Project repo checked out and basic readiness verified.
- [ ] Single-writer session policy documented.
- [ ] Backup/restore policy defined before relying on the runtime.
- [ ] No live state or secrets are committed to Git.
