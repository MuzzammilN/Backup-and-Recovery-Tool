import pathlib
from datetime import datetime
import shutil

PATH = r""
BACKUP_PATH = r""

def create_backup(source_directory: str, backup_directory: str) -> None:
    source_dir = pathlib.Path(source_directory)
    backup_dir = pathlib.Path(backup_directory)

    if not source_dir.exists():
        print("Source path does not exist")

    if not source_dir.is_dir():
        print("Source path is not a directory")

    if not backup_dir.is_dir():
        print("Backup path is not a directory")
    current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")

    print(current_timestamp)

    make_dir_backup = pathlib.Path(f"{backup_dir}\\backup")

    if make_dir_backup.exists():
        dst_path = copy_files(source_dir, make_dir_backup, current_timestamp)

    else:
        try:
            make_dir_backup.mkdir()
            copy_files(source_dir, make_dir_backup)
        except Exception as e:
            print("Unable to make a new directory for backup files")


def copy_files(src_path: pathlib.Path, dst_path: pathlib.Path, date: datetime) -> str:
    files = list(src_path.iterdir())
    try:
        dst = pathlib.Path(f"{dst_path}\\{date}")
        dst.mkdir()
    except Exception as e:
        print("Unable to copy files over")

    for file in files:
        file_destination = f"{dst}\\{file.stem}_{date}{file.suffix}"
        shutil.copy(file, file_destination)

    print(f"Files copied over to path: {file_destination}")

    return file_destination

create_backup(PATH, BACKUP_PATH)



