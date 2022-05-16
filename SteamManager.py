import os
from pysteamcmdwrapper import SteamCMD, SteamCMDException

STEAM_CMD_PATH = "C:\\steamcmd"


class SteamManager:
    def __init__(self):
        if not os.path.isdir(STEAM_CMD_PATH):
            os.mkdir(STEAM_CMD_PATH)
        steam = SteamCMD(STEAM_CMD_PATH)
        try:
            steam.install()
        except SteamCMDException:
            print("SteamCMD is already installed!")
        self.steam = steam

    def login(self):
        self.steam.login()

    def install_day_z_server(self, install_dir):
        self.steam.app_update(223350, install_dir=install_dir)

    def download_workshop_item(self, workshop_id):
        self.steam.workshop_update(221100, workshop_id)
