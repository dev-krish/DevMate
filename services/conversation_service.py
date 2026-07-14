from typing import Dict, List

MAX_HISTORY = 20  # 10 user + 10 assistant messages

# chat_id -> conversation history
_conversations: Dict[int, List[dict]] = {}


def get_history(chat_id: int) -> List[dict]:
    """
    Return the conversation history for a chat.
    """

    return _conversations.get(chat_id, []).copy()


def save_message(chat_id: int, role: str, content: str) -> None:
    """
    Save a message to the conversation history.
    """

    if chat_id not in _conversations:
        _conversations[chat_id] = []

    _conversations[chat_id].append(
        {
            "role": role,
            "content": content,
        }
    )

    # Keep only the latest messages
    _conversations[chat_id] = _conversations[chat_id][-MAX_HISTORY:]


def clear_history(chat_id: int) -> None:
    """
    Clear a conversation.
    """

    _conversations.pop(chat_id, None)