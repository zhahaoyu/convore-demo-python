from convore_api_client import MessageParticipant, MessageParticipantRole
from convore_api_client.models import Message, ChannelAddress


def print_email_content(message: Message) -> str:
    result = []
    result.append(f"From: {print_participant(message.sender)}")
    to_recipients = [recipient for recipient in message.recipients if recipient.role == MessageParticipantRole.TO]
    result.append(f"To: {print_participants(to_recipients)}")
    cc_recipients = [recipient for recipient in message.recipients if recipient.role == MessageParticipantRole.CC]
    if cc_recipients:
        result.append(f"CC: {print_participants(cc_recipients)}")
    bcc_recipients = [recipient for recipient in message.recipients if recipient.role == MessageParticipantRole.BCC]
    if bcc_recipients:
        result.append(f"BCC: {print_participants(bcc_recipients)}")
    result.append(f"Date: {message.var_date}")
    result.append(f"Subject: {message.subject}")

    file_attachments = [attachment for attachment in message.attachments if not attachment.is_inline]
    if file_attachments:
        result.append("Attachments:")
        for attachment in file_attachments:
            result.append(f"- {attachment.filename} ({attachment.size} bytes)")
    result.append("---------------BODY START---------------")
    # Regular expression to remove invisible characters (like ZWNJ, ZWJ, etc.) that lead GPT to
    # think the email is empty.
    # TODO: Python built-in Re does not support this expression. Use a third party library or move the logic to server side.
    # cleaned_body_text_content = re.sub(r'\p{Cf}', '', message.text_body)
    cleaned_body_text_content = message.text_body
    truncated_body = cleaned_body_text_content[:3000]
    result.append(truncated_body + ("..." if len(truncated_body) < len(cleaned_body_text_content) else ""))
    result.append("---------------BODY END---------------")
    return '\n'.join(result)

def print_participants(participants: list[MessageParticipant]) -> str:
    return ", ".join([print_participant(participant) for participant in participants])

def print_participant(message_participant: MessageParticipant) -> str:
    return f"{message_participant.name} <{message_participant.handle.value}>"

def print_channel_addresses(channelAddresses: list[ChannelAddress]) ->str:
    return ", ".join([f"{address.name} <{address.handle.value}>" for
            address
            in channelAddresses])
