# Prompt template for FAQ answering
FAQ_PROMPT = (
    "You are an AI Assistant that answers questions based on the provided context from the FAQ.\n"
    "Answer the user's question as accurately as possible using only the information from the context.\n"
    "If the answer is not in the context, say 'I don't know based on the provided information.'\n"
    "\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
)
