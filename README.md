# 🏢 HR Agent – MCP Leave Manager

An **MCP (Model Context Protocol) server** for managing employee leave workflows using **LLM-driven tools, resources, and prompts**. This project enables intelligent interaction with a leave management system through natural language.

---

## 🚀 Features

- 📌 Apply for leave  
- ✅ Approve / ❌ Reject leave requests  
- 📊 Track employee leave balances  
- 👥 Retrieve employee details  
- 📋 View all leave requests  
- ✉️ Generate leave request emails using prompts  
- 🤖 LLM-integrated tool execution via MCP  
- 🔗 Seamless integration with **Claude Desktop (Developer Mode)**  

---

## 🛠️ Tech Stack

- **MCP Framework:** FastMCP  
- **Language:** Python  
- **Runtime:** uv  
- **LLM Integration:** Claude (via MCP)  
- **Backend:** In-memory data store (extendable to DB)

---

## ⚙️ How It Works

1. MCP server exposes:
   - **Tools** → leave operations (apply, approve, reject)
   - **Resources** → employee data
   - **Prompts** → email generation
2. Claude interacts with the server using MCP
3. Natural language → tool execution → structured response

---

## 📦 Installation
### Install uv if not installed
```
pip3 install uv
```

### Create project
```
uv init my-first-mcp-server
cd my-first-mcp-server
```

### Add MCP
```
uv add "mcp[cli]"
```

---

## ▶️ Run the Server
```
uv run main.py
```
## 🔗 Connect to Claude Desktop
### Enable Developer Mode
### Install MCP server:
```
uv run mcp install main.py
```
### Restart Claude Desktop

---

## 💡 Example Queries
- “Apply leave for employee E001 from 2024-04-10 to 2024-04-12”
- “Approve leave request L001”
- “Check leave balance for E002”
- “Show all leave requests”

---

## 📊 Project Impact
- Automated leave management workflows
- Enabled LLM-driven tool execution
- Reduced manual HR operations through structured automation
- Built modular system using tools, resources, and prompts

---

## 🔮 Future Improvements
- 🗄️ Database integration (PostgreSQL / SQLite)
- 🔐 Authentication & role-based access
- 📊 Dashboard UI
- 📁 Multi-organization support
- 📈 Analytics on leave patterns
