import os
from dotenv import load_dotenv
import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI

# load_dotenv()

# Load API key from .env file
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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

def get_api_key():
    input_api_key = st.text_input("API Key", value="")
    return input_api_key

def get_text():
    input_text = st.text_input("Keyword", value="")

def generate_article():
    llm = OpenAI(model_name=model, temperature=temp)
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    response = llm_chain.run(keyword=keyword, max_tokens=500)
    return response


if 'api_key' not in st.session_state:
    api_form = st.form(key='API Key')
    st.markdown('## Enter Your OpenAI API Key')
    st.markdown('You can find your API key at https://beta.openai.com/account/api-keys')
    st.markdown('If you do not have an OpenAI account, you can sign up at https://beta.openai.com')
    st.markdown('This App is hosted on Streamlit. API keys are stored in the session state and will be destroyed when you closer your browser.')
    st.markdown('If you do not feel comfortable entering your API key, you can clone this repo and run the app locally.')
    st.markdown('Repo can be found at github.com/gnostichumor/seo-content-streamlit')
    st.session_state.api_key = api_form.text_input("API Key", value="")
    OPENAI_API_KEY = st.session_state.api_key
    api_submitted = api_form.form_submit_button(label="Submit")

submit = False

if api_submitted:
    generate_form = st.form(key='Generate Article')
    keyword = generate_form.text_input("Keyword", value="")
    submit = generate_form.form_submit_button(label="Generate Article")

st.markdown("## Generated Article")
if submit:
    article = generate_article()
    st.write(article)


