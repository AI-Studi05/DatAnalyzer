# DatAnalyzer

## To add in README
- [ ] Contributing
- [ ] Licence

## How to work with this repo
The *main* is protected, pull requests must be done as they require review to be completed.

Please follow some guidelines to improve clarity.

### Commit message policy
Please follow and use the recommended pattern for your commit messages. It helps having an easy-to-read git history :)

| ADD  | something new is added       |
|------|------------------------------|
| REM  | something was removed        |
| CHG  | something was changed        |
| FIX  | problem was corrected        |
| MOV  | something was moved          |
| NOTE | additional important message |
| WARN | additional warning message   |

**Example** "ADD: new get method, MOV: ressources"

### Branches names
Using *dev/amazing_feature* or *hotfix/issue_66*, *gui/input_fields* really helps to filter and see what are each branch doing. Is it a test, a hotfix, or even a bug resolution?
There is no limit as for the commit messages policy but the basics mentionned here covers many cases.

For more, read [this](https://dev.to/couchcamote/git-branching-name-convention-cch) article.

### Virtual environnement
The virtual environnement could be created based on the ```sources\requirement.txt```.

Using ```conda create --name <env> --requirements.txt```.

To update the requirements, please use ```pip list --format=freeze > requirements.txt```.

### Linter
An [Action](https://github.com/AI-Studi05/DatAnalyzer/actions/workflows/linter.yml) is running on each push to ensure consistency.

To test and run it locally: ```flake8 path\to\code.py --count --max-complexity=10 --max-line-length=127 --statistics```

**Please do it before pushing, reducing the amount of useless commits!**
