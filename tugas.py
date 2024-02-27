import requests

def get_github_project_info(MusangKing16, Sarah_tugas):
  
    access_token = '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'

    repo_url = f'https://api.github.com/repos/{MusangKing16}/{Sarah_tugas}'
    headers = {'Authorization': f'token {https://github.com/MusangKing16/Sarah_tugas.git}'}
    response = requests.get(repo_url, headers=headers)

    if response.status_code == 200:
        repo_info = response.json()
        repo_id = repo_info['id']
        owner_id = repo_info['owner']['id']
        git_url = repo_info['git_url']

        return repo_id, owner_id, git_url
    else:
        print(f'Error: {response.status_code}')
        return None

username = 'MusangKing16'
repository_name = 'Sarah_tugas'

result = get_github_project_info(username, repository_name)

if result:
    repo_id, owner_id, git_url = result
    print(f'Repository ID: {repo_id}')
    print(f'Owner ID: {owner_id}')
    print(f'Git URL: {git_url}')
