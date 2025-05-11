import subprocess

# Function to build the Docker container for a bot
def build_docker_image(bot_id):
    subprocess.run(["docker", "build", "-t", bot_id, bot_id])

# Function to start the Docker container for a bot
def start_docker_container(bot_id):
    subprocess.run(["docker", "run", "-d", "--name", bot_id, bot_id])

# Function to stop the Docker container for a bot
def stop_docker_container(bot_id):
    subprocess.run(["docker", "stop", bot_id])
    subprocess.run(["docker", "rm", bot_id])

# Function to remove bot files from the system
def delete_bot_files(bot_id):
    subprocess.run(["rm", "-rf", bot_id])
