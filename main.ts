input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    if (led.point(2, 4)) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.No)
    }
    
})
