# cookiecutter-django-app

Cookiecutter template for a Django app. 

* Testing setup with ``py.test``
* circleci: Ready for CircleCI Continuous Integration testing
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_

## Quick Start

To create a new django app:
 - Create a new project directory
 - Run cookiecutter against this `git`

e.g
```console
    mkdir -p new_project/
    cd new_project
    cookiecutter https://github.com/jtarball/cookiecutter-django-app
```

Then:
* Create a repo and put it there.
* Add repo to CircleCI
* You might need an user ssh key on CircleCI
```
    Under your project settings
    Permissions -> Checkout SSH Keys
    Click Create and add <Username> user key
```
* You will need to create a branch `gh-pages` to run the documentation

* Write your application (Search and replace Example model with appropriate name)
* Modify the documentation
* Modify and add tests