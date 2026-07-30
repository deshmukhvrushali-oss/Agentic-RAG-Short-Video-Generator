from gtts import gTTS
import os


def generate_voice(script):

    os.makedirs("output", exist_ok=True)

    tts = gTTS(
        text=script,
        lang="en",
        slow=False
    )

    output_file = "output/voice.mp3"

    tts.save(output_file)

    print("Voice Generated Successfully")

    return output_file