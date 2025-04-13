# Lab17_apisani-2_java_repos.py
# Alex Pisani
# Aug 9 2024
# scrapes GitHub for the highest-starred java repositories and then plots the results

import requests
import matplotlib.pyplot as plt

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

# Prepare data for plotting
repo_names = [repo_dict['name'] for repo_dict in repo_dicts]
repo_stars = [repo_dict['stargazers_count'] for repo_dict in repo_dicts]

# Plotting
plt.figure(figsize=(12, 8))
plt.barh(repo_names, repo_stars, color='skyblue')
plt.xlabel('Number of Stars')
plt.ylabel('Repository')
plt.title('Top Java Repositories on GitHub by Stars')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest stars at the top
plt.show()