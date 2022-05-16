import os


class FileManager:
    _workshop_dir = ""
    _server_dir = ""

    def __init__(self, server_dir, workshop_dir):
        self._server_dir = server_dir
        self._workshop_dir = workshop_dir

    def set_mod_link(self, mod_id, folder_name):
        try:
            os.symlink(os.path.join(self._workshop_dir, mod_id), os.path.join(self._server_dir, folder_name))
        except FileExistsError:
            print(f"SymLink for mod {folder_name} already exists")

