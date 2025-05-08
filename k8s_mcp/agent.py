import asyncio
import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

async def get_tools_async():
        tools, exit_stack = await MCPToolset.from_server(
            connection_params=StdioServerParameters(
                command='npx',
                args=["mcp-server-kubernetes"],
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
    return agent_instance, exit_stack

root_agent= create_agent()
