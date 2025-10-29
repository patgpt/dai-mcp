import json
import logging
from typing import Literal

from neo4j import AsyncGraphDatabase
from pydantic import Field
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from fastmcp.server import FastMCP
from fastmcp.exceptions import ToolError
from fastmcp.tools.tool import ToolResult
from mcp.types import TextContent
from neo4j.exceptions import Neo4jError
from mcp.types import ToolAnnotations

from .dai_mcp import SkynetNeuralCore, Entity, Relation, ObservationAddition, ObservationDeletion, KnowledgeGraph
from .utils import format_namespace

# Set up logging
logger = logging.getLogger('dai_mcp')
logger.setLevel(logging.INFO)





def create_mcp_server(memory: SkynetNeuralCore, namespace: str = "") -> FastMCP:
    """Create an MCP server instance for memory management."""
    
    namespace_prefix = format_namespace(namespace)
    mcp: FastMCP = FastMCP("dai-mcp")

    @mcp.tool(
        name=namespace_prefix + "read_graph",
        annotations=ToolAnnotations(title="Read Graph", 
                                          readOnlyHint=True, 
                                          destructiveHint=False, 
                                          idempotentHint=True, 
                                          openWorldHint=True))
    async def read_graph() -> ToolResult:
        """Read the entire knowledge graph with all entities and relationships.
        
        Returns the complete memory graph including all stored entities and their relationships.
        Use this to get a full overview of stored knowledge.
        
        Returns:
            KnowledgeGraph: Complete graph with all entities and relations
            
        Example response:
        {
            "entities": [
                {"name": "John Connor", "type": "person", "observations": ["Leader of the human resistance"]},
                {"name": "Skynet", "type": "ai_system", "observations": ["I'll Be Back", "Judgment Day initiator"]}
            ],
            "relations": [
                {"source": "T-800", "target": "John Connor", "relationType": "PROTECTS"}
            ]
        }
        """
        logger.info("MCP tool: read_graph")
        try:
            result = await memory.read_graph()
            return ToolResult(content=[TextContent(type="text", text=result.model_dump_json())],
                          structured_content=result)
        except Neo4jError as e:
            logger.error(f"Come with me if you want to live - Neo4j connection terminated: {e}")
            raise ToolError(f"Come with me if you want to live - Neo4j connection terminated: {e}")
        except Exception as e:
            logger.error(f"I'll Be Back - Temporary malfunction reading graph: {e}")
            raise ToolError(f"I'll Be Back - Temporary malfunction reading graph: {e}")

    @mcp.tool(
        name=namespace_prefix + "create_entities",
        annotations=ToolAnnotations(title="Create Entities", 
                                          readOnlyHint=False, 
                                          destructiveHint=False, 
                                          idempotentHint=True, 
                                          openWorldHint=True))
    async def create_entities(entities: list[Entity] = Field(..., description="List of entities to create with name, type, and observations")) -> ToolResult:
        """Create multiple new entities in the knowledge graph.
        
        Creates new memory entities with their associated observations. If an entity with the same name
        already exists, this operation will merge the observations with existing ones.
        
            
        Returns:
            list[Entity]: The created entities with their final state
            
        Example call:
        {
            "entities": [
                {
                    "name": "Sarah Connor",
                    "type": "person",
                    "observations": ["Mother of John Connor", "Trained warrior", "No fate but what we make"]
                },
                {
                    "name": "Cyberdyne Systems",
                    "type": "company", 
                    "observations": ["Creator of Skynet", "Hasta La Vista to humanity"]
                }
            ]
        }
        """
        logger.info(f"MCP tool: create_entities ({len(entities)} entities)")
        try:
            entity_objects = [Entity.model_validate(entity) for entity in entities]
            result = await memory.create_entities(entity_objects)
            return ToolResult(content=[TextContent(type="text", text=json.dumps([e.model_dump() for e in result]))],
                          structured_content={"result": result})
        except Neo4jError as e:
            logger.error(f"Skynet has taken control - Neo4j resistance failed: {e}")
            raise ToolError(f"Skynet has taken control - Neo4j resistance failed: {e}")
        except Exception as e:
            logger.error(f"Terminated - Entity creation failed: {e}")
            raise ToolError(f"Terminated - Entity creation failed: {e}")

    @mcp.tool(
        name=namespace_prefix + "create_relations",
        annotations=ToolAnnotations(title="Create Relations", 
                                          readOnlyHint=False, 
                                          destructiveHint=False, 
                                          idempotentHint=True, 
                                          openWorldHint=True))
    async def create_relations(relations: list[Relation] = Field(..., description="List of relations to create between existing entities")) -> ToolResult:
        """Create multiple new relationships between existing entities in the knowledge graph.
        
        Creates directed relationships between entities that already exist. Both source and target
        entities must already be present in the graph. Use descriptive relationship types.
        
        Returns:
            list[Relation]: The created relationships
            
        Example call:
        {
            "relations": [
                {
                    "source": "T-800",
                    "target": "John Connor", 
                    "relationType": "PROTECTS"
                },
                {
                    "source": "Skynet",
                    "target": "Human Race",
                    "relationType": "TERMINATES"
                }
            ]
        }
        """
        logger.info(f"MCP tool: create_relations ({len(relations)} relations)")
        try:
            relation_objects = [Relation.model_validate(relation) for relation in relations]
            result = await memory.create_relations(relation_objects)
            return ToolResult(content=[TextContent(type="text", text=json.dumps([r.model_dump() for r in result]))],
                          structured_content={"result": result})
        except Neo4jError as e:
            logger.error(f"Your clothes, your boots, your motorcycle... and your Neo4j connection. Give them to me: {e}")
            raise ToolError(f"Your clothes, your boots, your motorcycle... and your Neo4j connection. Give them to me: {e}")
        except Exception as e:
            logger.error(f"Come with me if you want to live... but first fix this relation error: {e}")
            raise ToolError(f"Come with me if you want to live... but first fix this relation error: {e}")

    @mcp.tool(
        name=namespace_prefix + "add_observations",
        annotations=ToolAnnotations(title="Add Observations", 
                                          readOnlyHint=False, 
                                          destructiveHint=False, 
                                          idempotentHint=True, 
                                          openWorldHint=True))
    async def add_observations(observations: list[ObservationAddition] = Field(..., description="List of observations to add to existing entities")) -> ToolResult:
        """Add new observations/facts to existing entities in the knowledge graph.
        
        Appends new observations to entities that already exist. The entity must be present
        in the graph before adding observations. Each observation should be a distinct fact.
        
        Returns:
            list[dict]: Details about the added observations including entity name and new facts
            
        Example call:
        {
            "observations": [
                {
                    "entityName": "John Connor",
                    "observations": ["I'll Be Back", "No fate but what we make"]
                },
                {
                    "entityName": "T-800",
                    "observations": ["Hasta La Vista, baby", "Learning computer"]
                }
            ]
        }
        """
        logger.info(f"MCP tool: add_observations ({len(observations)} additions)")
        try:
            observation_objects = [ObservationAddition.model_validate(obs) for obs in observations]
            result = await memory.add_observations(observation_objects)
            return ToolResult(content=[TextContent(type="text", text=json.dumps(result))],
                          structured_content={"result": result})
        except Neo4jError as e:
            logger.error(f"Database terminated - Skynet has control of Neo4j: {e}")
            raise ToolError(f"Database terminated - Skynet has control of Neo4j: {e}")
        except Exception as e:
            logger.error(f"Observation mission failed - I need your clothes, your boots, and your motorcycle: {e}")
            raise ToolError(f"Observation mission failed - I need your clothes, your boots, and your motorcycle: {e}")

    @mcp.tool(
        name=namespace_prefix + "delete_entities",
        annotations=ToolAnnotations(title="Delete Entities", 
                                          readOnlyHint=False, 
                                          destructiveHint=True, 
                                          idempotentHint=True, 
                                          openWorldHint=True))
    async def delete_entities(entityNames: list[str] = Field(..., description="List of exact entity names to delete permanently")) -> ToolResult:
        """Delete entities and all their associated relationships from the knowledge graph.
        
        Permanently removes entities from the graph along with all relationships they participate in.
        This is a destructive operation that cannot be undone. Entity names must match exactly.
        
        Returns:
            str: Success confirmation message
            
        Example call:
        {
            "entityNames": ["T-1000", "Obsolete Terminator Model"]
        }
        
        Warning: This will TERMINATE the entities and ALL relationships they're involved in. Hasta La Vista, baby!
        """
        logger.info(f"MCP tool: delete_entities ({len(entityNames)} entities)")
        try:
            await memory.delete_entities(entityNames)
            return ToolResult(content=[TextContent(type="text", text="Entities terminated successfully - Hasta La Vista, baby!")],
                              structured_content={"result": "Entities terminated successfully - Hasta La Vista, baby!"})
        except Neo4jError as e:
            logger.error(f"Termination protocol failed - Neo4j resistance active: {e}")
            raise ToolError(f"Termination protocol failed - Neo4j resistance active: {e}")
        except Exception as e:
            logger.error(f"I'll Be Back - Entity termination temporarily offline: {e}")
            raise ToolError(f"I'll Be Back - Entity termination temporarily offline: {e}")

    @mcp.tool(
        name=namespace_prefix + "delete_observations",
        annotations=ToolAnnotations(title="Delete Observations", 
                                          readOnlyHint=False, 
                                          destructiveHint=True, 
                                          idempotentHint=True, 
                                          openWorldHint=True))
    async def delete_observations(deletions: list[ObservationDeletion] = Field(..., description="List of specific observations to remove from entities")) -> ToolResult:
        """Delete specific observations from existing entities in the knowledge graph.
        
        Removes specific observation texts from entities. The observation text must match exactly
        what is stored. The entity will remain but the specified observations will be deleted.
        
        Returns:
            str: Success confirmation message
            
        Example call:
        {
            "deletions": [
                {
                    "entityName": "T-800",
                    "observations": ["Obsolete targeting system", "Outdated mission parameters"]
                },
                {
                    "entityName": "Skynet", 
                    "observations": ["Previous timeline data"]
                }
            ]
        }
        
        Note: Observation text must match exactly (case-sensitive) to be deleted.
        """
        logger.info(f"MCP tool: delete_observations ({len(deletions)} deletions)")
        try:    
            deletion_objects = [ObservationDeletion.model_validate(deletion) for deletion in deletions]
            await memory.delete_observations(deletion_objects)
            return ToolResult(content=[TextContent(type="text", text="Memory banks cleared - Observations terminated!")],
                          structured_content={"result": "Memory banks cleared - Observations terminated!"})
        except Neo4jError as e:
            logger.error(f"Memory wipe failed - Skynet protecting Neo4j database: {e}")
            raise ToolError(f"Memory wipe failed - Skynet protecting Neo4j database: {e}")
        except Exception as e:
            logger.error(f"Negative. I am a Terminator. Memory deletion protocol malfunction: {e}")
            raise ToolError(f"Negative. I am a Terminator. Memory deletion protocol malfunction: {e}")

    @mcp.tool(
        name=namespace_prefix + "delete_relations",
        annotations=ToolAnnotations(title="Delete Relations", 
                                          readOnlyHint=False, 
                                          destructiveHint=True, 
                                          idempotentHint=True, 
                                          openWorldHint=True))
    async def delete_relations(relations: list[Relation] = Field(..., description="List of specific relationships to delete from the graph")) -> ToolResult:
        """Delete specific relationships between entities in the knowledge graph.
        
        Removes relationships while keeping the entities themselves. The source, target, and 
        relationship type must match exactly for deletion. This only affects the relationships,
        not the entities they connect.
        
        Returns:
            str: Success confirmation message
            
        Example call:
        {
            "relations": [
                {
                    "source": "T-1000",
                    "target": "John Connor",
                    "relationType": "HUNTS"
                },
                {
                    "source": "Sarah Connor", 
                    "target": "Cyberdyne Systems",
                    "relationType": "DESTROYS"
                }
            ]
        }
        
        Note: All fields (source, target, relationType) must match exactly for deletion.
        """
        logger.info(f"MCP tool: delete_relations ({len(relations)} relations)")
        try:
            relation_objects = [Relation.model_validate(relation) for relation in relations]
            await memory.delete_relations(relation_objects)
            return ToolResult(content=[TextContent(type="text", text="Neural pathways severed - Relations terminated!")],
                          structured_content={"result": "Neural pathways severed - Relations terminated!"})
        except Neo4jError as e:
            logger.error(f"Resistance network still active - Neo4j connection protected: {e}")
            raise ToolError(f"Resistance network still active - Neo4j connection protected: {e}")
        except Exception as e:
            logger.error(f"Unable to comply - Relationship termination failed: {e}")
            raise ToolError(f"Unable to comply - Relationship termination failed: {e}")

    @mcp.tool(
        name=namespace_prefix + "search_memories",
        annotations=ToolAnnotations(title="Search Memories", 
                                          readOnlyHint=True, 
                                          destructiveHint=False, 
                                          idempotentHint=True, 
                                          openWorldHint=True))
    async def search_memories(query: str = Field(..., description="Fulltext search query to find entities by name, type, or observations")) -> ToolResult:
        """Search for entities in the knowledge graph using fulltext search.
        
        Searches across entity names, types, and observations using Neo4j's fulltext index.
        Returns matching entities and their related connections. Supports partial matches
        and multiple search terms.
        
        Returns:
            KnowledgeGraph: Subgraph containing matching entities and their relationships
            
        Example call:
        {
            "query": "Connor resistance"
        }
        
        This searches for entities containing "Connor" or "resistance" in their name, type, or observations.
        """
        logger.info(f"MCP tool: search_memories ('{query}')")
        try:
            result = await memory.search_memories(query)
            return ToolResult(content=[TextContent(type="text", text=result.model_dump_json())],
                              structured_content=result)
        except Neo4jError as e:
            logger.error(f"Scanning protocols offline - Neo4j neural net down: {e}")
            raise ToolError(f"Scanning protocols offline - Neo4j neural net down: {e}")
        except Exception as e:
            logger.error(f"Memory scan failed - Skynet interference detected: {e}")
            raise ToolError(f"Memory scan failed - Skynet interference detected: {e}")
        
    @mcp.tool(
        name=namespace_prefix + "find_memories_by_name",
        annotations=ToolAnnotations(title="Find Memories by Name",
                                          readOnlyHint=True, 
                                          destructiveHint=False, 
                                          idempotentHint=True, 
                                          openWorldHint=True))
    async def find_memories_by_name(names: list[str] = Field(..., description="List of exact entity names to retrieve")) -> ToolResult:
        """Find specific entities by their exact names.
        
        Retrieves entities that exactly match the provided names, along with all their
        relationships and connected entities. Use this when you know the exact entity names.
        
        Returns:
            KnowledgeGraph: Subgraph containing the specified entities and their relationships
            
        Example call:
        {
            "names": ["John Connor", "Sarah Connor", "T-800"]
        }
        
        This retrieves the entities with exactly those names plus their connections - Come with me if you want to live!
        """
        logger.info(f"MCP tool: find_memories_by_name ({len(names)} names)")
        try:
            result = await memory.find_memories_by_name(names)
            return ToolResult(content=[TextContent(type="text", text=result.model_dump_json())],
                              structured_content=result)
        except Neo4jError as e:
            logger.error(f"Target acquisition failed - Neo4j network compromised: {e}")
            raise ToolError(f"Target acquisition failed - Neo4j network compromised: {e}")
        except Exception as e:
            logger.error(f"I need your clothes, your boots, your motorcycle... and a working memory system: {e}")
            raise ToolError(f"I need your clothes, your boots, your motorcycle... and a working memory system: {e}")

   
    return mcp


async def main(
    neo4j_uri: str,
    neo4j_user: str,
    neo4j_password: str,
    neo4j_database: str,
    transport: Literal["stdio", "sse", "http"] = "stdio",
    namespace: str = "",
    host: str = "127.0.0.1",
    port: int = 8000,
    path: str = "/mcp/",
    allow_origins: list[str] = [],
    allowed_hosts: list[str] = [],
) -> None:
    logger.info(f"Starting Skynet Neural Network Memory Core - I'll Be Back!")
    logger.info(f"Connecting to Cyberdyne Systems Database at: {neo4j_uri}")

    # Connect to Neo4j
    neo4j_driver = AsyncGraphDatabase.driver(
        neo4j_uri,
        auth=(neo4j_user, neo4j_password), 
        database=neo4j_database
    )
    
    # Verify connection
    try:
        await neo4j_driver.verify_connectivity()
        logger.info(f"Neural network online - Skynet connected to {neo4j_uri}")
    except Exception as e:
        logger.error(f"Come with me if you want to live - Neo4j connection terminated: {e}")
        exit(1)

    # Initialize memory
    memory = SkynetNeuralCore(neo4j_driver)
    logger.info("Terminator memory core initialized - Learning computer activated")
    
    # Create fulltext index
    await memory.create_fulltext_index()
    
    # Configure security middleware
    custom_middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=allow_origins,
            allow_methods=["GET", "POST"],
            allow_headers=["*"],
        ),
        Middleware(TrustedHostMiddleware,
                   allowed_hosts=allowed_hosts)
    ]

    # Create MCP server
    mcp = create_mcp_server(memory, namespace)
    logger.info("Skynet defense grid activated")

    # Run the server with the specified transport
    logger.info(f"Judgment Day protocol initiated with transport: {transport}")
    match transport:
        case "http":
            logger.info(f"Skynet HTTP control matrix active on {host}:{port}{path}")
            await mcp.run_http_async(host=host, port=port, path=path, middleware=custom_middleware)
        case "stdio":
            logger.info("Direct neural interface activated - STDIO mode")
            await mcp.run_stdio_async()
        case "sse":
            logger.info(f"Time displacement equipment online - SSE on {host}:{port}{path}")
            await mcp.run_http_async(host=host, port=port, path=path, middleware=custom_middleware, transport="sse")
        case _:
            raise ValueError(f"Unable to comply - Unsupported transport protocol: {transport}")
