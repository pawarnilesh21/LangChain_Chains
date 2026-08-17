from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-3.6-flash")

prompt=PromptTemplate(
    template='Generate 5 Interesting fact About {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()

prompt1=prompt.invoke({'topic':'Psychology'})
response=model.invoke(prompt1)
result=parser.invoke(response)

print(result)
