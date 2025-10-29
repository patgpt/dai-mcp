FROM python:3.11-slim

# OCI Labels for Docker MCP Toolkit Discovery
LABEL org.opencontainers.image.title="Skynet Neural Network DAI MCP Server"
LABEL org.opencontainers.image.description="Persistent memory and knowledge graph for LLMs via Model Context Protocol"
LABEL org.opencontainers.image.version="0.4.1"
LABEL org.opencontainers.image.authors="Patrick Kelly"
LABEL org.opencontainers.image.url="https://github.com/patgpt/dai-mcp"
LABEL org.opencontainers.image.documentation="https://github.com/patgpt/dai-mcp#readme"
LABEL org.opencontainers.image.source="https://github.com/patgpt/dai-mcp"
LABEL org.opencontainers.image.licenses="MIT"

# MCP Server Metadata
LABEL mcp.server.name="skynet-neural-core"
LABEL mcp.server.type="knowledge-graph"
LABEL mcp.server.transport="http"
LABEL mcp.server.port="8000"

# Set working directory
WORKDIR /app

# Install build dependencies
RUN pip install --no-cache-dir hatchling

# Copy dependency files first
COPY pyproject.toml /app/

# Install runtime dependencies
RUN pip install --no-cache-dir fastmcp>=2.0.0 neo4j>=5.26.0

# Copy the source code
COPY src/ /app/src/
COPY README.md /app/


# Install the package
RUN pip install --no-cache-dir -e .

# Environment variables for Skynet neural network connection (defaults)
ENV NEO4J_URL="bolt://host.docker.internal:7687"
ENV NEO4J_USERNAME="neo4j"
ENV NEO4J_PASSWORD="password"
ENV NEO4J_DATABASE="neo4j"
ENV NEO4J_TRANSPORT="http"
ENV NEO4J_MCP_SERVER_HOST="0.0.0.0"
ENV NEO4J_MCP_SERVER_PORT="8000"
ENV NEO4J_MCP_SERVER_PATH="/skynet/"
ENV NEO4J_MCP_SERVER_ALLOW_ORIGINS=""
ENV NEO4J_MCP_SERVER_ALLOWED_HOSTS="localhost,127.0.0.1"
ENV NEO4J_NAMESPACE=""

# I'll Be Back - Command to run Skynet neural core with HTTP transport for Docker
CMD ["sh", "-c", "dai-mcp --transport http"]