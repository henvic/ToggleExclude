# ToggleExclude.py
# https://github.com/henvic/ToggleExclude
#
# Written by Henrique Vicente
# License: MIT

import sublime
import sublime_plugin
from sublime import load_settings

SUBLIME_PREFERENCES = 'Preferences.sublime-settings'
FILE_EXCLUDE_PATTERNS = 'file_exclude_patterns'
FOLDER_EXCLUDE_PATTERNS = 'folder_exclude_patterns'

PLUGIN_SETTINGS = 'ToggleExclude.sublime-settings'
CONDITIONAL_FILE_EXCLUDE_PATTERNS = 'conditional_file_exclude_patterns'
CONDITIONAL_FOLDER_EXCLUDE_PATTERNS = 'conditional_folder_exclude_patterns'
ENABLED_KEY = 'enabled'


def update(files, folders):
    s_settings = sublime.load_settings(SUBLIME_PREFERENCES)

    s_settings.set(FILE_EXCLUDE_PATTERNS, files)
    s_settings.set(FOLDER_EXCLUDE_PATTERNS, folders)

    sublime.save_settings(SUBLIME_PREFERENCES)


def merge(ignored, cond):
    return list(set(ignored + cond))


def diff(ignored, cond):
    return list(set(ignored) - set(cond))


def update_state(enable=None):
    s_settings = sublime.load_settings(SUBLIME_PREFERENCES)
    p_settings = sublime.load_settings(PLUGIN_SETTINGS)

    state = bool(p_settings.get(ENABLED_KEY, False))

    if enable is not None:
        state = bool(enable)
        p_settings.set(ENABLED_KEY, state)
        sublime.save_settings(PLUGIN_SETTINGS)

    files = s_settings.get(FILE_EXCLUDE_PATTERNS, [])
    folders = s_settings.get(FOLDER_EXCLUDE_PATTERNS, [])

    cond_files = p_settings.get(CONDITIONAL_FILE_EXCLUDE_PATTERNS, [])
    cond_folders = p_settings.get(CONDITIONAL_FOLDER_EXCLUDE_PATTERNS, [])

    if state:
        return update(merge(files, cond_files), merge(folders, cond_folders))

    return update(diff(files, cond_files), diff(folders, cond_folders))


def toggle():
    p_settings = sublime.load_settings(PLUGIN_SETTINGS)

    state = bool(p_settings.get(ENABLED_KEY, False))

    update_state(not state)


def plugin_loaded():
    p_settings = sublime.load_settings(PLUGIN_SETTINGS)
    p_settings.add_on_change('toggleexclude-reload', update_state)


def plugin_unloaded():
    p_settings = sublime.load_settings(PLUGIN_SETTINGS)
    p_settings.clear_on_change('toggleexclude-reload')


class ToggleExcludeCommand(sublime_plugin.ApplicationCommand):
    def is_enabled(self, enable=None):
        state = bool(load_settings(PLUGIN_SETTINGS).get(ENABLED_KEY, False))

        return enable ^ state

    def run(self, enable=None):
        if enable is None:
            return toggle()

        update_state(enable)
