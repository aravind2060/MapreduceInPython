from snakebite.client import Client

client = Client('namenode', 9000)
for x in client.ls(['/']):
   print x