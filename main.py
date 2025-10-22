import os
import yaml

def unsafe_command(input_str):
    os.system(input_str)  # vulnerability

with open('config.yaml', 'r') as f:
    config = yaml.full_load(f)

unsafe_command(config.get('user_input', 'echo Hello'))
