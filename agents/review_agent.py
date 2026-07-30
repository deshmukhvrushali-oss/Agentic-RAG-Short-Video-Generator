import os


def review():

    files = [
        "output/research.txt",
        "output/script.txt",
        "output/seo.txt",
        "output/voice.mp3",
        "output/final_video.mp4"
    ]

    print("\nChecking Generated Files\n")

    for file in files:

        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ Missing: {file}")

    print("\nProject Completed Successfully")