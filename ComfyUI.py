#!/usr/bin/env python3

import os
import subprocess
import sys

def run_command(command):
    print(f"Executing: {command}")
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
        rc = process.poll()
        if rc != 0:
            print(f"Error: {process.stderr.read().strip()}")
            sys.exit(rc)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    commands = [
        "curl -fsSL https://ollama.com/install.sh | sh",
        "sudo apt install aria2 -y",
        "git clone https://github.com/comfyanonymous/ComfyUI.git",
        "cd ComfyUI",
        "pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu124",
        "pip install -r requirements.txt",
        "cd models/clip && aria2c -x16 -s16 -k1M --file-allocation=none --optimize-concurrent-downloads=true https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors -o clip_l.safetensors",
        "aria2c -x16 -s16 -k1M --file-allocation=none --optimize-concurrent-downloads=true https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors -o t5xxl_fp8_e4m3fn.safetensors",
        "aria2c -x16 -s16 -k1M --file-allocation=none --optimize-concurrent-downloads=true https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors -o t5xxl_fp16.safetensors",
        "cd .. && cd vae && aria2c -x16 -s16 -k1M --file-allocation=none --optimize-concurrent-downloads=true --header=\"Authorization: Bearer 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\" https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/ae.safetensors -o ae.safetensors",
        "cd .. && cd unet && aria2c -x16 -s16 -k1M --file-allocation=none --optimize-concurrent-downloads=true --header=\"Authorization: Bearer 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\" https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux1-dev.safetensors -o flux1-dev.safetensors"
    ]

    for command in commands:
        run_command(command)

    print("All tasks completed successfully!")

if __name__ == "__main__":
    main()