#vypocty pro vyber pipet a labware
#loadPipettes
#load labware - priradit komponenty k labware
#AbPrep
#AbDispense
#AddSamples (+Controls)
#incubate
#lyse
#wash

#optimalizace common tube
#optimalizace poradi pipetovani pro setreni spicek

# tube wells

#tubes

class FCM_tube:
    components = {}
    location =

#PK
Tube_B = None
tube_L = {
    "CD8": 10,
    "CD16": 10,
    "CD56": 10,
    "CD19": 5,
    "CD4": 5,
    "CD3": 5,
    "CD45": 5
}
tube_DR = {
    "CD14": 10,
    "HLADR": 10,
    "IgG1FL3": 5,
    "IgG1FL4": 5,
    "CD3": 5,
    "CD45": 5
}

#LN
tube_B1
tube_B2
tube_B3


Tubes = (Tube_B, Tube_L, Tube_DR)
#Ab koktejl - co, odkud, kam, kolik - pripravit nazev = umisteni
#napr CD3 jiz musi mit prirazenu pozici, stejne tak Dest
def TubePrep(Tube=dict()):
    for Ab in Tube:
        P20S.transfer(Tube[Ab], Ab, TubeDest)
    return

p20s.pick_up_tip()
p20s.aspirate(5, CD45_well)
p20s.dispense(5, tube_L_well)
p20s.blow_out(tube_L.bottom(z=5))
p20s.drop_tip()

p20s.pick_up_tip()
p20s.aspirate(5, CD3_well)
p20s.dispense(5, tube_L_well)
p20s.blow_out(tube_L_well.bottom(z=5))
p20s.drop_tip()

p20s.pick_up_tip()
p20s.aspirate(5, CD4_well)
p20s.dispense(5, tube_L_well)
p20s.blow_out(tube_L_well.bottom(z=5))
p20s.drop_tip()

p20s.pick_up_tip()
p20s.aspirate(5, CD19_well)
p20s.dispense(5, tube_L_well)
p20s.blow_out(tube_L_well.bottom(z=5))
p20s.drop_tip()

p20s.pick_up_tip()
p20s.aspirate(10, CD56_well)
p20s.dispense(10, tube_L_well)
p20s.blow_out(tube_L_well.bottom(z=5))
p20s.drop_tip()

p20s.pick_up_tip()
p20s.aspirate(10, CD16_well)
p20s.dispense(10, tube_L_well)
p20s.blow_out(tube_L_well.bottom(z=5))
p20s.drop_tip()

p20s.pick_up_tip()
p20s.aspirate(10, CD8_well)
p20s.dispense(10, tube_L_well)
p20s.blow_out(tube_L_well.bottom(z=5))
p20s.drop_tip()