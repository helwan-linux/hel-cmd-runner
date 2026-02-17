class CommandActions:
    def __init__(self, game_state):
        self.state = game_state
        self.commands = {
            "ls": self.scan_area,
            "cd ..": self.jump_back,
            "hpm i": self.install_bridge,
            "clear": self.wipe_obstacles,
            "hel-netfix": self.repair_lane
        }

    def execute(self, cmd_string):
        if cmd_string in self.commands:
            return self.commands[cmd_string]()
        return False

    def scan_area(self):
        # كشف العقبات البعيدة بتغيير شفافيتها أو لونها
        self.state.vision_boost = True
        return "Area Scanned"

    def jump_back(self):
        # إرجاع اللاعب للخلف لتجنب اصطدام وشيك
        self.state.runner_position -= 50
        return "Jumped Back"

    def install_bridge(self):
        # بناء جسر فوق فجوة في المسار
        self.state.active_bridge = True
        return "Bridge Installed"

    def wipe_obstacles(self):
        # تدمير كل العقبات البسيطة الموجودة على الشاشة حالياً
        self.state.clear_screen = True
        return "Screen Cleared"

    def repair_lane(self):
        # إصلاح مسار معطل (Disabled Lane)
        self.state.target_lane_status = "active"
        return "Lane Repaired"
