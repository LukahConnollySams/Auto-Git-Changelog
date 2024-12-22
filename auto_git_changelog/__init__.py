from jinja2 import Template

# files
pyproject_file = 'pyproject.toml'
changelog_file = 'CHANGELOG.md'


# commit type dict
update_dict = {
    'fix': 'patch',
    'feat': 'minor',
    'feat!': 'major',
    'chore': 'none',
    'docs': 'none',
    'style': 'none',
    'refactor': 'patch',
    'perf': 'patch',
    'test': 'none'
}

# changelog templates
changelog_version_template = Template("<h2 id='{{ version }}'>v{{ version }}</h2>")

changelog_template = Template("<p>{{ date }}\t{{ message }}</p>")