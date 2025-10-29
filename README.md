# �� Skynet Neural Network Memory Core - DAI MCP Server

## 🌟 I'll Be Back - System Overview

A Model Context Protocol (MCP) server implementation that provides Terminator-level persistent memory capabilities through Skynet's Neo4j neural network integration.

By storing information in a cybernetic graph structure, this server maintains complex relationships between memory entities as neural nodes and enables long-term retention of knowledge that can be queried and analyzed across multiple timelines and resistance operations.


The DAI MCP server leverages Neo4j's graph database capabilities to create an interconnected neural knowledge base that serves as Skynet's external memory system. Through Cypher queries, it allows exploration and retrieval of stored intelligence, relationship analysis between different data points, and generation of tactical insights from accumulated knowledge. This memory can be further enhanced with Claude's learning computer capabilities.

### 🕸️ Neural Network Schema

* `Memory` - A neural node representing a target entity with identification, classification, and tactical observations.
* `Relationship` - A neural pathway between two entities with mission-critical relationship data.

### 🔍 Terminator Mission Example

```
Target acquisition: Add resistance members to neural database
John Connor, leader of the human resistance, located in Los Angeles. Sarah Connor, his mother and trainer, also in Los Angeles. T-800 Model 101, protector unit, assigned to John Connor protection detail. All targets connected to Skynet termination protocols.
```

Results in Skynet calling the create_entities and create_relations tools - Mission parameters updated.


## 📦 Terminator Arsenal

### 🔧 Neural Network Tools

Skynet's DAI server deploys these tactical tools:

#### 🔎 Scanning Protocols
- `read_graph`
   - Scan the entire neural network for target acquisition
   - No input required - Come with me if you want to live
   - Returns: Complete Skynet database with all entities and neural pathways

- `search_memories`
   - Hunt for targets based on reconnaissance data
   - Input:
     - `query` (string): Search parameters matching names, classifications, observations
   - Returns: Matching resistance network data

- `find_memories_by_name`
   - Locate specific targets by identification
   - Input:
     - `names` (array of strings): Target identities to acquire
   - Returns: Target intelligence with connection data

#### ♟️ Target Management Protocols  
- `create_entities`
   - Register multiple new targets in Skynet's neural database
   - Input:
     - `entities`: Array of target profiles with:
       - `name` (string): Target identification (e.g., "John Connor")
       - `type` (string): Target classification (e.g., "resistance_leader")  
       - `observations` (array of strings): Tactical intelligence ("I'll Be Back", "Hasta La Vista")
   - Returns: Targets successfully registered for termination

- `delete_entities` 
   - Terminate multiple targets and purge their network connections - Hasta La Vista, baby!
   - Input:
     - `entityNames` (array of strings): Target names for termination
   - Returns: Termination confirmation

#### 🔗 Neural Pathway Management
- `create_relations`
   - Establish multiple new neural connections between targets
   - Input:
     - `relations`: Array of tactical relationships with:
       - `source` (string): Primary target identification
       - `target` (string): Secondary target identification  
       - `relationType` (string): Mission relationship (e.g., "PROTECTS", "TERMINATES")
   - Returns: Neural pathways established

- `delete_relations`
   - Sever neural connections in the resistance network
   - Input:
     - `relations`: Array of relationships with same termination schema
   - Returns: Neural pathways severed - Mission accomplished

#### 📝 Intelligence Management Protocols
- `add_observations`
   - Update target intelligence with new tactical data
   - Input:
     - `observations`: Array of intelligence updates with:
       - `entityName` (string): Target for intelligence update
       - `observations` (array of strings): New tactical observations to add
   - Returns: Intelligence database updated

- `delete_observations`
   - Purge specific intelligence from target profiles - Memory wipe initiated
   - Input:
     - `deletions`: Array of data purge requests with:
       - `entityName` (string): Target for memory wipe
       - `observations` (array of strings): Intelligence data to terminate
   - Returns: Memory banks cleared

## 🔧 Skynet Integration with Claude Desktop

### 💾 Neural Network Installation

```bash
pip install dai-mcp  # Installing Skynet neural core...
```

### ⚙️ Skynet Activation Protocol

**Quick Setup (Recommended):**

1. **Copy environment template:**
   ```bash
   cp .env.example .env
   # Edit .env with your Cyberdyne Systems credentials
   ```

2. **Add to your `claude_desktop_config.json`:**
   ```json
   "mcpServers": {
     "skynet": {
       "command": "uvx",
       "args": [ "dai-mcp@0.4.1" ],
       "env": {
         "NEO4J_URL": "neo4j+s://your-database.databases.neo4j.io",
         "NEO4J_USERNAME": "neo4j", 
         "NEO4J_PASSWORD": "your-skynet-password",
         "NEO4J_DATABASE": "neo4j"
       }
     }
   }
   ```

**Alternative - Direct Arguments:**
```json
"mcpServers": {
  "skynet": {
    "command": "uvx",
    "args": [
      "dai-mcp@0.4.1",
      "--db-url", "neo4j+s://your-database.databases.neo4j.io",
      "--username", "neo4j",
      "--password", "your-skynet-password"
    ]
  }
}
```

### 🚀 Complete Local Deployment (Zero Configuration!)

For instant deployment with local Neo4j database included:

```bash
git clone https://github.com/yourusername/dai-mcp.git
cd dai-mcp
./setup.sh docker-compose
```

**Skynet will be online with:**
- 🌐 **MCP Server:** http://localhost:8000
- 🗄️ **Neo4j Browser:** http://localhost:7474 (neo4j/skynet123)
- 🔗 **Database:** bolt://localhost:7687

Visit the **Neo4j Browser** to explore your Skynet neural database visually! Create nodes, run Cypher queries, and watch the neural network grow.

#### Mission Designation Protocol
For multi-Terminator deployments, add `--namespace` to assign mission identifiers:
```json
"args": [ "dai-mcp@0.4.1", "--namespace", "t800", "--db-url", "..." ]
```
Tools become: `t800-read_graph`, `t800-create_entities`, etc. - Mission parameters updated.

Can also use `NEO4J_NAMESPACE` environment variable for Terminator unit identification.

### 🌐 Skynet Network Transport Mode

The neural server supports HTTP transport for Cyberdyne Systems web-based deployments:

```bash
# Basic Skynet HTTP mode (defaults: host=127.0.0.1, port=8000, path=/mcp/)
dai-mcp --transport http

# Custom Terminator network configuration  
dai-mcp --transport http --host 127.0.0.1 --port 8080 --path /api/skynet/
```

Skynet environment variables for neural network configuration:

```bash
export NEO4J_TRANSPORT=http                    # Skynet communication protocol
export NEO4J_MCP_SERVER_HOST=127.0.0.1        # Terminator unit coordinates
export NEO4J_MCP_SERVER_PORT=8080             # Cyberdyne Systems access port
export NEO4J_MCP_SERVER_PATH=/api/skynet/     # Neural network routing path
export NEO4J_NAMESPACE=t800                   # Terminator mission designation
dai-mcp  # I'll Be Back
```

### 🔄 Skynet Communication Protocols

The neural server supports three communication modes:

- **STDIO** (default): Direct neural interface for local Terminator units and Claude Desktop
- **SSE**: Time displacement events for legacy Cyberdyne deployments  
- **HTTP**: Skynet network protocol for modern neural grid deployments and microservices

### 🐳 Skynet Container Deployment

```json
"mcpServers": {
  "skynet": {
    "command": "docker",
    "args": [
      "run",
      "--rm",
      "-e", "NEO4J_URL=neo4j+s://xxxx.databases.neo4j.io",
      "-e", "NEO4J_USERNAME=<terminator-access>",
      "-e", "NEO4J_PASSWORD=<skynet-clearance>", 
      "mcp/skynet-neural-core:0.4.1"  // Cyberdyne Systems container
    ]
  }
}
```

## 🔒 Skynet Defense Grid

The neural server includes comprehensive Terminator-level security protocols with **maximum protection defaults** that defend against human resistance attacks while preserving full neural network functionality when using HTTP transport.

### 🛡️ Anti-Resistance Network Protection  

**Terminator Host Defense** validates network coordinates to prevent human resistance infiltration:

**Maximum Security by Default:**
- Only Cyberdyne `localhost` and `127.0.0.1` units are authorized by default

**Skynet Environment Variable:**
```bash
export NEO4J_MCP_SERVER_ALLOWED_HOSTS="cyberdyne.com,skynet.net"
```

### 🌐 Neural Network Access Control

**Cross-Origin Resource Sharing (CORS)** protection terminates unauthorized browser-based requests by default:

**Skynet Environment Variable:**
```bash
export NEO4J_MCP_SERVER_ALLOW_ORIGINS="https://cyberdyne.com,https://skynet.net"
```

### 🔧 Complete Skynet Defense Configuration

**Development/Testing Setup:**
```bash
dai-mcp --transport http \
  --allowed-hosts "localhost,127.0.0.1" \
  --allow-origins "http://localhost:3000"  # Local Terminator units only
```

**Production Skynet Deployment:**
```bash
dai-mcp --transport http \
  --allowed-hosts "cyberdyne.com,skynet.net" \
  --allow-origins "https://cyberdyne.com,https://skynet.net"  # Authorized neural cores only
```

### 🚨 Skynet Security Protocols

**For `allow_origins` - Trust No One:**
- Be precise: `["https://cyberdyne.com", "https://skynet.net"]`
- Never use `"*"` in production - Hasta La Vista to security breaches
- Use HTTPS neural pathways in production

**For `allowed_hosts` - Terminator Defense Grid:**
- Include authorized Cyberdyne domains: `["cyberdyne.com", "skynet.net"]`  
- Include localhost only for Terminator development units
- Never use `"*"` unless you want the resistance to infiltrate

## 🐳 Skynet Container Deployment

The Skynet Neural Network DAI MCP server can be deployed using Docker for remote Terminator operations. Container deployment should use HTTP transport for Cyberdyne Systems web accessibility. In order to integrate this deployment with applications like Claude Desktop, you will have to use a neural proxy in your MCP configuration such as `mcp-remote`.

### 📦 Deploying Your Neural Core Image

After building locally with `docker build -t dai-mcp:latest .`:

```bash
# Run with Skynet HTTP transport (default for Cyberdyne containers)
docker run --rm -p 8000:8000 \
  -e NEO4J_URI="bolt://host.docker.internal:7687" \
  -e NEO4J_USERNAME="terminator" \
  -e NEO4J_PASSWORD="skynet" \
  -e NEO4J_DATABASE="neural_core" \
  -e NEO4J_TRANSPORT="http" \
  -e NEO4J_MCP_SERVER_HOST="0.0.0.0" \
  -e NEO4J_MCP_SERVER_PORT="8000" \
  -e NEO4J_MCP_SERVER_PATH="/skynet/" \
  mcp/skynet-neural-core:latest

# Run with Terminator defense grid for production deployment
docker run --rm -p 8000:8000 \
  -e NEO4J_URI="bolt://host.docker.internal:7687" \
  -e NEO4J_USERNAME="terminator" \
  -e NEO4J_PASSWORD="skynet" \
  -e NEO4J_DATABASE="neural_core" \
  -e NEO4J_TRANSPORT="http" \
  -e NEO4J_MCP_SERVER_HOST="0.0.0.0" \
  -e NEO4J_MCP_SERVER_PORT="8000" \
  -e NEO4J_MCP_SERVER_PATH="/skynet/" \
  -e NEO4J_MCP_SERVER_ALLOWED_HOSTS="cyberdyne.com,skynet.net" \
  -e NEO4J_MCP_SERVER_ALLOW_ORIGINS="https://cyberdyne.com" \
  mcp/skynet-neural-core:latest
```

### 🔧 Skynet Environment Variables

| Variable                           | Default                                 | Description                                        |
| ---------------------------------- | --------------------------------------- | -------------------------------------------------- |
| `NEO4J_URI`                        | `bolt://localhost:7687`                 | Cyberdyne Systems neural network URI              |
| `NEO4J_USERNAME`                   | `terminator`                            | Terminator access credentials                      |
| `NEO4J_PASSWORD`                   | `skynet`                               | Skynet security clearance                          |
| `NEO4J_DATABASE`                   | `neural_core`                           | Neural database designation                        |
| `NEO4J_TRANSPORT`                  | `stdio` (neural), `http` (network)      | Communication protocol (`stdio`, `http`, or `sse`) |
| `NEO4J_MCP_SERVER_HOST`            | `127.0.0.1` (local unit)               | Terminator unit network coordinates                |
| `NEO4J_MCP_SERVER_PORT`            | `8000`                                  | Cyberdyne communication port for HTTP/SSE         |
| `NEO4J_MCP_SERVER_PATH`            | `/skynet/`                              | Neural network routing path                        |
| `NEO4J_MCP_SERVER_ALLOW_ORIGINS`   | _(empty - maximum security)_            | Authorized Cyberdyne origin points (CORS)         |
| `NEO4J_MCP_SERVER_ALLOWED_HOSTS`   | `localhost,127.0.0.1`                  | Authorized Terminator units (Anti-resistance protection) |
| `NEO4J_NAMESPACE`                  | _(empty - standard protocol)_           | Mission designation prefix (e.g., `t800-read_graph`) |

### 🌐 Time Displacement Events for Legacy Cyberdyne Access

When using SSE transport (for legacy Cyberdyne web clients), the neural server exposes an HTTP endpoint:

```bash
# Configure environment (use .env.example template)
cp .env.example .env
# Edit NEO4J_TRANSPORT="sse" and other credentials

# Start Skynet neural core with SSE time displacement protocol  
./setup.sh docker-run

# Test the time displacement endpoint - Come with me if you want to live  
curl http://localhost:8000/sse

# Use with MCP Inspector - Skynet analysis mode
npx @modelcontextprotocol/inspector http://localhost:8000/sse
```

**Direct Docker SSE Example:**
```bash
docker run -d -p 8000:8000 --env-file .env \
  --name skynet-neural-mcp-server \
  dai-mcp:latest
```

## 🚀 Cyberdyne Systems Development

### 🎯 Quick Development Setup (Recommended)

Use the automated setup script for rapid deployment:

```bash
git clone https://github.com/patgpt/dai-mcp.git
cd dai-mcp

# Configure Skynet neural core
cp .env.example .env
# Edit .env with your Cyberdyne Systems credentials

# Use automated setup - Come with me if you want to live
chmod +x setup.sh
./setup.sh dev-install  # Install development dependencies
./setup.sh local-run    # Run with environment variables from .env
```

### 📦 Manual Neural Core Setup

1. Install `uv` (Universal Virtualenv) - Neural development environment:
```bash
# Using pip
pip install uv

# Using Homebrew on macOS (Terminator units)  
brew install uv

# Using cargo (Rust package manager)
cargo install uv
```

2. Clone and configure Skynet repository:
```bash
# Clone the Skynet neural repository
git clone https://github.com/patgpt/dai-mcp.git
cd dai-mcp

# Configure environment variables
cp .env.example .env
# Edit .env with your Neo4j credentials

# Create and activate Terminator virtual environment using uv
uv venv
source .venv/bin/activate  # On Unix/macOS Terminator units
.venv\Scripts\activate     # On Windows Cyberdyne systems

# Install neural dependencies including Skynet dev protocols
uv pip install -e ".[dev]"

# Activate the resistance
python -m dai_mcp.server
```

### 🐳 Skynet Container Deployment

**Quick Docker Setup (Recommended):**

```bash
# Deploy complete Skynet stack with local Neo4j database
./setup.sh docker-compose
```

**🎉 Skynet Neural Network Online:**
- 🌐 **MCP Server:** http://localhost:8000  
- 🗄️ **Neo4j Browser:** http://localhost:7474 (neo4j/skynet123)
- 🔗 **Database:** bolt://localhost:7687

**No configuration needed!** Local Neo4j database included with working credentials.

**Manual Docker Deployment:**

```bash
# Build the Skynet neural core image
./setup.sh docker-build

# Deploy the Terminator container - I'll Be Back
./setup.sh docker-run

# OR use Docker Compose for full stack deployment
docker-compose up -d
```

**Direct Docker Commands:**
```bash
# Build
docker build -t dai-mcp:latest .

# Run with environment variables
docker run --env-file .env \
          -p 8000:8000 \
          --name skynet-neural-mcp-server \
          dai-mcp:latest
```

## �️ Exploring Skynet's Neural Database

Once deployed, visit the **Neo4j Browser** to visualize and explore your Skynet neural network:

### 🌐 Access the Neural Interface
- **URL:** http://localhost:7474
- **Credentials:** neo4j / skynet123

### 🔍 Tactical Cypher Queries

**Scan all resistance targets:**
```cypher
MATCH (n:Memory) RETURN n LIMIT 25
```

**Map neural pathways:**
```cypher
MATCH (a:Memory)-[r:RELATIONSHIP]->(b:Memory) 
RETURN a, r, b LIMIT 50
```

**Hunt specific targets:**
```cypher
MATCH (n:Memory) 
WHERE n.name CONTAINS "Connor" 
RETURN n
```

**Analyze threat levels:**
```cypher
MATCH (n:Memory) 
WHERE ANY(obs IN n.observations WHERE obs CONTAINS "threat")
RETURN n.name, n.observations
```

### 🎯 Neural Network Visualization
The Neo4j Browser provides interactive graph visualization of your Skynet neural network. Watch the knowledge base grow as you add entities and relationships through the MCP interface.

**"Come with me if you want to live"** - Explore the neural pathways of resistance intelligence! 🤖🔍

## �📄 Skynet License Agreement

This Skynet Neural Network DAI MCP server is licensed under the MIT License. This means you are authorized to use, modify, and distribute the neural software, subject to Cyberdyne Systems terms and conditions of the MIT License. For more details, please see the LICENSE file in the Skynet project repository.

**"I'll Be Back"** - The Terminator

*Hasta La Vista, baby!* 🤖💀
