import subprocess

# Path to your local file (must be accessible from within the Docker container, ensure proper volume mounting)
local_file_path = '/workspaces/MapreduceInPython/2023.csv'

# HDFS destination path
hdfs_destination_path = 'user/root/input/'

# Command to execute in the namenode container
cmd = [
    'docker', 'exec', '-it', 'resourcemanager', 
    'hadoop', 'fs', '-put', 
    local_file_path, 
    hdfs_destination_path
]

# Execute the command
subprocess.run(cmd, check=True)