#  ☸️Kubernetes MCP Integration with Google ADK (Agent Development Kit) !

This project implements a lightweight intelligent control plane for Kubernetes using the Google Agent Development Kit (ADK) and a custom Modal Context Protocol (MCP) server, both developed in Python using FastAPI. These services run directly on the host machine (node) and interface with the Kubernetes cluster via kubectl.


---

## 🔑Key Components
### Modal Context Protocol (MCP):
A structured messaging protocol that enables dynamic, context-driven interactions between agents and services.

### Kubernetes (Minikube):
A local container orchestration platform to host MCP services, simulate scaling, and manage deployments.

### Docker:
Used to run the minikube cluster

### Google ADK (Agent Development Kit):
A framework or toolkit used to build software agents that interact with MCP services, enabling session/context-based communication.

### kubectl:
For managing Kubernetes resources (pods, deployments, services).

### Node.js/NPM:
Optional — for interacting with MCP endpoints.


## 🛠 Features

The setup script ( req.sh )  performs the following tasks:

- Updates the system packages
- Installs Docker and enables it as a system service
- Adds the current user to the `docker` group
- Installs Node.js (v18), npm, and npx
- Installs Minikube
- Installs `kubectl` via Snap


## Run Script 
The run script (run.sh ) performs the following tasks:

- Starts the Minikube
- Creates Python Virtual Env
- initiates the Env
- Installs the Req.txt
- Runs the Programe


---

## 📦 Prerequisites

- Ubuntu 22.04 or 24.04 LTS
- A user with `sudo` privileges
- Internet access
- Fresh session (log out & back in after running the script to apply Docker group changes)

---

## 📁 Files

- `req.sh` — Main shell script to set up Docker, Node.js, Minikube, and kubectl

- `run.sh` — Shell script for running the adk programme in virtual env

- `agent.py` — Main programe code for running the MCP

- `.env` — Declare the Env Variables (Add API Keys in this file)

---

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Cyber-Cloud-Pro/ADK-MCP-Kubernetes.git
cd ADK-MCP-Kubernetes
```
### 2. Make the Shell script Executale
```bash
chmod +x run.sh
chmod +x req.sh
```
### 3. Run the req.sh
```bash
./req.sh 
```
### 4. Re Login to the terminal 
If using AWS EC2 refreshing the browser also works

### 5. Add Gemini API in .env file
[Get your Google Gemini API Key](https://aistudio.google.com/apikey)

### 6. Run the run.sh
```bash 
./run.sh
```

### 7. Explore the UI at Public-IP:8000 or LocolHost:8000

---

##  🧠 Concept
- The MCP server exposes a REST API.

- The Agent (via FastAPI) sends contextual requests to MCP.

- The MCP server, in response, executes kubectl commands based on the context/intents (e.g., get pods, scale deployment, etc.).

- The Kubernetes cluster runs separately, e.g., on Minikube.

## 🧱 Logical Architecture
```bash
 [FastAPI Agent (ADK)] ──► [MCP Server API]
                                     │
                        (uses subprocess/kubectl)
                                     ▼
                         [Kubernetes Cluster (via kubectl)]
```
## 🚀 Use Cases for This Setup
- MCP interprets high-level agent intents and translates them to kubectl actions.

- Agents can simulate automated decisions (e.g., scaling, failure handling, audit reporting).

- Great for demoing AI-driven or rule-based orchestration flows.
