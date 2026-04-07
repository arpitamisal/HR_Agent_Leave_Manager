# 🏢 HR Agent – MCP Leave Manager

An **MCP (Model Context Protocol) server** for managing employee leave workflows using **LLM-driven tools, resources, and prompts**. This project enables intelligent interaction with a leave management system through natural language.

---<img width="1181" height="887" alt="Screenshot 2026-04-06 at 8 50 45 PM" src="https://github.com/user-attachments/assets/6cc45ec2-0da6-427f-8c21-fe76d088c281" />
<img width="1470" height="956" alt="Screenshot 2026-04-06 at 7 47 35 PM" src="https://github.com/user-attachments/assets/a2d52a20-19fd-43bf-bdb3-bebb0ea2765e" />
<img width="1470" height="956" alt="Screenshot 2026-04-06 at 7 47 06 PM" src="https://github.com/user-attachments/assets/f2c9ee2e-c661-4360-853e-2b3c03770120" />
<img width="1470" height="956" alt="Screenshot 2026-04-06 at 7 46 44 PM" src="https://github.com/user-attachments/assets/3a048c33-672b-48a2-9f4c-3090c480b71f" />

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
