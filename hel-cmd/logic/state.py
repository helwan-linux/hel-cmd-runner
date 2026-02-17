class GameState:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.commands_executed = 0
        
        # تقليل السرعة البدائية من 5 لـ 2
        self.base_speed = 1 
        self.current_speed = 1
        self.max_speed = 5
        
        self.vision_boost = False
        self.active_bridge = False
        self.clear_screen = False
        self.target_lane_status = "active"
        self.game_over = False

    def update_score(self, points):
        self.score += points
        # رفع المستوى كل 1000 نقطة (عشان الصعوبة متزدش بسرعة)
        new_level = (self.score // 1000) + 1
        if new_level > self.level:
            self.level = new_level
            self.increase_difficulty()

    def increase_difficulty(self):
        if self.current_speed < self.max_speed:
            self.current_speed += 0.1 # زيادة طفيفة جداً
