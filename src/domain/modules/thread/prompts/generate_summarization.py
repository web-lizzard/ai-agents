# `Please summarize the following conversation in a concise manner, incorporating the previous summary if available:
# <previous_summary>${previousSummarization || "No previous summary"}</previous_summary>
# <current_turn> User: ${userMessage.content}\nAssistant: ${assistantResponse.content} </current_turn>


def generate_summarization(
    previous_summarization: str, user_message: str, assistant_response: str
) -> str:
    return f"""
    Please summarize the following conversation in a concise manner, incorporating the previous summary if available:
 <previous_summary>{previous_summarization if len(previous_summarization) else "No previous summary"}</previous_summary>
 <current_turn> User: ${user_message}\nAssistant: ${assistant_response} </current_turn>
    """
