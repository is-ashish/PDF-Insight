from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser
from config import GROQ_API_KEY
from langsmith import traceable
from langsmith.run_helpers import get_current_run_tree



@traceable(
    run_type="retriever",
    name="Context Builder",
    metadata={"llm": "llama-3.3-70b-versatile", "framework": "LangChain"}
)

def build_chain(vectorstore, threshold=2):
    
    print("Building chain .............................")
    
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.5,
        streaming=True,
        api_key=GROQ_API_KEY,
    )

    prompt = ChatPromptTemplate.from_template("""
                                              
    You are a helpful assistant for customer support.

    Use ONLY the information provided in the retrieved context to answer the user's question.
    If the context does not contain the answer, respond with: "I don't know based on the available information."

    Guidelines:
    - Be concise and clear.
    - Do not invent facts outside the context.
    - If multiple relevant points exist, summarize them logically."

    Context:
    {context}

    Question:
    {question}
    """)

    # retriever = vectorstore.as_retriever(
    #     search_kwargs={"k": 5}  # retrieve top 5
    # )

    def context_builder(question:str):
        # Step 1: similarity search with scores
        results = vectorstore.similarity_search_with_score(
            question,
            k=5,
        )
        # --------------- Tracing ----------------
        #log retrieved docs + scores to LangSmith
        run_tree = get_current_run_tree()
        if run_tree:
            run_tree.metadata.update({
                "retrieved_docs": [doc.page_content for doc, _ in results],
                "scores": [score for _, score in results],
                "metadata": [doc.metadata for doc, _ in results]                
            })
        # ----------------------------------------

        # Step 2: apply score threshold
        filtered = [doc for doc, score in results if score <= threshold]
        
        if not filtered:
            return "", []   # empty context → triggers "I don't know"
        return "\n\n".join(d.page_content for d in filtered), filtered

    def run_chain(question: str):
        context, document  = context_builder(question)
        answer_By_LLM = llm.invoke(prompt.format(context=context, question=question)).content
        return {
            "response": answer_By_LLM.strip(),
            "documents": document
        }
    
    return run_chain
