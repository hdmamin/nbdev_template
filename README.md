# Project Template

This template can be used to create a new data science project. You must have [cookiecutter](https://pypi.org/project/cookiecutter/) and [nbdev](https://pypi.org/project/nbdev/) installed:

```pip install cookiecutter nbdev```

If you clone this repo into your home directory, you can create a new project by running the command: `cookiecutter ~/nbdev_template`. You will be prompted to enter some basic information about the project. If you hit `Enter` without specifying a value, the default value (shown in brackets) will be used. Some directories (e.g. apps) are optional and will only be generated if you answer 'yes' to that option when creating your project. 

```
author [Harrison Mamin]: 
email [hmamin55@gmail.com]: 
dir_name [Your project name (no spaces, lowercase)]:
description [Description of your library.]:
apps [yes]:
reports [yes]:
```

In this example, the following file structure would be generated inside a directory with your specified `dir_name`. The information you enter will determine which directories are generated and will populate various fields throughout the project. 

```
├── CONTRIBUTING.md
├── LICENSE
├── MANIFEST.in
├── README.md
├── bin/
├── data/
├── dev_notebooks/
├── notebooks/
├── notes/
├── reports/
├── services/
├── requirements.txt
├── settings.ini
└── setup.py
```

