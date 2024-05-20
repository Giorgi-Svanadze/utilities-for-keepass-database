import time, wmi, json, os, shutil, configparser, base64
from cryptography.fernet import Fernet
from pykeepass import PyKeePass
def sync():
    def read_passwords(db_name, file):
        key = read_config()
        data = get_data(file, key)
        db_info = data.get(db_name)
        result = [db_name]
        result.extend(db_info)
        return result
    def read_config():
        file = os.path.join(os.getenv('LOCALAPPDATA'), 'Multipass', 'config.ini')
        config = configparser.ConfigParser()
        config.read(file)
        if 'security' in config and 'key' in config['security']:
            key_str = config['security']['key'].encode()
            key_bytes = base64.b64decode(key_str + b'=' * (4 - len(key_str) % 4))
            return key_bytes
    def get_data(file, key):
        with open(file, 'rb') as file:
            data = file.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)
        json_data = json.loads(decrypted.decode())
        return json_data
    local_appdata_dir = os.path.join(os.getenv('LOCALAPPDATA'), "Multipass")
    for root, dirs, files in os.walk(local_appdata_dir):
        if "db_info.json" in files:
            file = os.path.abspath(os.path.join(root, "db_info.json"))
            break
    documents_dir = os.path.join(os.path.expanduser("~"), "Documents")
    for root, dirs, files in os.walk(documents_dir):
        if "Multipass" in dirs:
            n_dir = os.path.join(root, "Multipass", "User databases")
            break
    key = read_config()
    data = get_data(file, key)
    for db_name in data.keys():
        info = read_passwords(db_name, file)
        n_path = os.path.join(n_dir, info[0])
        dst_file = os.path.join(n_path, info[0]+".kdbx")
        os.remove(info[2])
        shutil.copy2(info[1], n_path)
        n_db = PyKeePass(filename=dst_file, password=info[3])
        n_db.password = info[4]
        n_db.save()
        os.rename(dst_file, info[2])
c = wmi.WMI()
pr_state = False
while True:
    process = c.Win32_Process(name="KeePass.exe")
    if process:
        pr_state = True
    elif pr_state:
        sync()
        pr_state = False
    time.sleep(3)