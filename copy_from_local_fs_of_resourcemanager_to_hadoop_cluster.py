import subprocess

local_file_path = "/tmp/2023.csv"
hdfs_file_path = "user/root/input"

subprocess.check_call(["hdfs", "dfs", "-mkdir", "-p", hdfs_file_path])
subprocess.check_call(["hdfs", "dfs", "-copyFromLocal", local_file_path, hdfs_file_path])

output = subprocess.check_output(["hdfs", "dfs", "-ls", hdfs_file_path]).decode()
print(output)