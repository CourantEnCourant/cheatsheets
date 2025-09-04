

"""Whisper model base"""
pipe = pipeline("automatic-speech-recognition",
                model="openai/whisper-base",
                device=device)


def whisper(audio,
         max_new_tokens,
         generate_kwargs=None,
         chunk_length_s=30,
         batch_size=8,
         return_timestamps=True):
    """
    :param audio:
    :param max_new_tokens:
    :param generate_kwargs: {"task": "transcribe"} or {"task": "translation"}
    :param chunk_length_s:
    :param batch_size:
    :param return_timestamps:
    :return:
    """

    return


