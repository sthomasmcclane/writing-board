> [!IMPORTANT]
> This project has been consolidated into **[Writer's EDC](https://github.com/sthomasmcclane/writers-edc)**. This repository is now legacy and has been **Archived**. The code remains available for reference, but no further updates will be made here.

# 📋 Writing Board

A standalone, web-based Kanban board for managing writing projects and ideas.

## 🚀 Features
- **Kanban Workflow**: Move cards between Ideas, Development, Drafting, and Polishing.
- **Auto-Emoji**: Cards automatically get icons based on keywords (e.g., `comics`, `fiction`, `spicy`).
- **Persistence**: Save your board state directly to the server with one click.
- **Docker Ready**: Standardized deployment using Docker Compose.

## 🛠️ Deployment
This project is deployed following the server's standard Docker hierarchy:
- **Compose Path**: `/opt/docker/compose/writing-board`
- **Port**: `5080`

### To start:
```bash
docker compose up -d
```

## 📝 Usage
1. Open `http://<server-ip>:5080` in your browser.
2. Add or move cards as needed.
3. Click **"Save Board"** to persist your changes to the server's disk.

---
Part of the Writer's Ecosystem.
