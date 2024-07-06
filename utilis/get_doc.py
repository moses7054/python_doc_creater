from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage



# Sending to llm
def gettingdoc(srtcontent, prompt): 
    
    load_dotenv()
    model = ChatOpenAI(model="gpt-4o")

    messages = [
        SystemMessage(content= prompt),
        HumanMessage(content= srtcontent),
    ]

    doc_md = model.invoke(messages)
    print("Succesful in getting documentation!")
    return doc_md.content
    