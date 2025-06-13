import streamlit as st
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SerpAPIWrapper
import warnings

# Suppress LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# --- Set API keys directly in code (not secure for production) ---
GOOGLE_API_KEY = "AIzaSyCX3w_DD7PZD6I0zPsReks8XPkrJrylq1w"
SERPAPI_API_KEY = "2e4e2c92a24c82edadca5aa1fd068cc049909c3044721bb51997656c2849ae42"

# --- Validate API keys ---
if not GOOGLE_API_KEY or not SERPAPI_API_KEY:
    st.error("🚫 API keys missing.")
    st.stop()

# --- Initialize Gemini LLM ---
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

# --- Initialize SerpAPI Tool ---
search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)
search_tool = Tool(
    name="Google Search",
    func=search.run,
    description="Search the internet for recent hackathons and coding competitions"
)

# --- Initialize Memory ---
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# --- Initialize Agent ---
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# --- Streamlit UI ---
st.set_page_config(page_title="Hackathon Finder", layout="centered")
st.title("🔍 Hackathon Finder")
st.markdown("Ask me to find hackathons or coding competitions using web search + Gemini.")

# --- User Input ---
user_input = st.text_input("Enter your question (e.g., 'Find AI hackathons in India this month')")

# --- Run Agent ---
if st.button("Search"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a valid question.")
    else:
        with st.spinner("🔍 Searching the web..."):
            try:
                prompt = f"You are a helpful assistant. {user_input.strip()}"
                response = agent.run(prompt)
                st.success("✅ Here's what I found:")
                st.markdown(response)
            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")

# --- Optional: Display Chat History ---
with st.expander("🧠 Chat History"):
    for msg in memory.chat_memory.messages:
        role = "🧑‍💻 You" if msg.type == "human" else "🤖 Bot"
        st.markdown(f"**{role}:** {msg.content}")
