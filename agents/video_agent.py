import os
import glob
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips


def create_video():

    image_folder = "assets/images"
    audio_path = "output/voice.mp3"

    if not os.path.exists(audio_path):
        print("Voice file not found!")
        return

    images = sorted(glob.glob(os.path.join(image_folder, "*.jpg")))

    if len(images) == 0:
        print("No images found!")
        return

    audio = AudioFileClip(audio_path)

    duration = audio.duration / len(images)

    clips = []

    for image in images:

        clip = (
            ImageClip(image)
            .with_duration(duration)
            .resized(height=1920)
        )

        clips.append(clip)

    final_video = concatenate_videoclips(clips, method="compose")

    final_video = final_video.with_audio(audio)

    os.makedirs("output", exist_ok=True)

    output_path = "output/final_video.mp4"

    final_video.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )

    print("\nVideo Generated Successfully")
    print(output_path)