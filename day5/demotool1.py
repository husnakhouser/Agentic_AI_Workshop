import streamlit as st
import os
import warnings
from dotenv import load_dotenv

from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SerpAPIWrapper

# Optional: Suppress LangChain warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Load environment variables from local .env file (optional on Streamlit Cloud)
load_dotenv()

# Read keys from Streamlit secrets (for deployment) or fallback to .env
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"] if "GOOGLE_API_KEY" in st.secrets else os.getenv("GOOGLE_API_KEY")
SERPAPI_API_KEY = st.secrets["SERPAPI_API_KEY"] if "SERPAPI_API_KEY" in st.secrets else os.getenv("SERPAPI_API_KEY")

# Validate API keys
if not GOOGLE_API_KEY or not SERPAPI_API_KEY:
    st.error("🚫 API keys missing. Please check your `.env` file or Streamlit secrets.")
    st.stop()

# Set environment variables for tools to access
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["SERPAPI_API_KEY"] = SERPAPI_API_KEY

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

# Set up SerpAPI Search Tool
search = SerpAPIWrapper()
search_tool = Tool(
    name="Google Search",
    func=search.run,
    description="Search the internet for recent hackathons and coding competitions"
)

# Set up memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize LangChain agent
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# Streamlit UI setup
st.set_page_config(page_title="Hackathon Finder", layout="centered")
st.title("🔍 Hackathon Finder")
st.markdown("Ask me to find hackathons or coding competitions using web search + Gemini.")

# User input
user_input = st.text_input("Enter your query (e.g., 'Find AI hackathons in India this month')")

# Run agent on button click
if st.button("Search"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a question.")
    else:
        with st.spinner("Searching..."):
            try:
                result = agent.run(user_input)
                st.success("✅ Here's what I found:")
                st.markdown(result)
            except Exception as e:
                st.error(f"❌ Error: {e}")

# Show conversation history (optional)
with st.expander("🧠 Chat History"):
    for msg in memory.chat_memory.messages:
        role = "👤 You" if msg.type == "human" else "🤖 Gemini"
        st.markdown(f"**{role}:** {msg.content}")


