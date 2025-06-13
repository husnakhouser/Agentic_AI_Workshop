import streamlit as st
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SerpAPIWrapper
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set environment variables (you can remove these if using only .env)
os.environ["GOOGLE_API_KEY"] = "AIzaSyDRITZtXU3ZdZIz7XQC_38rijpG4lI3U84"
os.environ["SERPAPI_API_KEY"] = "1cf48d4c57a64dae23c97fbc19557af0ac1475b3c1a820c9a7d2a94b30c1ab51"

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

# Define search tool using SerpAPI
search = SerpAPIWrapper()
search_tool = Tool(
    name="Google Search",
    func=search.run,
    description="Search the internet for recent hackathons and coding competitions"
)

# Initialize memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize agent
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# Streamlit UI
st.set_page_config(page_title="Hackathon Finder", layout="centered")
st.title("🔍 Hackathon Finder")
st.markdown("Ask me to find hackathons or coding competitions using web search + Gemini.")

# User Input
user_input = st.text_input("Enter your question (e.g., 'Find AI hackathons in India this month')")

# Submit button
if st.button("Search"):
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching the web..."):
            try:
                response = agent.run(user_input)
                st.success("Here’s what I found:")
                st.markdown(response)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
