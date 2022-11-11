# Transfer beads to the samples on the Magnetic Module
# SWIFT
def transfer_beads(beads, source, dest, volume):
    p300m.flow_rate.aspirate = 75
    p300m.mix(10, 200, beads)

    for beads_dest in dest:
        p300m.pick_up_tip()
        p300m.flow_rate.aspirate = 10
        p300m.flow_rate.dispense = 10
        p300m.aspirate(volume, source)
        p300m.default_speed = 50
        p300m.move_to(beads_dest.top(-2))
        p300m.default_speed = 400
        p300m.dispense(volume, beads_dest.top(-5))
        p300m.blow_out()
        p300m.flow_rate.aspirate = 50
        p300m.flow_rate.dispense = 50
        p300m.mix(10, 50, beads_dest.top(-13.5))
        p300m.blow_out(beads_dest.top(-5))
        p300m.drop_tip()

# TZ
def transfer_beads(source, dest, volume):
    p300m.mix(10, 200, source.bottom(5))
    for beads_dest in dest:
        p300m.pick_up_tip()
        p300m.aspirate(volume, source, rate = 0.5)
        p300m.move_to(beads_dest.top(-2), speed = 100)
        p300m.dispense(volume, beads_dest.top(-5), rate = 0.5)
        p300m.blow_out()
        p300m.mix(10, 50, beads_dest.bottom(2), rate = 0.75)
        p300m.blow_out(beads_dest.top(-5))
        p300m.drop_tip()