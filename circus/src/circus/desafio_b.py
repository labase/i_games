# from ..braser import Braser
from random import shuffle

INTERVAL = 132

DETAIL, DETAILURL = "dungeon_detail", "http://s19.postimg.org/uacqyqsib/Dungeon_Detail.jpg"
MONSTER, MONSTERURL = "monster", "http://s19.postimg.org/ldsev0v6b/monstersheets.png"
FIRE, FIREURL = "fire", "http://s19.postimg.org/z9iojs2c3/magicfire.png"
AZTEC = "Ocuil Itotia Coyotl Icnoy Tochmi Patia Coaih Nahuap " \
        "Nehual Quahtli Nochtli Tlilpot Ilhicac Mezcotl Mazan Quezoh " \
        "Necuatl Xipil Matlal Eloxo Mahui Yolnen Tlacatl Huitzil " \
        "Coatl Cipac Tecotl Moyol Tonalco Potzin Ilhui Patonal " \
        "Iuitl Itzotl Xiuh Eleuia Coatzal Ichhual Xilopi Xitlal".split()


class DesafioA:
    def __init__(self, gamer):
        self.gamer = gamer
        self.gamer.subscribe(self)
        self.game = self.gamer.game
        self.tiler = AZTEC[:]
        shuffle(self.tiler)

    def preload(self):
        # self.game.load.image(DETAIL, DETAILURL)

        self.game.stage.backgroundColor = "#FFFFFF"
        self.game.load.spritesheet(MONSTER, MONSTERURL, 64, 63, 16 * 12)
        self.game.load.spritesheet(DETAIL, DETAILURL, 128, 128, 40)
        self.game.load.spritesheet(FIRE, FIREURL, 96, 96, 25)

    def create(self):
        rotate = 0
        style = dict(font="24px Arial", fill="#ff0044", align="center",
                     backgroundColor="#ffff00")

        for i in range(8):
            for j in range(5):
                detail = self.game.add.sprite(64 + i * INTERVAL, 64 + j * INTERVAL, DETAIL)
                detail.anchor.setTo(0.5, 0.5)
                #detail.scale.setTo(0.5, 0.5)
                # detail.angle = rotate
                detail.frame = (8 * j + i) #% 40
                rotate += 90
                text = self.game.add.text(0, 0, "%s" % AZTEC[8 * j + i], style)
                text.anchor.set(0.5)
                text.x, text.y = 32 + i * INTERVAL, 16 + j * INTERVAL

        for i in range(0):
            detail = self.game.add.sprite(64 + i * INTERVAL + 200, 500, DETAIL)
            detail.anchor.setTo(0.5, 0.5)
            detail.angle = rotate
            detail.frame = 0
            rotate += 90
            text = self.game.add.text(0, 0, "%s" % DIREN[i], style)
            text.anchor.set(0.5)
            text.x, text.y = 64 + i * INTERVAL + 200, 128 * 4

        tile = self.tiler[:]
        shuffle(tile)
        tile = tile[0:16]
        print(tile)

        for i in range(0):
            for j in range(4):
                detail = self.game.add.sprite(64 + i * 128//2, 328 + 64 + j * 128//2, DETAIL)
                detail.scale.setTo(0.5, 0.5)
                detail.anchor.setTo(0.5, 0.5)
                detail.frame = self.tiler.index(tile[4*i+j])
                detail.angle = (90 * detail.frame) % 360

    def update(self):
        pass


def main(gamer=None):
    DesafioA(gamer)


def test():
    from braser import Braser
    gamer = Braser(1100, 800)
    main(gamer)
