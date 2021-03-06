# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
        background Image("gui/ui/MainMenu.png")

    # The main menu buttons.
        xalign 0.0
        yalign 0.0

        imagebutton auto "gui/mm/start_%s.png" xpos 1391 ypos 40 focus_mask True action Start()
        imagebutton auto "gui/mm/load_%s.png" xpos 1391 ypos 215 focus_mask True action ShowMenu("load")
        imagebutton auto "gui/mm/prefs_%s.png" xpos 1391 ypos 390 focus_mask True action ShowMenu('preferences')
        imagebutton auto "gui/mm/help_%s.png" xpos 1391 ypos 565 focus_mask True action Help()
        imagebutton auto "gui/mm/quit_%s.png" xpos 1391 ypos 740 focus_mask True action Quit(confirm=True)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.


    # The various buttons.

    hbox:
        style_group "navigation"

        xalign 0
        yalign 1.0

        imagebutton auto "gui/nv/rtn_%s.png" xpos 1494 ypos -891 focus_mask True action Return()
        imagebutton auto "gui/nv/prefs_%s.png" xpos 1193 ypos -763 focus_mask True action ShowMenu('preferences')
        imagebutton auto "gui/nv/save_%s.png" xpos 892 ypos -635 focus_mask True action ShowMenu('save')
        imagebutton auto "gui/nv/load_%s.png" xpos 591 ypos -507 focus_mask True action ShowMenu("load")
        imagebutton auto "gui/nv/mm_%s.png" xpos 290 ypos -379 focus_mask True action MainMenu()
        imagebutton auto "gui/nv/help_%s.png" xpos -11 ypos -251 focus_mask True action Help()
        imagebutton auto "gui/nv/quit_%s.png" xpos -312 ypos -123 focus_mask True action Quit(confirm=True)



init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    add "gui/ui/SaveScreen.png" xalign 1.0 yalign 1.0

        # The buttons at the top allow the user to pick a
        # page of files.
    
    $ firstNum = 1379

    imagebutton auto "gui/sv/auto_%s.png" xpos 735 ypos 20 focus_mask True action FilePage("auto")
    imagebutton auto "gui/sv/quick_%s.png" xpos 896 ypos 20 focus_mask True action FilePage("quick")
    imagebutton auto "gui/sv/prev_%s.png" xpos 1057 ypos 20 focus_mask True action FilePagePrevious()
    imagebutton auto "gui/sv/next_%s.png" xpos 1218 ypos 20 focus_mask True action FilePageNext()

    for i in range(1, 10):
        imagebutton auto "gui/sv/" + str(i) +"_%s.png":
            xpos (int(firstNum)+((i-1)*59)) 
            ypos 20 
            focus_mask True 
            action FilePage(i)

    $ columns = 2
    $ rows = 6

        # Display a grid of file slots.
    grid columns rows:
        xalign 0
        yalign 0
        xsize 1760
        ysize 750
        xpos 68
        ypos 139

        xfill True

        style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
        for i in range(1, columns * rows + 1):

                # Each file slot is a button.
            button:
                action FileAction(i)

                xfill True

                xalign 0
                yalign 0
                xsize 673
                ysize 102
                xpos ((i*15)*(i%2))+((45+(i*15))*((i+1)%2))
                ypos (i-((i+1)%2))*14

                background Frame("gui/sv/SlotBG_idle.png", 4, 4, 4, 4)
                idle_background Frame("gui/sv/SlotBG_hover.png", 4, 4, 4, 4)
                hover_background Frame("gui/sv/SlotBG_idle.png", 4, 4, 4, 4)

                has hbox

                add FileScreenshot(i)

                $ file_name = FileSlotName(i, columns * rows)
                $ file_time = FileTime(i, empty=_("Empty Slot."))
                $ save_name = FileSaveName(i)

                text "[file_name]. [file_time!t]\n[save_name!t]"

                key "save_delete" action FileDelete(i)

### Menu Buttons For Save Screen ###

    imagebutton auto "gui/nv/mm_%s.png" xpos 1260 ypos 969 focus_mask True action MainMenu()
    imagebutton auto "gui/nv/rtn_%s.png" xpos 1571 ypos 969 focus_mask True action Return()



screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use file_picker

    hbox:
        xpos 20
        ypos 10
        
        text "SAVE GAME" font "LSANS.ttf" size 64 color "000000ff"

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use file_picker

    hbox:
        xpos 20
        ypos 10
        
        text "LOAD GAME" font "LSANS.ttf" size 64 color "000000ff"

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu
    
    add "gui/ui/Preferences Screen.png" xalign 1.0 yalign 1.0
    
# Include the navigation.
    use navigation

    viewport id "pref_vp":
        draggable True
        mousewheel True
        xalign 0
        yalign 0
        xsize 1050
        ysize 828
        xpos 125
        ypos 125
        
        
        grid 1 1:
            style_group "prefs"
            xfill True


            vbox:
                spacing 20
                frame:
                    style_group "pref"

                    hbox:
                        yalign 0.5
                        text "Display" 
                    hbox:
                        xpos 475
                        yalign 0.5
                        textbutton _("Window"):

                            action Preference("display", "window")

                        textbutton _("Fullscreen"):

                            action Preference("display", "fullscreen")
                frame:
                    style_group "pref"

                    hbox:
                        yalign 0.5
                        text "Transitions"
                    hbox:
                        xpos 475
                        yalign 0.5
                        textbutton _("All") action Preference("transitions", "all")
                        textbutton _("None") action Preference("transitions", "none")

                frame:
                    style_group "pref"

                    hbox:
                        yalign 0.5
                        text "Text Speed"
                    hbox:
                        xpos 500
                        yalign 0.5
                        bar value Preference("text speed")
    
                frame:
                    style_group "pref"
 
                    hbox:
                        xpos 475
                        yalign 0.5    
                        textbutton _("Joystick...") action Preference("joystick")
    
    
                frame:
                    style_group "pref"

                    hbox:
                        yalign 0.5
                        text "Skip"
                    hbox:
                        xpos 475
                        yalign 0.5
                        textbutton _("Seen Messages") action Preference("skip", "seen")
                        textbutton _("All Messages") action Preference("skip", "all")

                frame:
                    style_group "pref"

                    hbox:
                        xpos 475
                        yalign 0.5    
                        textbutton _("Begin Skipping") action Skip()
    
                frame:
                    style_group "pref"

                    hbox:
                        yalign 0.5
                        text "After Choices"
                    hbox:
                        xpos 475
                        yalign 0.5
                        textbutton _("Stop Skipping") action Preference("after choices", "stop")
                        textbutton _("Keep Skipping") action Preference("after choices", "skip")
    
                frame:
                    style_group "pref"

                    hbox:
                        yalign 0.5
                        text "Auto-Forward Time"
                        bar value Preference("auto-forward time")
                        textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

                frame:
                    style_group "pref"

                    hbox:
                        yalign 0.5
                        text "Music Volume"
                        bar value Preference("music volume")
    
                frame:
                    style_group "pref"
                    has vbox
                    hbox:
                        yalign 0.5
                        text "Sound Volume"
                    hbox:
                        xpos 475
                        yalign 0.5
                        bar value Preference("sound volume")
    
                        if config.sample_sound:
                            textbutton _("Test"):
                                action Play("sound", config.sample_sound)
                                style "soundtest_button"
    
                if config.has_voice:
                    frame:
                        style_group "pref"

                        hbox:
                            yalign 0.5
                            text "Voice Volume"
                        hbox:
                            xpos 475
                            yalign 0.5
                            bar value Preference("voice volume")
    
                            textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                            if config.sample_voice:
                                textbutton _("Test"):
                                    action Play("voice", config.sample_voice)
                                    style "soundtest_button"

    vbar:
        value YScrollValue("pref_vp")
        
        left_bar Frame("gui/ui/ScrollBarExternal.png", 2, 2, 2, 2)
        right_bar Frame("gui/ui/ScrollBarExternal.png", 2, 2, 2, 2)
        
        left_gutter 0
        right_gutter 0
        bottom_gutter 0
        top_gutter 0
        
        thumb_offset 0
        
        thumb Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)
        thumb_shadow Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)
        
        bar_resizing False
        
        xsize 10
        ysize 878
        xpos 101
        ypos 100


init -2:
    style pref_frame:

        background Frame("gui/ui/FrameBox.png", 2, 2, 2, 2)
        xfill True
        ysize 100
        xsize 1050


    style pref_vbox:
        xfill True

    style pref_lable:

        yalign 0.5

    style pref_text:

        size 32
        color "000000ff" 
        yanchor 0.5
        yalign 0.5 

    style pref_button:
        xfill True
        background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        idle_background Frame("gui/ui/FrameBox.png", 4, 4, 4, 4)
        hover_background Frame("gui/ui/FrameBox_hover.png", 4, 4, 4, 4)
        xalign 0

        ysize 50
        xsize 250
        left_margin 25

    style pref_slider:
    
        left_bar Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)
        right_bar Frame("gui/ui/ScrollBarExternal.png", 2, 2, 2, 2)
        
        left_gutter 0
        right_gutter 0
        bottom_gutter 0
        top_gutter 0
        
        thumb_offset 0
        
        thumb Image("gui/ui/SliderThing.png")
        thumb_shadow Frame("gui/ui/ScrollBarInternal.png", 2, 2, 2, 2)

        xsize 475
        
    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"
        
    frame:
        
        background Image("gui/ui/YesNoFrame.png")
        
        xsize 960
        ysize 360
        xpos 490
        ypos 180
            
        label _(message):
            xalign 0.5
            yalign 0.25
            text_size 38

        hbox:

            xalign 0.5
            ypos 252
            spacing 100

            imagebutton auto "gui/yn/yes_%s.png" focus_mask True action yes_action
            imagebutton auto "gui/yn/no_%s.png" focus_mask True action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5 


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        xalign 0
        yalign 1.0
        
        imagebutton auto "gui/qm/prefs_%s.png" xpos 1675 ypos -128 focus_mask True action ShowMenu('preferences')
    hbox: 
        xalign 0
        yalign 1.0

        imagebutton auto "gui/qm/save_%s.png" xpos 1805 ypos -198 focus_mask True action ShowMenu('save')
        imagebutton auto "gui/qm/load_%s.png" xpos 1580 ypos -198 focus_mask True action ShowMenu('load')
    hbox:
        xalign 0
        yalign 1.0

        imagebutton auto "gui/qm/quit_%s.png" xpos 1700 ypos -58 focus_mask True action Quit(confirm=True)

        

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

