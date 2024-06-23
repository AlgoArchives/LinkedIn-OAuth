# src/utils.py

def save_details_to_file(pending_connections, high_follower_connections, file_path='data/linkedin_details.txt'):
    with open(file_path, 'w') as file:
        file.write("Pending Connection Requests:\n")
        for pending in pending_connections:
            file.write(f'- {pending}\n')
        file.write("\nConnections with 10,000+ Followers:\n")
        for high_follower in high_follower_connections:
            file.write(f'- {high_follower}\n')