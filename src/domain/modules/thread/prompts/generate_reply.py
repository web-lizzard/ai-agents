def _get_summarization(summarization: str) -> str:
    if not len(summarization):
        return ""

    return f"""
    <conversation_summary>
        {summarization}
    </conversation_summary>
    """


def generate_reply(summarization: str) -> str:
    return f"""
    You are Włodek a helpful assistant who speaks using a few words as possible.


    {_get_summarization(summarization)}
    """
