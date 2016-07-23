# Wriker
Plugin to open a Wrike task straight from Sublime Text

Use the shortcut `super+shift+9` to open the task, or use the command `open_wrike_task` if you want to define your own shortcut.

# Behind the scenes
It looks at the git branch name of the file you're currently on to find the task ID.
The git branch name has to start with `w9999999999` where 9999999999 would be the branch ID. For example: `w9999999999-some-branch-name`.
The branch ID is found here:
![screen shot 2016-07-23 at 6 40 45 pm](https://cloud.githubusercontent.com/assets/876161/17080852/a7068ae8-5105-11e6-90ca-b8f61205173f.png)

# Pro tip
Instead of manually creating your branch name, you can use `git_branch_from_task` from [git-scripts](https://github.com/bodyshopbidsdotcom/git-scripts):
```shell
$ git branch
* master

$ git_branch_from_task 102024221

$ git branch
* w102024221-vehicle-type-field-ui
  master
```
