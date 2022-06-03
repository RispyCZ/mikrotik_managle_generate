import paramiko
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(os.getenv('SSH_IP'), int(os.getenv('SSH_PORT')), os.getenv('SSH_USER'), os.getenv('SSH_PASSWORD'))
