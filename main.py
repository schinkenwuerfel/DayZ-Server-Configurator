import argparse, os
from SteamManager import SteamManager
from FileManager import FileManager

STEAM_COMMON = "C:\\Program Files (x86)\\Steam\\steamapps\\common"
WORKSHOP_CONTENT = "C:\\steamcmd\\steamapps\\workshop\\content"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A DayZ Standalone Server Configurator")
    parser.add_argument('-server_dir', '-sd', '-s', default=os.path.join(STEAM_COMMON, "DayZServer"), nargs=1)
    parser.add_argument('-workshop_dir', '-wd', '-w', default=os.path.join(WORKSHOP_CONTENT, "221100"), nargs=1)
    parser.add_argument('-mod_list', '-ml', '-m', default="Modlist.txt", nargs=1)
    parser.add_argument('-steam_user', '-user', '-u')
    parser.add_argument('-steam_password', '-pass', '-p')

    args = parser.parse_args()

    steamManager = SteamManager()
    steamManager.login(args.steam_user, args.steam_password)

    steamManager.install_day_z_server(args.server_dir)

    fileManager = FileManager(args.server_dir, args.workshop_dir)


def setup_mods():
    with open(os.path.join(args.server_dir, args.mod_list), 'r') as file:
        for line in file:
            mod_id, folder_name = line.split(',')
            steamManager.download_workshop_item(mod_id)
            fileManager.set_mod_link(mod_id, folder_name)