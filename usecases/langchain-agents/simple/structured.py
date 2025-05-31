from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama


tagging_prompt = ChatPromptTemplate.from_template(
    """
Extract the desired information from the following passage.

Only extract the properties mentioned in the 'Classification' function.

Passage:
{input}
"""
)


class Classification(BaseModel):
    sentiment: str = Field(description="The sentiment of the text")
    aggressiveness: int = Field(
        description="How aggressive the text is on a scale from 1 to 10"
    )
    language: str = Field(description="The language the text is written in")


# Structured LLM
llm = ChatOllama(
    model="qwen3:latest",
    base_url="http://localhost:11434"
)
structured_llm = llm.with_structured_output(Classification)


# inp = "Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!"
inp = "Mẹ cha chúng mày, Tao không thể chấp nhận được. Chúng mày làm ăn thế đỏ hả. Làm sao làm, phải trả tiền lại cho tao"
# inp = "I'm angry. fuck off"
prompt = tagging_prompt.invoke({"input": inp})
response = structured_llm.invoke(prompt)

print(response)
