from models import Project,ACEUserProfile

with open("projects.tsv",encoding = 'utf-8') as f:
    csv = f.read().splitlines()

print(csv)

for proj in csv:
    name,stack,developer,date,image,description = proj.split("\t")

    if name == 'Project Name':
        continue
    
    project = Project(
        name = name,
        description = description,
        tools = stack
    )

    developer = developer.split(",")