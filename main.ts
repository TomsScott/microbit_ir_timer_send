let Time2 = 0
let Lap = 0
basic.showLeds(`
    . . . . #
    . . . # .
    # . # . .
    . # . . .
    . . . . .
    `)
basic.pause(100)
basic.clearScreen()
servos.P2.setAngle(0)
radio.setGroup(193)
basic.forever(function () {
    if (Lap <= 10) {
        if (BitMaker.read_Din_value(GrovePort.P0) == 0) {
            Lap += 1
            radio.sendNumber(control.millis())
            Time2 = control.millis()
            basic.showNumber(Lap)
            servos.P2.setAngle(5)
            // Agitation de drapeau
            basic.pause(300)
            servos.P2.setAngle(0)
        }
    }
})
