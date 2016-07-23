import sublime
import sublime_plugin
import os
import subprocess
import re
import webbrowser

class OpenWrikeTaskCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    git_dir = get_git_dir(self.view.file_name())
    if git_dir is None:
      sublime.message_dialog('Not a git repo')
      return

    current_branch = output_from_command('git', '--git-dir', git_dir + '/.git' ,'rev-parse', '--abbrev-ref', 'HEAD')

    match = re.match(r'^\s*w(\d+)', current_branch, flags = re.IGNORECASE)
    if match is None:
      sublime.message_dialog('"' + current_branch + '" is not a Wrike branch. Wrike branches start with "w999999999", where 999999999 is the task ID')
      return

    webbrowser.open("https://www.wrike.com/open.htm?id=" + match.group(1))

def get_git_dir(current_file):
    if current_file is None:
      return None

    check_path = os.path.dirname(current_file)
    git_dir_path = None
    while (len(check_path) > 1) and (git_dir_path is None):
      dirs = [possible_dir for possible_dir in os.listdir(check_path) if os.path.isdir(os.path.join(check_path, possible_dir))]
      if '.git' in dirs:
        git_dir_path = check_path

      check_path = os.path.dirname(check_path)

    return git_dir_path

def output_from_command(*cmd):
  return subprocess.check_output(cmd, stderr = subprocess.STDOUT).decode("utf-8").strip()
