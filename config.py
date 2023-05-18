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
browser = "google-chrome-stable"
myTerminal = "alacritty"

# Minimize all windows (show desktop)
@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()

## Key Bindings ##
keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key(["mod1"], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "n", lazy.window.toggle_floating(), desc="Toggles floating"),
    # Grow windows. If current window is on the edge of screen and direction
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
    Key([mod], "c", lazy.spawn(browser), desc="Launch_Browser"),
    Key([mod], "f", lazy.spawn("thunar"), desc="File manager"),
    Key([mod], "l", lazy.spawn("dm-tool lock"), desc="Lock_Screen"),
    Key([mod], "s", lazy.spawn("spotify"), desc="Launch spotify"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Launch_rofi"),
    Key([mod], "n", lazy.spawn("notion-app"), desc="Launch Notion"),
    Key([mod], "v", lazy.spawn("code"), desc="launch vscode"),
    Key([mod], "m", lazy.spawn("thunderbird"), desc="launch mail client"),
   Key([mod], "x", lazy.spawn("xkill"), desc="launch xkill to force kill selected window"), 
    Key([mod], "Print", lazy.spawn("shutter -f -e")),
    Key([mod], "Period", lazy.spawn("rofimoji")),
   # Volume
    Key([], 'XF86AudioMute', lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('pulseaudio-ctl down +5%')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pulseaudio-ctl up +5%')),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='Play/Pause Player'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),
    # Brightness
    Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl set +5%')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl set 5%-')),
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

# Fonts #

iconFontSize = 18
letterFontSize = 16
spacerFontSize = 40
padding = 7
spacerPadding = 10 
# Colors ##

colors = [["#ff2738", "#ff2738"],
          ["#ffffff", "#ffffff"],
          ["#ffffff", "#ffffff"], # text color
          ["#ffb480", "#ffb480"],
          ["#fce43c", "#fce43c"],  
          ["#42d6a4", "#42d6a4"],
          ["#08cad1", "#08cad1"],
          ["#ffb135", "#ffb135"], 
          #["#ffd65a", "#ffd65a"],
          ["#76787C", "#76787C"], # separators (|)
          ["#ff5722", "#ff5722"],
          ["#000000", "#000000"],
          ["#000000", "#000000"]]

## Widget Defaults ##
widget_defaults = dict(
    background=colors[0]
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
                text = '',
                background = colors[11],
                foreground = "#76787C",
                fontsize = iconFontSize + 5,
                padding = padding,
                mouse_callbacks = {            
                                   'Button1': minimize_all(),
                                   'Button2': lazy.spawn("shutdown now"),
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
                this_screen_border = colors [0],
                foreground = colors[2],
                center_aligned = True,
                disable_drag = True,
                background = colors[11]
                ),
              widget.Spacer(
                  background = colors[11],
                ),
             #widget.Mpris2(
             #   foreground=colors[2],
             #   background=colors[11],
             #   fontsize = letterFontSize,
             #   name="spotify",
             #   stopped_text="Nothing currently playing",
             #   stop_pause_text="{track}", width=100,
             #   display_metadata=["xesam:title", "xesam:artist"],
             #   objname="org.mpris.MediaPlayer2.spotify",
             #  ),
              widget.TextBox(
                text=' ',
                background = colors[11],
                foreground = colors[8],
                fontsize = spacerFontSize,
                padding = spacerPadding,
                ),
              widget.TextBox(
                text='',
                background = colors[11],
                foreground = colors[2],
                fontsize = iconFontSize,
                mouse_callbacks = {'Button1': brightup, 'Button3': brightdown},
                padding = padding,
                ),
              widget.Backlight(
                background = colors[11],
                foreground = colors[2],
                backlight_name = 'amdgpu_bl0',
                brightness_file = 'brightness',
                fontsize = letterFontSize 
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
                format = '{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
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
            # widget.TextBox(
            #   text='↓↑',
            #   foreground = colors[2],
            #   background = colors[11],
            #   fontsize = 12,
            #   padding = 0,
            #   mouse_callbacks={'Button3': speedtest}
            #   ),
            # widget.Net(
            #   background = colors[11],
            #   format = '{down} {up}',
            #   foreground = colors[2],
            #   fontsize = 12
            #   ),  
            # widget.TextBox(
            #   text='|',
            #   background = colors[11],
            #   foreground = colors[8],
            #   fontsize = 35,
            #   padding = 2
            #   ),
              widget.TextBox(
                text='',
                background = colors[11],
                foreground = colors[2],
                fontsize = iconFontSize,
                padding = padding,
                ),
              widget.Battery(
                background = colors[11],
                foreground = colors[2],
                format = '{char}{percent:2.0%}',
                full_char = "100%",
                update_interval = 1,
                fontsize = letterFontSize,
                notify_below = 20,
                low_percentage = 0.2,
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
                format='%d-%m-%Y %a %I:%M:%S %p',
                foreground = colors[2],
                background = colors[11],
                fontsize = letterFontSize,
                padding = padding,
                ),
              widget.Spacer(
                length = 10,
                background = colors[11],
                ),
            # widget.Spacer(
             #   length = 6,
              #  background = colors[11],
               # ),                
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
    layout.Floating(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Matrix(**layout_theme),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod, "control" ], "Button1", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

## Autostart ##
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

wmname = "QTILE" 
