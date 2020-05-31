# {{ cookiecutter.dir_name }}

# Project Description
{{ cookiecutter.description }}

### Project Author
* {{ cookiecutter.author }}

### Repo Structure
```
{{ cookiecutter.dir_name }}/
├── data             # Raw and processed data. Actual files are excluded from github.
├── notebooks        # Jupyter notebooks for experimentation and exploratory analysis.
├── dev_notebooks    # Jupyter notebooks for library development.
├── reports          # Markdown reports (performance reports, blog posts, etc.)
├── bin              # Executable scripts to be run from the project root directory.
└── apps             # Apps or other tools to interact with data or models.
```

Once you build your library using `nbdev_build_lib`, an additional directory will be created and python files will be populated based on your code in `dev_notebooks`.

