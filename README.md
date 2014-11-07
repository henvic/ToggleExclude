#ToggleExclude

[![Build Status](https://travis-ci.org/henvic/ToggleExclude.svg?branch=master)](https://travis-ci.org/henvic/ToggleExclude)

ToggleExclude is a plugin that adds conditional excluded file / folder list to Sublime Text 3, allowing you to browse / search code faster.

## Installing
Using Sublime Package Control

1. Open the Sublime Text command palette
2. Select Package Control: Install Package
3. Select ToggleExclude

## Usage
1. Open the Sublime Text command palette
2. Type ToggleExclude to see the available options

![clip](http://cl.ly/YPer/toggle-exclude.gif)

## Adding a shortcut

1. Open the Sublime Text menu
2. Select Preferences
3. Select Keys Bindings - User

Add a tuple where the command key is `toggle_exclude`.

```json
[{"keys": ["ctrl+shift+t"], "command": "toggle_exclude"}]
```

If you're not familiar with Sublime keymaps read [Customizing Sublime Text Key Bindings](http://docs.sublimetext.info/en/latest/customization/key_bindings.html) and [Key Bindings](http://docs.sublimetext.info/en/latest/reference/key_bindings.html)

## Contributing
In lieu of a formal styleguide, take care to maintain the existing coding style.

Pull requests with *common and safe* exclude patterns are welcome.

## Author
[Henrique Vicente](https://henvic.github.io/)
