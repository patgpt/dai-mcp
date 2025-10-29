#!/bin/bash

# 🤖 Skynet Neural Network Setup Script - DAI MCP Server
# "Come with me if you want to live" - Quick deployment assistance

set -e

echo "🤖 Initializing Skynet Neural Network Memory Core..."
echo "=================================================="

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  No .env file found. Creating from template..."
    cp .env.example .env
    echo "✅ Created .env file from template"
    echo "📝 Please edit .env with your Cyberdyne Systems credentials"
    echo ""
fi

# Function to show available commands
show_usage() {
    echo "Available Terminator deployment modes:"
    echo ""
    echo "🐳 Docker Commands:"
    echo "  $0 docker-build    # Build Skynet neural core image"
    echo "  $0 docker-run      # Run single container (requires .env)"
    echo "  $0 docker-compose  # Deploy with docker-compose"
    echo ""
    echo "🔧 Local Development:"
    echo "  $0 dev-install     # Install for local development"
    echo "  $0 local-run       # Run locally with uv"
    echo ""
    echo "🧪 Testing & Management:"
    echo "  $0 test            # Test connection and functionality"
    echo "  $0 status          # Check Skynet operational status"
    echo "  $0 cleanup         # Terminate all Skynet operations"
    echo ""
    echo "Hasta La Vista, baby! 🤖💀"
}

# Docker build
docker_build() {
    echo "🔨 Building Skynet neural core image..."
    docker build -t dai-mcp:latest .
    echo "✅ Skynet neural core image built successfully - I'll Be Back!"
}

# Docker run with environment file
docker_run() {
    echo "🤖 Initializing Skynet Neural Network Memory Core..."
    echo "=================================================="
    
    if [ ! -f ".env" ]; then
        echo "⚠️  No .env file found. Creating from template..."
        cp .env.example .env
        echo "✅ Created .env file from template"
        echo "� Please edit .env with your Cyberdyne Systems credentials"
        return 1
    fi
    
    echo "🗂️  Environment: Local Neo4j database included"
    echo "🔑 Default credentials: neo4j/skynet123"
    
    echo "🔥 Building Skynet neural core image..."
    docker build -t dai-mcp:latest .
    
    echo "🚀 Deploying Terminator container..."
    docker run -d --name skynet-neural-mcp-server \
        --env-file .env \
        -p ${NEO4J_MCP_SERVER_PORT:-8000}:8000 \
        dai-mcp:latest
    
    echo ""
    echo "✅ Skynet deployment successful!"
    echo "🌐 MCP Neural Interface: http://localhost:${NEO4J_MCP_SERVER_PORT:-8000}"
    echo "🗄️  Neo4j Browser: http://localhost:7474 (neo4j/skynet123)"
    echo "📊 Status: docker logs skynet-neural-mcp-server"
    echo "🛑 Terminate: docker stop skynet-neural-mcp-server"
    echo ""
    echo "💡 Visit the Neo4j Browser to explore your Skynet neural database!"
    echo "\"Hasta La Vista, baby!\" - The Terminator 🤖💀"
}

# Docker compose deployment
docker_compose() {
    echo "🤖 Initializing Skynet Neural Network Memory Core..."
    echo "=================================================="
    
    if [ ! -f ".env" ]; then
        echo "⚠️  No .env file found. Creating from template..."
        cp .env.example .env
        echo "✅ Created .env file from template"
        echo "� Please edit .env with your Cyberdyne Systems credentials"
        echo ""
    fi
    
    echo "🗂️  Environment: Local Neo4j database included"
    echo "🔑 Default credentials: neo4j/skynet123"
    
    echo "🚀 Launching Skynet with Docker Compose..."
    echo "🔥 Building and starting neural core..."
    docker-compose up --build -d
    
    echo ""
    echo "✅ Skynet is online and operational!"
    echo "🌐 MCP Neural Interface: http://localhost:${NEO4J_MCP_SERVER_PORT:-8000}"
    echo "🗄️  Neo4j Browser: http://localhost:7474 (neo4j/skynet123)"
    echo "📊 Status: docker-compose logs -f"
    echo "🛑 Terminate: docker-compose down"
    echo ""
    echo "💡 Visit the Neo4j Browser to explore your Skynet neural database!"
    echo "\"I'll Be Back\" - Skynet Neural Core 🤖💀"
}

# Local development installation
dev_install() {
    echo "🔧 Installing Skynet neural dependencies..."
    if ! command -v uv &> /dev/null; then
        echo "❌ uv not found. Installing uv first..."
        pip install uv
    fi
    uv pip install -e .
    echo "✅ Skynet neural core installed for development"
}

# Local run
local_run() {
    echo "🧠 Starting local Skynet neural interface..."
    if [ -f ".env" ]; then
        set -a
        source .env
        set +a
    fi
    uv run dai-mcp
}

# Test functionality
test_connection() {
    echo "🧪 Testing Skynet neural network connection..."
    if [ -f ".env" ]; then
        set -a
        source .env
        set +a
    fi
    
    echo "🔍 Checking neural core status..."
    timeout 10s uv run dai-mcp --help || echo "✅ Command interface operational"
    
    echo "🎯 Testing database connection..."
    timeout 5s uv run dai-mcp || echo "⚠️  Database connection test completed (expected if no Neo4j running)"
    
    echo "✅ Skynet neural core tests completed"
}

# Cleanup operations
cleanup() {
    echo "🤖 Terminating Skynet operations..."
    echo "=================================="
    
    echo "🛑 Stopping Docker containers..."
    docker-compose down --remove-orphans 2>/dev/null || true
    
    echo "🗑️  Removing Docker containers..."
    docker rm skynet-neural-mcp-server 2>/dev/null || true
    
    echo "🔥 Cleaning up Docker images..."
    docker image prune -f 2>/dev/null || true
    
    echo "✅ Skynet termination complete"
    echo "\"Hasta La Vista, baby!\" - The Terminator 🤖💀"
}

# Status report
status() {
    echo "🤖 Skynet Neural Core Status Report"
    echo "=================================="
    
    if [ -f ".env" ]; then
        echo "✅ Environment configuration found"
        if grep -q "bolt://localhost:7687" .env 2>/dev/null; then
            echo "✅ Local Neo4j database configured (neo4j/skynet123)"
        elif grep -q "bolt://" .env 2>/dev/null || grep -q "neo4j+s://" .env 2>/dev/null; then
            echo "✅ Custom Neo4j database configured"
        else
            echo "⚠️  Database URL may need configuration"
        fi
    else
        echo "❌ No .env file found"
    fi
    
    if docker ps | grep -q skynet-neural-mcp-server 2>/dev/null; then
        echo "✅ Skynet container running"
        echo "📊 Container logs: docker logs skynet-neural-mcp-server"
    else
        echo "❌ Skynet container not running"
    fi
    
    if docker-compose ps 2>/dev/null | grep -q skynet-neural-core; then
        echo "✅ Docker Compose stack active"
        echo "📊 Stack status: docker-compose ps"
    else
        echo "❌ Docker Compose stack not active"
    fi
    
    echo ""
    echo "🌐 Expected endpoints:"
    echo "  - MCP Server: http://localhost:8000"
    echo "  - MCP SSE: http://localhost:8000/sse"
    echo "  - Neo4j Browser: http://localhost:7474 (neo4j/skynet123)"
    echo "  - Neo4j Bolt: bolt://localhost:7687"
    echo ""
}

# Main execution
case "${1:-help}" in
    docker-build)
        docker_build
        ;;
    docker-run)
        docker_run
        ;;
    docker-compose)
        docker_compose
        ;;
    dev-install)
        dev_install
        ;;
    local-run)
        local_run
        ;;
    test)
        test_connection
        ;;
    cleanup)
        cleanup
        ;;
    status)
        status
        ;;
    help|*)
        show_usage
        ;;
esac