#!/bin/bash

set -e

run_command() {
    echo "Executing: $1"
    if ! eval "$1"; then
        echo "Error executing: $1"
        exit 1
    fi
}

main() {
    run_command "curl -fsSL https://ollama.com/install.sh | sh"
    run_command "sudo apt install aria2 -y"
    run_command "git clone https://github.com/comfyanonymous/ComfyUI.git"
    run_command "cd ComfyUI"
    run_command "pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu124"
    run_command "pip install -r requirements.txt"
    run_command "cd models/clip && aria2c -x16 -s16 -k1M --file-allocation=none --optimize-concurrent-downloads=true https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors -o clip_l.safetensors"
    run_command "cd models/clip && aria2c -x16 -s16 -k1M --file-allocation=none --optimize-concurrent-downloads=true https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors -o t5xxl_fp8_e4m3fn.safetensors"
    run_command "cd models/clip && aria2c -x16 -s16 -k1M --file-allocation=none --optimize-concurrent-downloads=true https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors -o t5xxl_fp16.safetensors"
    run_command "cd models/vae && aria2c -x16 -s16 -k1M --file-allocation=none --optimize-concurrent-downloads=true --header=\"Authorization: Bearer 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\" https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/ae.safetensors -o ae.safetensors"
    run_command "cd models/unet && aria2c -x16 -s16 -k1M --file-allocation=none --optimize-concurrent-downloads=true --header=\"Authorization: Bearer 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\" https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux1-dev.safetensors -o flux1-dev.safetensors"

    echo "All tasks completed successfully!"
}

main