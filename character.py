class Character:
    def __init__(self):

        self.str = 10
        self.dex = 10
        self.con = 10
        self.int = 10
        self.wis = 10
        self.cha = 10

        self.classes = Classes()

class Classes:
    def __init__(self):
        self.barbarian  = 0
        self.bard       = 0
        self.cleric     = 0
        self.druid      = 0
        self.fighter    = 0
        self.monk       = 0
        self.paladin    = 0
        self.ranger     = 0
        self.rogue      = 0
        self.sorcerer   = 0
        self.warlock    = 0
        self.wizard     = 0