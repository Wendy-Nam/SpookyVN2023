import os
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)  # Get the parent directory of the script

def generate_lipsync_data(chapter_dir, audio_file):
    # Generate lipsync data using Rhubarb
    rhubarb_path = os.path.join(script_dir, "Rhubarb-Lip-Sync-1.13.0-macOS", "rhubarb")
    audio_path = os.path.join(parent_dir, "audio", "voice", chapter_dir, audio_file)
    output_path = os.path.join(script_dir, "lip-sync-data", chapter_dir, os.path.splitext(audio_file)[0] + ".txt")
    # Create the corresponding directory structure in the output path
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)
    # Run Rhubarb to generate lipsync data
    subprocess.run([rhubarb_path, "-f", "tsv", "-o", output_path, audio_path], check=True)
    print(f"Lipsync data generated for {audio_file}")

# Iterate through chapters and voice files
chapters = [d for d in os.listdir(os.path.join(script_dir, os.pardir, "audio/voice")) if os.path.isdir(os.path.join(script_dir, os.pardir, "audio/voice", d))]
for chap in chapters:
    voice_dir = os.path.join(os.path.join(script_dir, os.pardir, "audio/voice"), chap)
    voice_files = [f for f in os.listdir(voice_dir) if f.endswith(".wav") or f.endswith(".ogg")]
    for voice_file in voice_files:
        generate_lipsync_data(chap, voice_file)
