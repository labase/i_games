from random import random
from braser import Braser
from circus.desafio_a import main as desafio0

DETAIL, DETAILURL = "dungeon_detail", "DungeonWall.jpg"
MONSTER, MONSTERURL = "monster", "monstersheets.png?"
DETILE = "dungeon_detile"
FIRE, FIREURL = "fire", "http://s19.postimg.org/z9iojs2c3/magicfire.png"
FSP = 1.5
MOVES = {0: (0, FSP*150), 90: (FSP*-150, 0), 180: (0, FSP*-150), 270: (FSP*150, 0)}
DIR = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


class Masmorra:
    _instance = None

    def __init__(self):
        self.gamer = Braser(800, 600)
        self.gamer.subscribe(self)
        self.game = self.gamer.game
        self.hero = Hero(self.gamer)
        self.sprite = Monster(self)
        self.monsters = self.magic = None
        self.monster_list = []

    @classmethod
    def created(cls):
        cls._instance = Masmorra()
        cls.created = lambda *_: Masmorra._instance
        return cls._instance

    def posiciona_monstro(self, m, x, y):
        self.monster_list.append((m, x, y))

    def preload(self):
        self.game.load.spritesheet(MONSTER, MONSTERURL, 64, 63, 16*12)
        self.game.load.spritesheet(DETILE, DETAILURL, 128, 128, 12)
        self.game.load.spritesheet(FIRE, FIREURL, 96, 96, 25)

    def create(self):
        self.game.physics.startSystem(self.gamer.PHASER.Physics.ARCADE)
        self.game.add.sprite(0, 0, DETILE)
        rotate = 0
        for i in range(6):
            for j in range(5):
                detail = self.game.add.sprite(64+i * 128, 64+j * 128, DETILE)
                detail.anchor.setTo(0.5, 0.5)
                detail.angle = rotate
                detail.frame = (6*j+i) % 12
                rotate += 90

        self.monsters = self.game.add.group()
        self.magic = self.game.add.group()
        self.monsters.enableBody = True
        self.magic.enableBody = True
        self.magic.checkWorldBounds = True
        self.magic.outOfBoundsKill = True

    def update(self):
        def kill(_, monster):
            monster.kill()

        def killall(magic, monster):
            magic.kill()
            monster.kill()

        self.game.physics.arcade.overlap(self.hero.sprite, self.sprite.sprite, kill, None, self)
        # self.game.physics.arcade.overlap(self.magic, self.monsters, killall, None, self)
        self.game.physics.arcade.overlap(self.magic, self.hero.sprite, killall, None, self)


class Monster:
    def __init__(self, masmorra):
        self.masmorra = masmorra
        masmorra.gamer.subscribe(self)
        self.game = masmorra.gamer.game
        self.sprite = self.cursors = self.moves = None
        self.direction = 0
        self.xy = (0, 0)

    def create(self):

        sprite = self.game.add.sprite(148, 148, MONSTER)
        sprite.animations.add('mon', [6 * 16 + 0, 6 * 16 + 1, 6 * 16 + 2, 6 * 16 + 3], 4, True)
        sprite.play('mon')
        self.game.physics.arcade.enable(sprite)
        sprite.body.setCircle(28)
        sprite.anchor.setTo(0.5, 0.5)
        sprite.body.collideWorldBounds = True
        sprite.body.bounce.setTo(1, 1)
        self.masmorra.monsters.add(sprite)
        self.sprite = sprite

    def preload(self):
        pass

    def update(self):
        def rd(play, dd):
            x, y = self.xy
            vx, vy = play.body.velocity.x, play.body.velocity.y
            if self.sprite.alive and int(random() + 0.02):
                self.direction = d = int(random()*8.0)
                x, y = player.body.position.x, player.body.position.y
                if vx or vy:
                    Magic(self.masmorra, x+30, y+30, vx, vy, (dd*45+180) % 360)
                x, y = self.xy = DIR[d]
            return x*150, y*150
        player = self.sprite
        player.angle = (self.direction*45+270) % 360
        player.body.velocity.x, player.body.velocity.y = rd(player, self.direction)
        player.animations.play('mon')


class Magic:
    def __init__(self, masmorra, x, y, vx, vy, d):
        self.masmorra, self.x, self.y, self.d = masmorra, x, y, d
        self.v = vx * 1.5, vy * 1.5
        masmorra.gamer.subscribe(self)
        self.game = masmorra.gamer.game
        self.sprite = self.cursors = self.moves = None
        self._create = self.create

    def kill(self):
        if not self.sprite.inWorld:
            print("kill")
            self.sprite.alive = False

    def create(self):

        sprite = self.game.add.sprite(self.x, self.y, FIRE)
        sprite.animations.add('fire', [10, 11, 12, 13, 14], 16, True)
        sprite.play('fire')
        sprite.scale.setTo(0.5, 0.5)
        self.game.physics.arcade.enable(sprite)
        sprite.body.setCircle(28)
        sprite.anchor.setTo(0.5, 0.5)
        self.masmorra.magic.add(sprite)
        self.sprite = sprite
        player = self.sprite
        player.body.velocity.x, player.body.velocity.y = self.v
        player.angle = self.d
        self._create = self.kill

    def preload(self):
        pass

    def update(self):
        self._create()


class Hero:
    def __init__(self, gamer):
        self.gamer = gamer
        self.gamer.subscribe(self)
        self.game = self.gamer.game
        self.sprite = self.cursors = self.moves = None

    def create(self):
        sprite = self.game.add.sprite(20, 148, MONSTER)
        sprite.animations.add('ani', [0, 1, 2, 3], 16, True)
        sprite.play('ani')
        self.game.physics.arcade.enable(sprite)
        sprite.body.setCircle(28)
        sprite.anchor.setTo(0.5, 0.5)
        sprite.body.collideWorldBounds = True
        self.sprite = sprite
        self.cursors = self.game.input.keyboard.createCursorKeys()

    def preload(self):
        pass

    def update(self):
        crs, player = self.cursors, self.sprite
        player.body.velocity.x, player.body.velocity.y = 0, 0
        player.animations.play('ani')
        moves = [(crs.left.isDown, 90, (-150, 0)), (crs.right.isDown, 270, (150, 0)),
                 (crs.up.isDown, 180, (0, -150)), (crs.down.isDown, 0, (0, 150))]

        stopped = True
        for move in moves:
            if move[0]:
                player.angle = move[1]
                player.body.velocity.x, player.body.velocity.y = move[2]
                stopped = False
        if stopped:
            player.animations.stop()


TOPO_ESQUERDA = "LS"
TOPO_DIREITA = "KO"
TOPO_CENTRO = "JN"
MEIO_ESQUERDA, CENTRO, MEIO_DIREITA = "IO", "FN", "IL"
FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA = "GS", "JS", "GL"

MASMORRA = [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO,
            MEIO_DIREITA], [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]]


def main(_=None):
    Masmorra()
DES = [main, desafio0, desafio0]


def posiciona_monstro(m, x, y):
    masmorra = Masmorra.created()
    masmorra.posiciona_monstro(m, x, y)


def circus(desafio=1, param=MASMORRA):
    from browser import doc
    # doc["pydiv"].html = PAGE0
    DES[desafio](param)

print(__name__)
if __name__ == "__main__":
    main()


PAGE0 = '''
  <div class="section" id="bem-vindos-ao-circo-voador-da-programacao-python">
<h1>Bem Vindos ao Circo Voador da Programação Python<a class="headerlink"
href="#bem-vindos-ao-circo-voador-da-programacao-python" title="Permalink to this headline">¶</a></h1>
<p>Aqui vamos ter uma introdução rápida de como programar jogos para Web usando Python.
Na verdade vamos usar o Brython que é o Python que funciona dentro de um navegador web como o Firefox.</p>
<img alt="http://s19.postimg.org/ufgi8eztf/PPFC.jpg" src="http://s19.postimg.org/ufgi8eztf/PPFC.jpg" />
</div>
<div class="section" id="sumario">
<h1>Sumário<a class="headerlink" href="#sumario" title="Permalink to this headline">¶</a></h1>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="inicia.html">Primeiro Cenário do Jogo</a></li>
<li class="toctree-l1"><a class="reference internal" href="desafio_a.html">Criando uma Câmara com Constantes</a></li>
<li class="toctree-l1"><a class="reference internal" href="desafio_b.html">Posicionando um Personagem com Inteiros</a>
</li>
</ul>
</div>
</div>
<div class="section" id="indices-e-tabelas">
<h1>Indices e Tabelas<a class="headerlink" href="#indices-e-tabelas" title="Permalink to this headline">¶</a></h1>
<ul class="simple">
<li><a class="reference internal" href="genindex.html"><em>Index</em></a></li>
<li><a class="reference internal" href="py-modindex.html"><em>Module Index</em></a></li>
<li><a class="reference internal" href="search.html"><em>Search Page</em></a></li>
</ul>
</div>
          </div>
        </div>
      </div>
    <div class="footer">
        &copy; Copyright 2016, Carlo E. T. Oliveira.
      Created using <a href="http://sphinx-doc.org/">Sphinx</a> 1.2.3.
    </div>
'''