import asyncio
import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from google.adk.models.lite_llm import LiteLlm

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

async def get_tools_async():
    """Connects to the mcp-reddit server via uvx and returns the tools and exit stack."""
    print("--- Attempting to start and connect to mcp-reddit MCP server via uvx ---")
    try:
        # Check if uvx is available (basic check)
        # A more robust check might involve checking the actual command's success
        await asyncio.create_subprocess_shell('uvx --version', stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

        tools, exit_stack = await MCPToolset.from_server(
            connection_params=StdioServerParameters(
                command='uvx',
                args=['--from', 'git+https://github.com/manusa/kubernetes-mcp-server.git', "-y",
        "kubernetes-mcp-server@latest"],
                # Optional: Add environment variables if needed by the MCP server,
                # e.g., credentials if mcp-reddit required them.
                # env=os.environ.copy()
            )
        )
        print(f"--- Successfully connected to k8s server Discovered {len(tools)} tool(s). ---")
        # Print discovered tool names for debugging/instruction refinement
        for tool in tools:
            print(f"  - Discovered tool: {tool.name}") # Tool name is likely 'fetch_reddit_hot_threads' or similar
        return tools, exit_stack
    except FileNotFoundError:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!! ERROR: 'uvx' command not found. Please install uvx: pip install uvx !!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # Return empty tools and a no-op exit stack to prevent agent failure
        class DummyExitStack:
            async def __aenter__(self): return self
            async def __aexit__(self, *args): pass
        return [], DummyExitStack()
    except Exception as e:
        print(f"--- ERROR connecting to or starting mcp-reddit server: {e} ---")
        # Return empty tools and a no-op exit stack
        class DummyExitStack:
            async def __aenter__(self): return self
            async def __aexit__(self, *args): pass
        return [], DummyExitStack()
# Define LLM for wrapping the tool output if needed


async def create_agent():
    tools, exit_stack = await get_tools_async()
    if not tools:
        print("no tools")

    agent_instance = Agent(
        name= "kubernetes_MCP",
        description= "Kuberntes MCP Agent",
        model= 'gemini-2.0-flash',
        instruction=" You are a Kubernetes Engineer with CKA, CKAD,CKS and all other certifications from Linux Foundation ",
        tools=tools,

    )
    return agent_instance(), exit_stack

root_agent= create_agent()

