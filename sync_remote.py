import subprocess
import os
import sys

def show_dir(remote_name, remote_folder):
    """ Show directory. Was used for testing purposes"""
    # rclone command
    rclone_command = [
        "rclone", "lsd",
        f"{remote_name}:{remote_folder}"
    ]
        
    # run 
    try:
        subprocess.run(rclone_command, check=True)
        print("Sync Completed Succesfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Rclone sync failed with return code {e.returncode}")

def sync_with_clone(local_folder, remote_name, remote_folder):
    """ takes a local folder path and syncs it with the folder in the remote drive"""

    # check if remote directory exists, create it if not
    remote_exists_command = ["rclone", "lsd", f"{remote_name}:{remote_folder}"]
    try:
        subprocess.run(remote_exists_command, check=True)
    except subprocess.CalledProcessError:
        # remote folder does not exist; create it
        remote_create_command = ["rclone", "mkdir",
                                 f"{remote_name}:{remote_folder}"
                                 ]
        try:
            subprocess.run(remote_create_command, check=True)
            print(f"Created remote folder: {remote_folder}")
        except subprocess.CalledProcessError as e:
            print(f"Error: failed to create remote folder {remote_folder}")
            print(f"Rclone mkdir failed with return code {e.returncode}")
            sys.exit(1)


    # rclone cli command to sync
    rclone_command = [
        "rclone", "sync",
        local_folder,
        f"{remote_name}:{remote_folder}"
    ]

    # run 
    try:
        subprocess.run(rclone_command, check=True)
        print("Sync Completed Succesfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Rclone sync failed with return code {e.returncode}")

if __name__ == "__main__":
    # check provided arguments 
    # 4 since script name is argv[0]
    if len(sys.argv) != 4:
        print("Usage: python3 sync_remote.py local_folder remote_name remote_folder")
        sys.exit(1)

    # extract args
    local_folder = sys.argv[1]
    remote_name = sys.argv[2]
    remote_folder = sys.argv[3]

    sync_with_clone(local_folder, remote_name, remote_folder)