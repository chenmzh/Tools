class PlasmidDilution:
    def __init__(self, PlasmidConcentration, StandardConcentration, CurrentVolume, **args):
        self.PlasmidConcentration = PlasmidConcentration
        self.StandardConcentration = StandardConcentration
        self.CurrentVolume = CurrentVolume
        self.FinalVolume = args.get("FinalVolume")

    def PlasmidDilutionTotally(self):
        # Add water to the current volume to meet the standard concentration
        AddWaterVolume = (self.PlasmidConcentration /
                          self.StandardConcentration - 1) * self.CurrentVolume
        FinalVolume = self.PlasmidConcentration / \
            self.StandardConcentration * self.CurrentVolume
        print(
            f"To dilute all the Plasmid with {self.PlasmidConcentration} unit concentration to {self.StandardConcentration} unit concentration, you need to add {AddWaterVolume} unit water, to get the {FinalVolume} unit final volume")
        return {"AddWaterVolume": AddWaterVolume, "FinalVolume": FinalVolume}

    def PlasmidDilutionToFixedVolume(self):
        # Want a specific final volume with specific plasmid concentration.
        TakeCurrentVolume = self.StandardConcentration * \
            self.FinalVolume / self.PlasmidConcentration
        AddWaterVolume = self.FinalVolume - TakeCurrentVolume
        print(
            f"To dilute the Plasmid with {self.PlasmidConcentration} unit concentration to {self.StandardConcentration} unit concentration with {self.FinalVolume} unit volume, you need to take {TakeCurrentVolume} unit volume of origin plasmid with {self.PlasmidConcentration} unit concentration out and add {AddWaterVolume} unit water")

        return {"AddWaterVolume": AddWaterVolume, "TakeCurrentVolume": TakeCurrentVolume}


PlasmidConcentration = int(input(
    "Please enter the plasmid concentration(with the unit of ng/ul, exclude unit)"))
StandardConcentration = int(input(
    "Please enter the final concentration you want (with the unit of ng/ul, exclude unit)"))

CurrentVolume = int(input(
    "Please enter the Volume of current plasmid (with the unit of ul, exclude unit)"))

FinalVolume = int(input(
    "Please enter the Final volume (with the unit of ul, exclude unit)"))

exp1 = PlasmidDilution(PlasmidConcentration=PlasmidConcentration,
                       StandardConcentration=StandardConcentration, CurrentVolume=CurrentVolume, FinalVolume=15)

PlasmidDilutionTotally = exp1.PlasmidDilutionTotally()
PlasmidDilutionToFixedVolume = exp1.PlasmidDilutionToFixedVolume()

print(PlasmidDilutionTotally)
print(PlasmidDilutionToFixedVolume)

# AddWaterVolume1 = exp1.PlasmidDilutionTotally()["AddWaterVolume"]
# FinalVolume = exp1.PlasmidDilutionTotally()["FinalVolume"]
# AddWaterVolume2 = exp1.PlasmidDilutionToFixedVolume()["AddWaterVolume"]
# TakeCurrentVolume = exp1.PlasmidDilutionToFixedVolume()["TakeCurrentVolume"]

# print(
#     f"To dilute all the Plasmid to target concentration, you need to add {AddWaterVolume1} unit water, to get the final volume of {FinalVolume} unit")
# print(
#     f"To dilute the Plasmid to target concentration with target concentration, you need to add {AddWaterVolume2} unit water")
# print(
#     f"To dilute the Plasmid to target concentration with target concentration, you need to take {TakeCurrentVolume} origin plasmid")
