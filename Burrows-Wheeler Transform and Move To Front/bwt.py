def transform_bwt(message: str) -> tuple:
    words = [message]
    message_idx = None

    for i in range(len(message) - 1):
        words.append(message[i + 1:] + message[0:i + 1])
    words.sort()

    last_column = []
    for idx, s in enumerate(words):
        if s == message:
            message_idx = idx
        last_column.append(s[-1])

    return ''.join(last_column), message_idx
