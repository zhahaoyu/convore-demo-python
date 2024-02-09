from enum import Enum


class EventType(str, Enum):
    CONVERSATION_DONE = "conversation_done"
    CONVERSATION_MARKED_AS_SPAM = "conversation_marked_as_spam"
    CONVERSATION_MOVED_TO_TRASH = "conversation_moved_to_trash"
    CONVERSATION_REOPENED = "conversation_reopened"
    CONVERSATION_RESTORED_FROM_TRASH = "conversation_restored_from_trash"
    CONVERSATION_UNMARKED_AS_SPAM = "conversation_unmarked_as_spam"
    LABEL_ADDED_TO_CONVERSATION = "label_added_to_conversation"
    LABEL_REMOVED_FROM_CONVERSATION = "label_removed_from_conversation"
    MESSAGE_INBOUND_RECEIVED = "message_inbound_received"
    MESSAGE_OUTBOUND_SENT = "message_outbound_sent"

    def __str__(self) -> str:
        return str(self.value)
