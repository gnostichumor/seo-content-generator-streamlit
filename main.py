import os
from dotenv import load_dotenv
import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI

load_dotenv()

# Load API key from .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

template = """
Write a 100 percent unique, creative, and human-like style article of a minimum of 1500 words using # headings # and # sub-headings #. 
For the "#Keyword Or Title”. Try to use contractions, idioms, transitional phrases, interjections, dangling modifiers, 
and colloquialisms, and avoid repetitive phrases and unnatural sentence structures. 
The article should include Creative Title, SEO meta-description, ## Introduction ##. Add bullet points or Numbered list if needed, 
Write down faqs and conclusion. 
Make sure the article is plagiarism free. Don't forget to use a question mark at the end of questions. 
Try not to change the original #Keyword Or Title while writing the Title. Try to use The "#Keyword Or Title " 2-3 times in the article. try to include #Keyword Or Title in headings as well. 
write content that can easily pass the ai detection tools test.

#Keyword Or Title: {keyword}
"""

# Create a new prompt template
prompt = PromptTemplate(input_variables=["keyword"],template=template)

with st.sidebar:
    st.markdown("## Input Variables")
    temp = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.001)

    st.markdown("## Model:")
    model = st.selectbox("Select Model", ["gpt-3.5-turbo", "gpt-4", "text-davinci-003"])

st.markdown("# SEO Content Generator")

def get_text():
    input_text = st.text_input("Keyword", value="")

def generate_article():
    llm = OpenAI(model_name=model, temperature=temp)
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    response = llm_chain.run(keyword=keyword, max_tokens=500)
    return response


form = st.form(key='Generate Article')
keyword = form.text_input("Keyword", value="")
submit = form.form_submit_button(label="Generate Article")

st.markdown("## Generated Article")
if submit:
    article = generate_article()
    st.write(article)


