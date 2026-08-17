#import pkg
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

#load dotenv
load_dotenv()

#form model
model=ChatGoogleGenerativeAI(model='gemini-3.5-flash')
#form prompt
prompt1=PromptTemplate(
    template='Write a Detailed Report on {topic}',
    input_variables=['topic']
)
#form prompt2
prompt2=PromptTemplate(
    template='Extract 5 Main Key Points from {ans}',
    input_variables=['ans']
)
#form parser
parser=StrOutputParser()
#form chain
chain =prompt1 | model | parser | prompt2 | model | parser
#print Result
result = chain.invoke({'topic':'psychology'})
print(result)

chain.get_graph().print_ascii()
