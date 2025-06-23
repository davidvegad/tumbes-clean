import os

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')
TEAM_DIR = os.path.join(MEDIA_ROOT, 'team')

print("MEDIA_ROOT:", MEDIA_ROOT)
print("Archivos en TEAM_DIR:", TEAM_DIR)

if os.path.isdir(TEAM_DIR):
    print("Contenido de 'team/':")
    for fname in os.listdir(TEAM_DIR):
        fpath = os.path.join(TEAM_DIR, fname)
        print(f"- {fname} ({'archivo' if os.path.isfile(fpath) else 'NO es archivo'})")
else:
    print("No existe la carpeta 'team/' en media.")
