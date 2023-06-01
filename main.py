def on_button_pressed_a():
    global Time
    Active = 0
    while Active == 1:
        Time += 0.1
        basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

Time2 = 0
Lap = 0
Time = 0
basic.show_leds("""
    . . . . #
        . . . # .
        # . # . .
        . # . . .
        . . . . .
""")
basic.pause(100)
basic.clear_screen()
servos.P2.set_angle(0)

def on_forever():
    global Lap, Time2, Time
    if Lap <= 10:
        if BitMaker.read_Din_value(GrovePort.P0) == 0:
            Lap += 1
            serial.write_line("Lap " + ("" + str(Lap)) + " finished in ")
            # Montrer le numero du tour avec le temps du tour
            serial.write_number(Time)
            serial.write_line("secondes")
            Time2 = Time + Time2
            serial.write_line("Lap " + ("" + str(Lap)) + " finished at ")
            # Montrer le numero du tour avec le temps totale
            serial.write_number(Time2)
            serial.write_line("secondes")
            Time = 0
            basic.show_number(Lap)
            servos.P2.set_angle(5)
            # Agitation de drapeau
            basic.pause(300)
            servos.P2.set_angle(0)
basic.forever(on_forever)
