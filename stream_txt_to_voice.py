from elevenlabs import generate, stream

def text_stream():
    yield "Hi there, I'm Eleven "
    yield "I'm a text to speech API "

audio_stream = generate(
    text=text_stream(),
    voice="SzymonK voice",
    model="eleven_monolingual_v1",
    stream=True
)

stream(audio_stream)
