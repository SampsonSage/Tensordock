# Comfy UI Install 

## System Update and Restart

First, update the system and restart:

```bash
sudo apt update && sudo apt upgrade -y
sudo reboot
```

## Dependencies Installation

After the system restarts, install the necessary dependencies:

```bash
sudo apt install libgl1 aria2 -y
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu124
```

## Setup Workspace and ComfyUI

Create a workspace and clone ComfyUI:

```bash
mkdir workspace && cd workspace
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
pip install -r requirements.txt
```

## Model Installation

Choose the appropriate installation based on your VRAM capacity:

<details>
<summary><h3>High VRAM Setup</h3></summary>

![Flux Dev Example](https://comfyanonymous.github.io/ComfyUI_examples/flux/flux_dev_example.png)

Run the following commands to download the necessary models:

```bash
aria2c -x 16 -s 16 https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors -o /home/user/ComfyUI/models/clip/t5xxl_fp16.safetensors

aria2c -x 16 -s 16 https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors -o /home/user/ComfyUI/models/clip/clip_1.safetensors

aria2c -x 16 -s 16 https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors -o /home/user/ComfyUI/models/vae/ae.safetensors

aria2c -x 16 -s 16 --header="Authorization: Bearer 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" https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux1-dev.safetensors -o /home/user/ComfyUI/models/unet/flux1-dev.safetensors
```

> **Note**: The last command includes an authorization token. Ensure you have the necessary permissions to use this token.

</details>

<details>
<summary><h3>Low VRAM Setup</h3></summary>

![Flux Dev Checkpoint Example](https://comfyanonymous.github.io/ComfyUI_examples/flux/flux_dev_checkpoint_example.png)

For systems with lower VRAM, use this command instead:

```bash
aria2c -x 16 -s 16 https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors -o /home/user/workspace/ComfyUI/models/checkpoints/flux1-dev-fp8.safetensors
```

</details>

## Start the web UI in the background

```bash
python main.py &
```

# Open Web UI Install

```bash
cd ..
pip install open-webui -U
```
## Start in the background
```bash
open-webui serve &
```
## Post install 
Forward ports 11434 8188 8080 7860
