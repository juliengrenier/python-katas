class Game(object):
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        score = 0
        self.roll_index = 0
        for frame in range(0, 10):
            score += self.next_frame_score()

        return score

    def next_frame_score(self):
        def _is_strike():
            return self.rolls[self.roll_index] == 10

        def add_frame(from_index):
            return self.rolls[from_index] + self.rolls[from_index + 1]

        score = 0
        if _is_strike():
            self.roll_index += 1
            score += 10 + add_frame(self.roll_index)

        else:
            frame_score = add_frame(self.roll_index)
            score += frame_score
            if frame_score == 10:
                score += self.rolls[self.roll_index + 2]

            self.roll_index += 2
        return score
