import psutil, GPUtil

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
vram = psutil.virtual_memory()
print("RAM: " + get_size(vram.total))
print("RAM In-Use: " + get_size(vram.used))
print("Free RAM: " + get_size(vram.available))