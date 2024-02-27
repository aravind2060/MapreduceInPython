from snakebite.client import Client

client = Client('namenode', 9000)
for f in client.copyToLocal(['/tmp/sample.txt'],'user/root/input/'):
   print f