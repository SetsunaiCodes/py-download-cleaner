import os
import shutil
import ctypes

def move_downloads_to_trash(download_dir):
    download_path = os.path.expanduser(download_dir)
    
    if not os.path.exists(download_path):
        print("Der Download-Ordner existiert nicht.")
        return
    
    files = os.listdir(download_path)
    
    for file_name in files:
        file_path = os.path.join(download_path, file_name)
        
        try:
            ctypes.windll.shell32.SHFileOperationW(None, 2, file_path, None, None, 0)
            print(f"{file_name} wurde erfolgreich in den Papierkorb verschoben.")
        except Exception as e:
            print(f"Fehler beim Verschieben von {file_name}:", str(e))

move_downloads_to_trash("~/Downloads")
