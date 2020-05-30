# Project Template

This template can be used to create a new data science project. You must have [cookiecutter](https://pypi.org/project/cookiecutter/) installed:

```pip install cookiecutter```

To create a new project, run the command: `cookiecutter ~/ds_template`. You will be prompted to enter some basic information about the project. If you hit `Enter` without specifying a value, the default value (shown in brackets) will be used. Some directories (e.g. lib) are optional and will only be generated if you answer 'yes' to that option when creating your project. 

```
author [Harrison Mamin]: 
email [hmamin55@gmail.com]: 
dir_name [HelloWorld]:
description [Data Science project.]:
lib [yes]:
services [yes]:
```

In this example, the following file structure was generated. The information you enter will determine which directories are generated and will populate various fields throughout the project. 

```
HelloWorld/
├── README.md
├── .gitignore
├── data
│   └── README.md
├── notebooks
│   └── README.md
├── reports
│   └── README.md
├── bin
│   └── README.md
├── services
│   └── README.md
└── lib
    ├── helloworld
    │   ├── __init__.py
    │   └── utils.py
    ├── MANIFEST.in
    ├── README.md
    ├── requirements.txt
    └── setup.py
```

From the project's root directory, you can run the command `pip install -e lib`. This will make your package importable from other directories. 

