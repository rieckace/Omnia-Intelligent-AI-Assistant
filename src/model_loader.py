# src/model_loader.py
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_llm(model_name: str = "mistralai/Mistral-7B-Instruct-v0.2"):
    """
    Loads an open-source model using HuggingFace Transformers
    and wraps it as a LangChain LLM pipeline.
    """
    print(f"🔹 Loading model: {model_name} ...")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype="auto",
        device_map="auto"
    )

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=256,
        temperature=0.7,
        do_sample=True
    )

    llm = HuggingFacePipeline(pipeline=pipe)
    return llm
