import subprocess


tool_path = ".\\shibuyaTools.exe"


def export_game(gamepath, export_directory):
    """extract the game assets

    Args:
        gamepath (str): path of the game
        export_directory (str): directory where files will be extracted
    """
    shell_command = [
        tool_path,
        "export",
        "--game-path",
        gamepath,
        "--export-directory",
        export_directory
    ]
    subprocess.run(shell_command, shell=True)


def import_game(gamepath, source_directory, object_directory):
    """insert game assets in the game

    Args:
        gamepath (str): path of the game
        source_directory (str): same as export_directory of export_game
        object_directory (str): temp directory
    """
    shell_command = [
        tool_path,
        "import",
        "--game-path",
        gamepath,
        "--source-directory",
        source_directory,
        "--object-directory",
        object_directory
    ]
    subprocess.run(shell_command, shell=True)
