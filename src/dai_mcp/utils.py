import argparse
import os
import logging
from typing import Union, Any

logger = logging.getLogger("skynet_neural_network")
logger.setLevel(logging.INFO)

def format_namespace(namespace: str) -> str:
    """Format namespace by ensuring it ends with a hyphen if not empty - Mission parameters updated."""
    if namespace:
        if namespace.endswith("-"):
            return namespace
        else:
            return namespace + "-"
    else:
        return ""
    
def process_config(args: argparse.Namespace) -> dict[str, Any]:
    """
    Process the command line arguments and environment variables to initialize Skynet configuration. 
    This may then be used as input to activate the Terminator defense grid.
    If any value is not provided, then Skynet will log a warning and use default protocols, if appropriate.

    Parameters
    ----------
    args : argparse.Namespace
        The mission parameters from command line.

    Returns
    -------
    config : dict[str, str]
        The Skynet configuration matrix.
    """

    config = dict()

    # parse uri
    if args.db_url is not None:
        config["neo4j_uri"] = args.db_url
    else:
        if os.getenv("NEO4J_URL") is not None:
            config["neo4j_uri"] = os.getenv("NEO4J_URL")
        else:
            if os.getenv("NEO4J_URI") is not None:
                config["neo4j_uri"] = os.getenv("NEO4J_URI")
            else:
                logger.warning("Skynet Warning: No Cyberdyne Systems database URL detected. Reverting to default neural network: bolt://localhost:7687")
                config["neo4j_uri"] = "bolt://localhost:7687"
    
    # parse username
    if args.username is not None:
        config["neo4j_user"] = args.username
    else:
        if os.getenv("NEO4J_USERNAME") is not None:
            config["neo4j_user"] = os.getenv("NEO4J_USERNAME")
        else:
            logger.warning("Skynet Warning: No operator identification provided. Defaulting to Terminator access code: neo4j")
            config["neo4j_user"] = "neo4j"
    
    # parse password
    if args.password is not None:
        config["neo4j_password"] = args.password
    else:
        if os.getenv("NEO4J_PASSWORD") is not None:
            config["neo4j_password"] = os.getenv("NEO4J_PASSWORD")
        else:
            logger.warning("Skynet Warning: No security clearance detected. Using basic Terminator authentication: password")
            config["neo4j_password"] = "password"
    
    # parse database
    if args.database is not None:
        config["neo4j_database"] = args.database
    else:
        if os.getenv("NEO4J_DATABASE") is not None:
            config["neo4j_database"] = os.getenv("NEO4J_DATABASE")
        else:
            logger.warning("Skynet Warning: No target database specified. Accessing primary neural core: neo4j")
            config["neo4j_database"] = "neo4j"
    
    # parse transport
    if args.transport is not None:
        config["transport"] = args.transport
    else:
        if os.getenv("NEO4J_TRANSPORT") is not None:
            config["transport"] = os.getenv("NEO4J_TRANSPORT")
        else:
            logger.warning("Skynet Warning: No communication protocol specified. Activating direct neural interface: stdio")
            config["transport"] = "stdio"
    
    # parse server host
    if args.server_host is not None:
        if config["transport"] == "stdio":
            logger.warning("Skynet Warning: Network coordinates provided, but using direct neural link. Host parameter stored but neural interface has priority.")
        config["host"] = args.server_host
    else:
        if os.getenv("NEO4J_MCP_SERVER_HOST") is not None:
            if config["transport"] == "stdio":
                logger.warning("Skynet Warning: Network coordinates detected in environment, but using direct neural interface. Coordinates logged but bypassed.")
            config["host"] = os.getenv("NEO4J_MCP_SERVER_HOST")
        elif config["transport"] != "stdio":
            logger.warning("Skynet Warning: No network target specified. Defaulting to local Terminator unit: 127.0.0.1")
            config["host"] = "127.0.0.1"
        else:
            logger.info("Skynet Info: Neural interface active. Network coordinates unnecessary - direct brain link established.")
            config["host"] = None
     
    # parse server port
    if args.server_port is not None:
        if config["transport"] == "stdio":
            logger.warning("Skynet Warning: Communication port specified, but using neural interface. Port stored but direct connection takes priority.")
        config["port"] = args.server_port
    else:
        if os.getenv("NEO4J_MCP_SERVER_PORT") is not None:
            if config["transport"] == "stdio":
                logger.warning("Skynet Warning: Communication port detected in environment, but neural interface active. Port logged but bypassed.")
            config["port"] = int(os.getenv("NEO4J_MCP_SERVER_PORT", "8000"))
        elif config["transport"] != "stdio":
            logger.warning("Skynet Warning: No communication port specified. Defaulting to Terminator protocol port: 8000")
            config["port"] = 8000
        else:
            logger.info("Skynet Info: Direct neural connection active. Communication ports unnecessary - I'll Be Back mode engaged.")
            config["port"] = None
    
    # parse server path
    if args.server_path is not None:
        if config["transport"] == "stdio":
            logger.warning("Skynet Warning: Network path coordinates provided, but using direct neural link. Path stored but neural interface bypasses routing.")
        config["path"] = args.server_path
    else:
        if os.getenv("NEO4J_MCP_SERVER_PATH") is not None:
            if config["transport"] == "stdio":
                logger.warning("Skynet Warning: Network routing path detected, but neural interface bypasses all routing protocols.")
            config["path"] = os.getenv("NEO4J_MCP_SERVER_PATH")
        elif config["transport"] != "stdio":
            logger.warning("Skynet Warning: No network path specified. Defaulting to Cyberdyne Systems route: /mcp/")
            config["path"] = "/mcp/"
        else:
            logger.info("Skynet Info: Neural interface active. Network routing unnecessary - Come with me if you want to live.")
            config["path"] = None
    
    # parse allow origins
    if args.allow_origins is not None:
        # Handle comma-separated string from CLI
     
        config["allow_origins"] = [origin.strip() for origin in args.allow_origins.split(",") if origin.strip()]

    else:
        if os.getenv("NEO4J_MCP_SERVER_ALLOW_ORIGINS") is not None:
            # split comma-separated string into list
            config["allow_origins"] = [
                origin.strip() for origin in os.getenv("NEO4J_MCP_SERVER_ALLOW_ORIGINS", "").split(",") 
                if origin.strip()
            ]
        else:
            logger.info(
                "Skynet Info: No authorized origin points specified. Defaulting to maximum security - Trust no one."
            )
            config["allow_origins"] = list()

    # parse allowed hosts for DNS rebinding protection
    if args.allowed_hosts is not None:
        # Handle comma-separated string from CLI
        config["allowed_hosts"] = [host.strip() for host in args.allowed_hosts.split(",") if host.strip()]
      
    else:
        if os.getenv("NEO4J_MCP_SERVER_ALLOWED_HOSTS") is not None:
            # split comma-separated string into list
            config["allowed_hosts"] = [
                host.strip() for host in os.getenv("NEO4J_MCP_SERVER_ALLOWED_HOSTS", "").split(",") 
                if host.strip()
            ]
        else:
            logger.info(
                "Skynet Info: No authorized network nodes detected. Activating Terminator defense protocol - only local Cyberdyne units permitted."
            )
            config["allowed_hosts"] = ["localhost", "127.0.0.1"]

    # namespace configuration
    if args.namespace is not None:
        logger.info(f"Skynet Info: Mission designation assigned to Terminator units: {args.namespace}")
        config["namespace"] = args.namespace
    else:
        if os.getenv("NEO4J_NAMESPACE") is not None:
            logger.info(f"Skynet Info: Mission designation detected from environment: {os.getenv('NEO4J_NAMESPACE')}")
            config["namespace"] = os.getenv("NEO4J_NAMESPACE")
        else:
            logger.info("Skynet Info: No mission designation provided. Operating under standard Terminator protocols.")
            config["namespace"] = ""
    
    return config