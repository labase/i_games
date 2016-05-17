from braser import Braser

DETAIL, DETAILURL = "dungeon_detail", "DungeonWall.jpg"
MONSTER, MONSTERURL = "monster", "monstersheets.png?"
DETILE = "dungeon_detile"
TILEN = "ABCDEFGHIJKLMN"
DIREN = "NLSO"

TOPO_ESQUERDA = "LS"
TOPO_DIREITA = "KO"
TOPO_CENTRO = "JN"
MEIO_ESQUERDA, CENTRO, MEIO_DIREITA = "IO", "FN", "IL"
FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA = "GS", "JS", "GL"

MASMORRA = [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO,
            MEIO_DIREITA], [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]]

MASMORRA = ["LS JN HN HN JN KO".split(),
            "IO FN FN FN FN IL".split(),
            "IO FN FN FN FN IL".split(),
            "IO FN FN FN FN IL".split(),
            "GS JS HS HS JS GL".split()
            ]


class DesafioA:
    def __init__(self, masmorra):
        self.masmorra = masmorra
        self.gamer = Braser(768, 640)
        self.gamer.subscribe(self)
        self.game = self.gamer.game
        self.ph = self.gamer.PHASER

    def preload(self):
        # self.game.load.image(DETAIL, DETAILURL)

        self.game.stage.backgroundColor = "#FFFFFF"
        self.game.load.spritesheet(MONSTER, MONSTERURL, 64, 63, 16*12)
        self.game.load.spritesheet(DETILE, DETAILURL, 128, 128, 12)

    def create(self):
        rotate = 0
        style = dict(font="32px Arial", fill="#ff0044", align="center",
                     backgroundColor="#ffff00")

        for i in range(4):
            for j in range(3):
                detail = self.game.add.sprite(64+i * 132, 64+j * 132, DETILE)
                detail.anchor.setTo(0.5, 0.5)
                # detail.angle = rotate
                detail.frame = (4*j+i) % 12
                rotate += 90
                text = self.game.add.text(0, 0, "%s" % TILEN[4*j+i], style)
                text.anchor.set(0.5)
                text.x, text.y = 64+i * 132, 64+j * 132

        for i in range(4):
                detail = self.game.add.sprite(64+i * 132 + 200, 500, DETILE)
                detail.anchor.setTo(0.5, 0.5)
                detail.angle = rotate
                detail.frame = 0
                rotate += 90
                text = self.game.add.text(0, 0, "%s" % DIREN[i], style)
                text.anchor.set(0.5)
                text.x, text.y = 64+i * 132 + 200, 128*4

        for i, line in enumerate(self.masmorra):
            for j, cell in enumerate(line):
                detail = self.game.add.sprite(64+j * 128, 64+i * 128, DETILE)
                detail.anchor.setTo(0.5, 0.5)
                tile = cell  # MASMORRA[3*j+i]
                print(cell)
                detail.frame = ord(tile[0]) - ord("A")
                detail.angle = 90 * DIREN.index(tile[1])

    def update(self):
        pass


def main():
    DesafioA()
