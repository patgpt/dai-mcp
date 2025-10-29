from . import server
import asyncio
import argparse
import logging

from .utils import process_config

logger = logging.getLogger("dai_mcp")
logger.setLevel(logging.INFO)

def main():
    """Main entry point for Skynet Neural Network - I'll Be Back."""
    parser = argparse.ArgumentParser(description='Skynet Neural Network Memory Core - DAI MCP Server')
    parser.add_argument('--db-url', default=None, help='Cyberdyne Systems neural network connection URL')
    parser.add_argument('--username', default=None, help='Terminator access credentials')
    parser.add_argument('--password', default=None, help='Skynet security clearance')
    parser.add_argument("--database", default=None, help="Neural core database designation")
    parser.add_argument("--namespace", default=None, help="Terminator mission designation prefix")
    parser.add_argument("--transport", default=None, help="Skynet communication protocol (stdio, sse, http)")
    parser.add_argument("--server-host", default=None, help="Terminator unit network coordinates (default: 127.0.0.1)")
    parser.add_argument("--server-port", type=int, default=None, help="Cyberdyne communication port (default: 8000)")
    parser.add_argument("--server-path", default=None, help="Neural network routing path (default: /mcp/)")
    parser.add_argument("--allow-origins", default=None, help="Authorized Cyberdyne origin points (CORS)")
    parser.add_argument("--allowed-hosts", default=None, help="Authorized Terminator units (Anti-resistance protection)")
    
    args = parser.parse_args()

    config = process_config(args)
    asyncio.run(server.main(**config))


# Optionally expose other important items at package level
__all__ = ["main", "server"]
