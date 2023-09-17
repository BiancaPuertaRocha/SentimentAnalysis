import pandas as pd
import json

df = pd.read_csv('files/top5/commits_per_project/commits20.csv')
print(df.head())


with open('files/top5/projects_per_languages/projects.json', 'r') as f:
    data = json.load(f)

## adicionando language no dataset para cada commit
df_data = []
total_projs = []
for i, item in enumerate(data):
    lang = item["lang"]
    repos = item["repos"]
    for repo_info in item["repo"]:
        repo_name = repo_info["name"]
        stars = repo_info["stars"]
        total_projs.append(repo_name)
        df_data.append({"lang": lang, "repos": repos, "repo_name": repo_name, "stars": stars})

df_data = pd.DataFrame(df_data)

df_original = pd.DataFrame(df)

df_resultado = df_data.merge(df_original, left_on="repo_name", right_on="project", how="left")

# contando projetos por linguagem em que foram encontrados commits
print(df_resultado.groupby('lang')['project'].nunique().reset_index())


# para nao desbalancear, vamos pegar uma sample desses dados que seja igualitaria para as linguagens apresentadas


print(','.join([f"'{x}'" for x in total_projs]))