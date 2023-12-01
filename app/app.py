import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline
import torch
import base64
import textwrap
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.chains import RetrievalQA
from constants import CHROMA_SETTINGS

checkpoint = "LaMini-T5-738M"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
base_model = AutoModelForSeq2SeqLM.from_pretrained(
    checkpoint, device_map="cpu", torch_dtype=torch.float32
)


@st.cache_resource
def llm_pipeline():
    pipe = pipeline(
        "text2text-generation",
        model=base_model,
        tokenizer=tokenizer,
        max_length=256,
        do_sample=True,
        temperature=0.3,
        top_p=0.95,
    )
    local_llm = HuggingFacePipeline(pipeline=pipe)
    return local_llm


@st.cache_resource
def qa_llm():
    llm = llm_pipeline()
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(
        persist_directory="db",
        embedding_function=embeddings,
    )
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True
    )
    return qa


def process_answer(instruction):
    response = ""
    instruction = instruction
    qa = qa_llm()
    genereated_text = qa(instruction)
    answer = genereated_text["result"]
    return answer, genereated_text


def main():
    st.title("Search Your PDF")
    with st.expander("About the App"):
        st.markdown(
            """
    This is a Generative AI powered Question and Answering app that responds to quesitons about your PDF file.
    """
        )

    question = st.text_area("Enter Your Question:")
    if st.button("Search"):
        st.info("Your Question: " + question)
        st.info("Your Answer")
        answer, metada = process_answer(question)
        st.write(answer)
        st.write(metada)


if __name__ == "__main__":
    main()
