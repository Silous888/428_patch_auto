from fileFolderUI import FileFolderUI
import utils
import drive_to_local
from API import steam_game_api
import shibuya_tools_api

import os

# pyinstaller --onefile --noconsole --name 428_Patch_Automatique --icon=./ressource/DreamteamLogo.ico main.py

utils.import_names_files()


def process(instance_worker):
    gamepath_directory = steam_game_api.find_game_path("428_shibuya_scramble_en")
    name_game_exe = "428 Shibuya Scramble.exe"
    gamepath = os.path.join(gamepath_directory, name_game_exe)

    source_directory = "F:\\Documents\\traduction_DreamTeam\\428\\export"
    object_directory = "F:\\Documents\\traduction_DreamTeam\\428\\object"

    drive_to_local.replace_every_files_text(instance_worker)

    # # sm.incrementer_progression(instance_worker, 10)
    drive_to_local.update_texte_progression(instance_worker, "recompilation")
    shibuya_tools_api.import_game(gamepath, source_directory, object_directory)


# -------------------- Main code -------------------
if __name__ == "__main__":
    var = FileFolderUI()
    var.process_func = lambda: process(var.get_worker())
    var.has_progressbar = True
    var.has_lineedit = False
    var.run()
