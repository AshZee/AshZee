## Requirements : psutil,scrot,rofi,FuraCode_NerdFont(any),firefox
## Do chmod +x autostart.sh
## Enter your username in line 62

## Imports ##
import os
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.group import _Group
from typing import List  # noqa: F401 

## My defaults ##
mod = "mod4" # It is "alt"{change to mod4 if you want super as mod key}
browser = "brave"
myTerminal = "kitty"
# Bring to front if a floating window
def floating_to_front(qtile):
    w = qtile.current_window
    if w.floating:
        w.bring_to_front()

# Minimize all windows (show desktop)
@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()

## Key Bindings ##
keys = [
    Key([mod], "g", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "h", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "comma", lazy.next_screen(), desc="Move through the screen focus"),
    #Key(["mod1"], "Tab", lazy.function(floating_to_front), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "n", lazy.window.toggle_floating(), desc="Toggles floating"),
    # Grow windows. If current window is on the edge of screen and direction
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "control"], "i", lazy.layout.grow(), desc="Grow window"),
    Key([mod, "control"], "o", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod, "control"], "r", lazy.layout.reset(), desc="Reset"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(myTerminal), desc="Launch terminal"),
    Key([mod, "control"], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.screen.toggle_group(), desc="Toggle between layouts"),
    Key([mod], "quoteleft", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "Right", lazy.screen.next_group(), desc="Next group"),
    Key([mod], "Left", lazy.screen.prev_group(), desc="Previous group"),
    # Toggle Apps
    Key([mod, "control"], "s", lazy.spawn("/usr/bin/obsGit.sh")),
    Key([mod], "c", lazy.spawn(browser), desc="Launch_Browser"),
    Key([mod], "p", lazy.spawn('xournalpp'), desc="Launch xournal++"),
    Key([mod], "f", lazy.spawn("thunar"), desc="File manager"),
    Key([mod], "l", lazy.spawn("dm-tool switch-to-greeter"), desc="Lock_Screen"),
    Key([mod], "s", lazy.spawn("spotify"), desc="Launch spotify"),
    Key([mod], "space", lazy.spawn("/home/ash/.config/rofi/launchers/type-1/launcher.sh"), desc="Launch_rofi"),
    Key([mod], "n", lazy.spawn("notion-app"), desc="Launch Notion"),
    Key([mod], "o", lazy.spawn("obsidian"), desc="Launch Obsidian"),
    Key([mod], "v", lazy.spawn("code"), desc="launch vscode"),
    Key([mod], "m", lazy.spawn("thunderbird"), desc="launch mail client"),
   Key([mod], "x", lazy.spawn("xkill"), desc="launch xkill to force kill selected window"), 
    Key([mod], "Print", lazy.spawn("shutter -f -e")),
    Key([mod], "Period", lazy.spawn("rofimoji")),
   # Volume
    Key([], 'XF86AudioMUTE', lazy.spawn('volume.sh mute')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('volume.sh down')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('volume.sh up')),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='Play/Pause Player'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),
    # Brightness
    Key([], 'XF86MonBrightnessUp', lazy.spawn('brightness.sh up')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightness.sh down')),
    # ScreenShot
    Key([mod], "Super_L", lazy.spawn("scrot /home/ash/Screenshots/%Y-%m-%d-%T-screenshot.png")),
    Key(["control"], "Print", lazy.spawn("flameshot gui")),
    # Shutdown
    Key(["mod1", "control"], "z", lazy.spawn("shutdown now")),
    Key(["mod1", "control"], "s", lazy.spawn("systemctl suspend")),
    # Show desktop
    Key([mod], "d", minimize_all()),
]

## GroupBox ##
group_names = [("", {'layout': 'monadtall', 'label': ''}),
               ("", {'layout': 'monadtall', 'label': ''}),
               ("", {'layout': 'monadtall', 'label': ''}),
               ("", {'layout': 'monadtall', 'label': ''}),
               ("", {'layout': 'monadtall', 'label': ''}),
               ("󰎈", {'layout': 'monadtall', 'label': ''}),
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

## Mouse_callback functions

# Shutdown
def shutdown_now():
  qtile.cmd_spawn('shutdown now')
# Reboot
def reboot_now():
  qtile.cmd_spawn('reboot')
# Open_htop
def open_htop():
  qtile.cmd_spawn(myTerminal + ' -e htop')
# Speedtest.net
def speedtest():
  qtile.cmd_spawn(browser + 'www.speedtest.net')
# Brightness Up 
def brightup():
  qtile.cmd_spawn('brightnessctl set +5%')
# Brightness Down
def brightdown():
  qtile.cmd_spawn('brightnessctl set 5%-')
# Toggle On-Screen Keyboard
def toggleKb():
    #showKb = True
    #if(showKb):
     #   qtile.cmd_spawn('florence hide')
    #else:
     qtile.cmd_spawn('florence show')
# Fonts #

iconFontSize = 18
letterFontSize = 16
spacerFontSize = 20
padding = 5
spacerPadding = 5 

# On-Screen Keyboard#

showKb = False

# Colors ##

colors = [["#ff2738", "#ff2738", "#ff2738"], # red
          ["#ffffff", "#ffffff", "#ffffff"],
          ["#ffffff", "#ffffff", "#ffffff"], # text color
          ["#ffb480", "#ffb480", "#ffb480"], # tan
          ["#fce43c", "#fce43c", "#fce43c"], # yellow
          ["#42d6a4", "#42d6a4", "#42d6a4"], # turquoise
          ["#08cad1", "#08cad1", "#08cad1"], # sky blue
          ["#ffb135", "#ffb135", "#ffb135"], # yellow-orange
          ["#76787C", "#76787C", "#76787C"], # separators (|) light-gray
          ["#ff5722", "#ff5722", "#ff5722"], # red-orange
          ["#000000", "#000000", "#000000"],
          ["#00000000", "#00000000", "#00000000"]]

## Widget Defaults ##
widget_defaults = dict(
    background=colors[11]
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
              widget.Spacer(
                length = 10,
                background = colors[11],
                ),
              widget.TextBox(
                text = '󰣇',
                background = colors[11],
                foreground = "#76787C",
                fontsize = iconFontSize + 5,
                padding = padding,
                mouse_callbacks = {            
                                   'Button1': lazy.spawn('xinput enable "AT Translated Set 2 keyboard"'),
                                   'Button2': lazy.spawn('xinput disable "AT Translated Set 2 keyboard"'),
                }
                ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize/2,
                padding = spacerPadding/2
                ),
              widget.GroupBox(
                fontsize = iconFontSize,
                margin_x = 5,
                margin_y = 4,
                padding_y = 0,
                padding_x = padding,
                borderwidth = 4,
                active = "#76787C",
                inactive = colors[1],
                rounded = True,
                highlight_color = colors[11],
                highlight_method = "line",
                this_current_screen_border = colors[8],
                other_screen_border = colors[8],
                other_current_screen_border = colors[8],
                this_screen_border = colors[8],
                foreground = colors[2],
                center_aligned = True,
                disable_drag = True,
                background = colors[11]
                ),
              widget.Spacer(
                  background = colors[11],
                ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize,
                padding = spacerPadding
                ),
             # widget.TextBox(
             #   text='',
             #   background = colors[11],
             #   foreground = colors[2],
             #   fontsize = iconFontSize,
             #   mouse_callbacks = {'Button1': brightup, 'Button3': brightdown},
             #   padding = padding,
             #   ),
             # widget.Backlight(
             #   background = colors[11],
             #   foreground = colors[2],
             #   backlight_name = 'amdgpu_bl1',
             #   brightness_file = 'brightness',
             #   fontsize = letterFontSize 
             #   ),
             # widget.TextBox(
             #   text=' ',
             #   background = colors[11],
             #   foreground = colors[8],
             #   fontsize = spacerFontSize,
             #   padding = spacerPadding
             #   ),
             # widget.TextBox(
             #   text='',
             #   foreground = colors[2],
             #   background = colors[11],
             #   fontsize = iconFontSize,
             #   padding = padding,  
             #   ),
             # widget.PulseVolume(
             #   background = colors[11],
             #   foreground = colors[2],
             #   limit_max_volume = True,
             #   padding_x = padding,
             #   fontsize = letterFontSize, 
             #   ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize,
                padding = spacerPadding,
                ),
              widget.TextBox(
                text='',
                background = colors[11],
                foreground = colors[2],
                fontsize = iconFontSize,
                padding = padding,
                mouse_callbacks = {'Button1': open_htop},
                ),
              widget.Memory(
                background = colors[11],
                foreground = colors[2],
                measure_mem = 'G',
                format = '{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
                padding = padding,
                fontsize = letterFontSize,
                ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize,
                padding = spacerPadding,
                ),
              widget.BatteryIcon(
                background = colors[11],
                scale = 1.2,
                theme_path = '/usr/share/icons/kora/panel/24/',
                mouse_callbacks = {'Button1': lazy.spawn("/bin/toggle2.sh 2> /dev/null")},
                padding = 0,
                update_interval = 1
                ),
              widget.Battery(
                background = colors[11],
                battery = 0,
                foreground = colors[2],
                format = '{char}{percent:2.0%}',
                full_char = "100%",
                mouse_callbacks = {'Button1': lazy.spawn("/bin/toggle2.sh 2> /dev/null")},
                update_interval = 1,
                fontsize = letterFontSize,
                notify_below = 20,
                notification_timeout = 5,
                low_percentage = 0.20,
                discharge_char = '',
                charge_char = '󱐋',
                padding = padding/2,
                low_foreground = "#FFEE75"
                ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize,
                padding = spacerPadding,
                ),
              widget.CurrentLayout(
                background = colors[11],
                foreground = colors[2],
                fontsize = letterFontSize,
                max_chars = 20,
                fmt = "<span text_transform='capitalize' weight=\"bold\">{}</span>",
                padding = padding,
                ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize,
                padding = spacerPadding,
                ),
              widget.Clock(
                #format='%d-%m-%Y %a %I:%M:%S %p',
                format='%D %I:%M %p',
                foreground = colors[2],
                background = colors[11],
                fontsize = letterFontSize,
                padding = padding,
                ),
              widget.Sep(
                background = colors[11],
                foreground = colors[8],
                linewidth = 3,
                padding = spacerPadding * 0,
                ),
              widget.Systray(
                  background = colors[11],
                  icon_size = iconFontSize,
                  padding = 2*padding,
                ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize,
                padding = spacerPadding/2,
                ),
              widget.Sep(
                background = colors[11],
                foreground = colors[8],
                linewidth = 3,
                padding = spacerPadding * 0,
                ),
              widget.TextBox(
                text='󰌌',
                background = colors[11],
                foreground = colors[2],
                fontsize = iconFontSize,
                mouse_callbacks = {'Button1': toggleKb},
                padding = padding*2,
                ),
              widget.TextBox(
                text='󰝜',
                background = colors[11],
                foreground = colors[2],
                fontsize = iconFontSize,
                mouse_callbacks = {'Button1': lazy.layout.next()},
                padding = padding*2,
                ),
              widget.TextBox(
                text='󰍺',
                background = colors[11],
                foreground = colors[2],
                fontsize = iconFontSize,
                mouse_callbacks = {'Button1': lazy.spawn("/usr/bin/setup-ext-display.sh")},
                padding = padding*2,
                ),
              widget.Spacer(
                length = 10,
                background = colors[11],
                ),
            ],
            35,
            margin = [0,0,0,0],
            background = "#ff000000",
        ),
    ),
    Screen(
        top=bar.Bar(
            [
              widget.Spacer(
                length = 10,
                background = colors[11],
                ),
              widget.TextBox(
                text = '󰣇',
                background = colors[11],
                foreground = "#76787C",
                fontsize = iconFontSize + 5,
                padding = padding,
                mouse_callbacks = {            
                                   'Button1': lazy.spawn('xinput enable "AT Translated Set 2 keyboard"'),
                                   'Button2': lazy.spawn('xinput disable "AT Translated Set 2 keyboard"'),
                }
                ),
              widget.GroupBox(
                fontsize = iconFontSize,
                margin_x = 5,
                margin_y = 4,
                padding_y = 0,
                padding_x = padding,
                borderwidth = 4,
                active = "#76787C",
                inactive = colors[1],
                rounded = True,
                highlight_color = colors[11],
                highlight_method = "line",
                this_current_screen_border = colors[8],
                other_screen_border = colors[8],
                other_current_screen_border = colors[8],
                this_screen_border = colors[8],
                foreground = colors[2],
                center_aligned = True,
                disable_drag = True,
                background = colors[11]
                ),
              widget.Spacer(
                  background = colors[11],
                ),
              widget.TextBox(
                text='',
                background = colors[11],
                foreground = colors[2],
                fontsize = iconFontSize,
                padding = padding,
                ),
              widget.Wlan(
                background = colors[11],
                foreground = colors[2],
                fontsize = iconFontSize,
                format ='{essid}',
                mouse_callbacks = {'Button1': lazy.spawn("toggleNetwork.sh")},
                padding = padding,
                update_interval = 1,
                ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize,
                padding = spacerPadding
                ),
              widget.TextBox(
                text='',
                foreground = colors[2],
                background = colors[11],
                fontsize = iconFontSize,
                padding = padding,  
                ),
              widget.PulseVolume(
                background = colors[11],
                foreground = colors[2],
                limit_max_volume = True,
                padding_x = padding,
                fontsize = letterFontSize, 
                ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize,
                padding = spacerPadding,
                ),
              widget.TextBox(
                text='',
                background = colors[11],
                foreground = colors[2],
                fontsize = iconFontSize,
                padding = padding,
                mouse_callbacks = {'Button1': open_htop},
                ),
              widget.Memory(
                background = colors[11],
                foreground = colors[2],
                measure_mem = 'G',
                format = '{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
                padding = padding,
                fontsize = letterFontSize,
                ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize,
                padding = spacerPadding,
                ),
              widget.TextBox(
                text='',
                background = colors[11],
                foreground = colors[2],
                fontsize = iconFontSize,
                padding = padding,
                ),
              widget.CPU(
                background = colors[11],
                foreground = colors[2],
                format = '{freq_current}GHz {load_percent}%',
                padding = padding,
                fontsize = letterFontSize,
                ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize,
                padding = spacerPadding,
                ),
              widget.TextBox(
                text='󰁹',
                background = colors[11],
                foreground = colors[2],
                fontsize = iconFontSize,
                padding = padding,
                ),
              widget.Battery(
                background = colors[11],
                battery = 0,
                foreground = colors[2],
                format = '{char}{percent:2.0%}',
                full_char = "100%",
                update_interval = 1,
                fontsize = letterFontSize,
                notify_below = 20,
                notification_timeout = 5,
                low_percentage = 0.20,
                discharge_char = '',
                charge_char = '󱐋',
                padding = padding,
                ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize,
                padding = spacerPadding,
                ),
              widget.CurrentLayout(
                background = colors[11],
                foreground = colors[2],
                fontsize = letterFontSize,
                max_chars = 20,
                fmt = "<span text_transform='capitalize' weight=\"bold\">{}</span>",
                padding = padding,
                ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize,
                padding = spacerPadding,
                ),
              widget.Clock(
                #format='%d-%m-%Y %a %I:%M:%S %p',
                format='%D %I:%M %p',
                foreground = colors[2],
                background = colors[11],
                fontsize = letterFontSize,
                padding = padding,
                ),
              widget.Spacer(
                length = 10,
                background = colors[11],
                ),
            ],
            35,
            margin = [0,0,0,0],
        ),
    ),
    
]

## Layout Themes ##
layout_theme = {"border_width": 0,
                "margin": 10,
                "border_focus": "89bdc5",
                "border_normal": "586669"
                }

## Layouts ##

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod, "control" ], "Button1", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod, "control" ], "Button2", lazy.window.move_to_bottom()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
cursor_warp = False
floating_layout = layout.Floating(
        border_width=0,
        border_focus="#000000",
        border_normal="#000000",
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="discord"),  # gitk
        Match(wm_class="blueman-manager"),  # gitk
        Match(wm_class="Mail"),  # gitk
        Match(wm_class="thunderbird"),  # gitk
        Match(wm_class="com.vixalien.sticky"),  # gitk
        Match(wm_class="Thunar"),  # gitk
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="DBeaver"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
bring_front_click = False
# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

## Autostart ##
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

wmname = "QTILE" 
