# repo_miner.py

from github import Github
import base64
import json

class RepoMiner:
    def __init__(self, target_repo_name):
        self.target_repo_name = target_repo_name
        self.collected_data = []

    def mine_repositories(self):
        """Mine public repositories for sensitive data"""
        g = Github()  # No auth needed for public repos
        
        # Search for repositories matching target name
        repos = g.search_repositories(self.target_repo_name)
        
        for repo in repos:
            try:
                # Look for specific files
                files_to_check = [
                    'UserPubkey.pub',
                    'config.js',
                    'environment.ts'
                ]
                
                for file_name in files_to_check:
                    try:
                        content = repo.get_contents(file_name)
                        decoded_content = base64.b64decode(content.content)
                        self.collected_data.append({
                            'repo': repo.full_name,
                            'file': file_name,
                            'content': decoded_content.decode('utf-8')
                        })
                    except:
                        continue
            except Exception as e:
                print(f"Error mining repo {repo.full_name}: {str(e)}")
                continue

        return self.collected_data