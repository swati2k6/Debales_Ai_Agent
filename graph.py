from langgraph.graph import StateGraph
from rag import load_retriever
from tools import search_serp
from router import route_query
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key="your_api_key"
)

retriever = load_retriever()


# ✅ Router
def router_node(state):
    query = state["query"]
    route = route_query(query)
    return {"query": query, "route": route}


# ✅ RAG
def rag_node(state):
    query = state["query"]
    docs = retriever.get_relevant_documents(query)

    context = "\n".join([d.page_content for d in docs])
    return {"query": query, "context": context}


# ✅ SERP
def serp_node(state):
    query = state["query"]
    context = search_serp(query)

    return {"query": query, "context": context}


# ✅ FINAL
def final_node(state):
    query = state["query"]
    context = state.get("context", "")

    prompt = f"""
Answer the question using the context.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return {
        "query": query,
        "answer": response.content
    }


def build_graph():
    graph = StateGraph(dict)

    graph.add_node("router", router_node)
    graph.add_node("rag", rag_node)
    graph.add_node("serp", serp_node)
    graph.add_node("final", final_node)

    graph.set_entry_point("router")

    graph.add_conditional_edges(
        "router",
        lambda x: x["route"],
        {
            "rag": "rag",
            "serp": "serp"
        }
    )

    graph.add_edge("rag", "final")
    graph.add_edge("serp", "final")

    return graph.compile()