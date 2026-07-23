import os
import sys
import subprocess
from urllib.request import urlretrieve

MODEL_URLS = [
    "https://huggingface.co/mradermacher/KobbleTinyV2-1.1B-GGUF/resolve/main/KobbleTinyV2-1.1B.Q6_K.gguf",
    "https://huggingface.co/concedo/KobbleTinyV2-1.1B-GGUF/resolve/main/KobbleTiny-Q4_K.gguf"
]
MODEL_FILENAME = "KobbleTiny-Q6_K.gguf"

def download_model():
    if os.path.exists(MODEL_FILENAME):
        print(f"[+] {MODEL_FILENAME} already exists locally.")
        return
    
    for url in MODEL_URLS:
        print(f"[*] Trying to download model from: {url}")
        try:
            urlretrieve(url, MODEL_FILENAME)
            print(f"[+] Download completed successfully: {MODEL_FILENAME}")
            return
        except Exception as e:
            print(f"[!] Failed to download from {url}: {e}")
    
    print("[-] Error: Could not download GGUF from any source URL.")
    sys.exit(1)

def setup_git_lfs():
    print("[*] Setting up Git LFS tracking for *.gguf files...")
    subprocess.run(["git", "lfs", "install"], check=False)
    subprocess.run(["git", "lfs", "track", "*.gguf"], check=False)
    print("[+] Git LFS configured for *.gguf files.")

if __name__ == "__main__":
    print("=== MOONMILK 1.0 Release Preparation ===")
    download_model()
    setup_git_lfs()
    print("\n[+] All release files prepared successfully!")
