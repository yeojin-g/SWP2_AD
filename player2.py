from player import Player


class Player2(Player):

    def __init__(self, beads, name, number):
        Player.__init__(self, beads)
        self.name = name
        self.number = number

    def messageOutput(self):
        note = f"""
                참가번호 {self.number}번 {self.name}님의 수비입니다.
                이번 게임에 걸 구슬의 개수를 입력하세요.
                """
        return note
