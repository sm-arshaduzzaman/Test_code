import random
import string
import tkinter as tk
from tkinter import scrolledtext

def generate_area():
    return [round(random.uniform(0, 20), 2) for _ in range(4)]

def generate_device_name(used_letters):
    letters = list(string.ascii_uppercase)
    random.shuffle(letters)
    for letter in letters:
        if letter not in used_letters:
            return letter
    return random.choice(letters)  # fallback

def generate_mac_suffix(used):
    while True:
        val = random.randint(1, 254)
        if val not in used:
            return val

def generate_device_block(used_letters, used_macs):
    device_letter = generate_device_name(used_letters)
    used_letters.add(device_letter)
    mac_suffix = generate_mac_suffix(used_macs)
    used_macs.add(mac_suffix)
    
    area = generate_area()
    block = f"""      - name: Device {device_letter}
        random_address: AA:BB:CC:DD:EE:{mac_suffix:02X}
        duration:
          - 2.5
          - 3
        zone:
          name: Zone {device_letter}
          area:
            - {area[0]}
            - {area[1]}
            - {area[2]}
            - {area[3]}
"""
    return block

def generate_yaml_blocks(count=5):
    used_letters = set()
    used_macs = set()
    blocks = [generate_device_block(used_letters, used_macs) for _ in range(count)]
    return "\n".join(blocks), len(blocks)

def on_generate(text_area, count_label, block_count):
    text_area.configure(state="normal")
    text_area.delete(1.0, tk.END)
    new_text, actual_count = generate_yaml_blocks(block_count.get())
    text_area.insert(tk.INSERT, new_text)
    text_area.configure(state="normal")
    count_label.config(text=f"YAML blocks: {actual_count}")

def copy_to_clipboard(text_area, root):
    yaml_text = text_area.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(yaml_text)
    root.update()  # Keep clipboard after closing
    tk.messagebox.showinfo("Copied", "YAML copied to clipboard!")

def popup_yaml():
    root = tk.Tk()
    root.title("Generated YAML")
    root.geometry("700x600")

    block_count = tk.IntVar(value=10)

    frame = tk.Frame(root)
    frame.pack(pady=5)

    count_label = tk.Label(frame, text="YAML blocks: 0", font=("Arial", 12))
    count_label.pack(side="left", padx=10)

    gen_button = tk.Button(frame, text="Generate YAML", command=lambda: on_generate(text_area, count_label, block_count), font=("Arial", 12))
    gen_button.pack(side="left", padx=10)

    copy_button = tk.Button(frame, text="Copy to Clipboard", command=lambda: copy_to_clipboard(text_area, root), font=("Arial", 12))
    copy_button.pack(side="left", padx=10)

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 10))
    text_area.pack(expand=True, fill="both", padx=10, pady=5)

    # Initial generate
    on_generate(text_area, count_label, block_count)

    root.mainloop()

if __name__ == "__main__":
    popup_yaml()
