def on_button_pressed_ab():
    if led.point(2, 4):
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
