from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain import HuggingFaceHub, PromptTemplate, LLMChain
from dotenv import load_dotenv
from langchain.tools import DuckDuckGoSearchRun
import warnings
import os

# Suppress all warnings
warnings.filterwarnings("ignore")

# Load environment variables
load_dotenv()
huggingfacehub_api_token = os.getenv("API_TOKEN")

# Create the LLM object and configure it
repo_id = "tiiuae/falcon-7b-instruct"
llm = HuggingFaceHub(huggingfacehub_api_token=huggingfacehub_api_token,
                     repo_id=repo_id,
                     model_kwargs={"temperature": 0.1, "max_new_tokens": 500})

# Load the necessary tools
tools = load_tools(["llm-math"], llm=llm)
search = DuckDuckGoSearchRun()
result = str(search.run("Who is Leo DiCaprio's year old?", lang="en"))

# Initialize the agent
agent = initialize_agent(tools, llm,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=True)
print(f"Resultado de busquedas: {result} \n-------------------------")
# Run the agent with a prompt string
agent.run(f"Qué haces? calculame 4 + 5 dame el resultado. Responde siempre en Español.")
