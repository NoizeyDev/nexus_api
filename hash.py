import hashlib

def file_hash(file_path):
    with open(file_path, 'rb') as f:
        digest = hashlib.md5(f.read()).hexdigest()
    return digest
hashed = file_hash('./_dump/SkyUI_5_2_SE-12604-5-2SE.7z')
print(hashed)
#60385f7094908527b0823a0497b764b6


