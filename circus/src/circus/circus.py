from random import random
from braser import Braser
from circus.desafio_a import main as desafio0

DETAIL, DETAILURL = "dungeon_detail", "DungeonWall.jpg"
MONSTER, MONSTERURL = "monster", "monstersheets.png?"
DETILE = "dungeon_detile"
FIRE, FIREURL = "fire", "http://s19.postimg.org/z9iojs2c3/magicfire.png"
MOVES = {0: (0, 150), 90: (-150, 0), 180: (0, -150), 270: (150, 0)}


class Masmorra:
    _instance = None

    def __init__(self):
        self.gamer = Braser(800, 600)
        self.gamer.subscribe(self)
        self.game = self.gamer.game
        self.ph = self.gamer.PHASER
        self.hero = Hero(self.gamer)
        self.monster = Monster(self)
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
        # self.game.load.image(DETAIL, DETAILURL)
        self.game.load.spritesheet(MONSTER, MONSTERURL, 64, 63, 16*12)
        self.game.load.spritesheet(DETILE, DETAILURL, 128, 128, 12)
        self.game.load.spritesheet(FIRE, FIREURL, 96, 96, 25)

    def create(self):
        self.game.physics.startSystem(self.ph.Physics.ARCADE)
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

        self.game.physics.arcade.overlap(self.hero.monster, self.monster.monster, kill, None, self)
        self.game.physics.arcade.overlap(self.magic, self.monsters, killall, None, self)
        self.game.physics.arcade.overlap(self.magic, self.hero.monster, killall, None, self)


class Monster:
    def __init__(self, masmorra):
        self.masmorra = masmorra
        masmorra.gamer.subscribe(self)
        self.game = masmorra.gamer.game
        self.monster = self.cursors = self.moves = None
        self.direction = [0] * 4

    def create(self):

        sprite = self.game.add.sprite(148, 148, MONSTER)
        # sprite.animations.add('mon', [7*16+0, 7*16+1, 7*16+2, 7*16+3, 7*16+16 + 0,
        #                               7*16+16 + 1, 7*16+16 + 2, 7*16+16 + 3], 4, True)
        sprite.animations.add('mon', [6 * 16 + 0, 6 * 16 + 1, 6 * 16 + 2, 6 * 16 + 3], 4, True)
        sprite.play('mon')
        self.game.physics.arcade.enable(sprite)

        # self.game.physics.p2.enable(sprite, False)
        sprite.body.setCircle(28)
        sprite.anchor.setTo(0.5, 0.5)
        sprite.body.collideWorldBounds = True
        # sprite.body.fixedRotation = True
        self.masmorra.monsters.add(sprite)
        self.monster = sprite

    def preload(self):
        pass

    def update(self):
        def rd(d):
            self.direction[d] = abs(self.direction[d]-1) if int(random() + 0.005) else self.direction[d]
            return self.direction[d]
        player = self.monster
        player.body.velocity.x, player.body.velocity.y = 0, 0
        player.animations.play('mon')
        moves = [(rd(0), 90, -150, 0), (rd(1), 270, 150, 0),
                 (rd(2), 180, 0, -150), (rd(3), 0, 0, 150)]

        stopped = True
        for move in moves:
            if move[0]:
                player.angle = move[1]
                player.body.velocity.x += move[2]
                player.body.velocity.y += move[3]
                stopped = False
        if stopped:
            player.animations.stop()


class Magic:
    def __init__(self, masmorra, x, y, d):
        self.masmorra, self.x, self.y, self.d = masmorra, x, y, d
        masmorra.gamer.subscribe(self)
        self.game = masmorra.gamer.game
        self.monster = self.cursors = self.moves = None
        self.direction = [0] * 4

    def create(self):

        sprite = self.game.add.sprite(self.x, self.y, FIRE)
        sprite.animations.add('fire', [10, 11, 12, 13, 14], 4, True)
        sprite.play('fire')
        self.game.physics.arcade.enable(sprite)

        # self.game.physics.p2.enable(sprite, False)
        sprite.body.setCircle(28)
        sprite.anchor.setTo(0.5, 0.5)
        sprite.body.collideWorldBounds = True
        # sprite.body.fixedRotation = True
        self.masmorra.magic.add(sprite)
        self.monster = sprite
        player = self.monster
        player.body.velocity.x, player.body.velocity.y = MOVES[self.d]
        player.angle = self.d

    def preload(self):
        pass

    def update(self):
        pass


class Hero:
    def __init__(self, gamer):
        self.gamer = gamer
        self.gamer.subscribe(self)
        self.game = self.gamer.game
        self.ph = self.gamer.PHASER
        self.monster = self.cursors = self.moves = None

    def create(self):
        # self.game.physics.startSystem(self.ph.Physics.ARCADE)
        sprite = self.game.add.sprite(20, 148, MONSTER)
        # sprite.animations.add('ani', [0, 1, 2, 3, 16+0, 16+1, 16+2, 16+3], 2, True)
        sprite.animations.add('ani', [0, 1, 2, 3], 16, True)
        sprite.play('ani')
        self.game.physics.arcade.enable(sprite)

        # self.game.physics.p2.enable(sprite, False)
        sprite.body.setCircle(28)
        sprite.anchor.setTo(0.5, 0.5)
        sprite.body.collideWorldBounds = True
        # sprite.body.fixedRotation = True
        self.monster = sprite
        self.cursors = crs = self.game.input.keyboard.createCursorKeys()

    def preload(self):
        pass

    def update(self):
        crs, player = self.cursors, self.monster

        #  Collide the player and the stars with the platforms
        # self.game.physics.arcade.collide(self.player, self.platforms)

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


class Main:
    def __init__(self, game, phaser):
        self.ph = phaser
        self.game = game(800, 600, phaser.AUTO, 'flying-circus',
                         {"preload": self.preload, "create": self.create, "update": self.update})
        self.player = self.platforms = self.cursors = self.stars = self.scoreText = None
        self.score = 0
        pass

    def preload(self, *_):
        self.game.load.image('image-url', 'assets/sky.png')

        self.game.load.image('ground', 'assets/platform.png')
        self.game.load.image('star', 'assets/star.png')
        self.game.load.spritesheet('dude', 'assets/dude.png', 32, 48)

    def create(self, *_):
        self.game.physics.startSystem(self.ph.Physics.ARCADE)
        self.game.add.sprite(0, 0, 'image-url')
        self.game.add.sprite(0, 0, 'star')
        platforms = self.game.add.group()
        platforms.enableBody = True
        ground = platforms.create(0, self.game.world.height - 64, 'ground')
        ground.scale.setTo(2, 2)
        ground.body.immovable = True
        ledge = platforms.create(400, 400, 'ground')

        ledge.body.immovable = True

        ledge = platforms.create(-150, 250, 'ground')

        ledge.body.immovable = True

        player = self.game.add.sprite(32, self.game.world.height - 150, 'dude')

        #  We need to enable physics on the player
        self.game.physics.arcade.enable(player)

        #  Player physics properties. Give the little guy a slight bounce.
        player.body.bounce.y = 0.2
        player.body.gravity.y = 300
        player.body.collideWorldBounds = True

        #  Our two animations, walking left and right.
        player.animations.add('left', [0, 1, 2, 3], 10, True)
        player.animations.add('right', [5, 6, 7, 8], 10, True)

        self.cursors = self.game.input.keyboard.createCursorKeys()
        stars = self.game.add.group()

        stars.enableBody = True
        # return

        #  Here we'll create 12 of them evenly spaced apart
        for i in range(12):

            #  Create a star inside of the 'stars' group
            star = stars.create(i * 70, 0, 'star')

            #  Let gravity do its thing
            star.body.gravity.y = 6

            #  This just gives each star a slightly random bounce value
            star.body.bounce.y = 0.7 + random() * 0.2
        self.scoreText = self.game.add.text(16, 16, 'score: 0', dict(fontSize='32px', fill='#000'))
        self.player, self.platforms, self.stars = player, platforms, stars

    def update(self, *_):
        cursors, player, platforms, stars = self.cursors, self.player, self.platforms, self.stars

        #  Collide the player and the stars with the platforms
        self.game.physics.arcade.collide(self.player, self.platforms)

        player.body.velocity.x = 0

        if cursors.left.isDown:
            #  Move to the left
            player.body.velocity.x = -150

            player.animations.play('left')
        elif cursors.right.isDown:
            #  Move to the right
            player.body.velocity.x = 150

            player.animations.play('right')
        else:
            #  Stand still
            player.animations.stop()

            player.frame = 4

        #  Allow the player to jump if they are touching the ground.
        if cursors.up.isDown and player.body.touching.down:
            player.body.velocity.y = -350

        def collectstar(_, star):
            # Removes the star from the screen
            star.kill()
            self.score += 10
            self.scoreText.text = 'Score: %d' % self.score

        self.game.physics.arcade.collide(stars, platforms)

        self.game.physics.arcade.overlap(player, stars, collectstar, None, self)


TOPO_ESQUERDA = "LS"
TOPO_DIREITA = "KO"
TOPO_CENTRO = "JN"
MEIO_ESQUERDA, CENTRO, MEIO_DIREITA = "IO", "FN", "IL"
FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA = "GS", "JS", "GL"

MASMORRA = [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO,
            MEIO_DIREITA], [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]]


def main():
    Masmorra()
    # Main(Game, auto)
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
<h1>Bem Vindos ao Circo Voador da Programação Python<a class="headerlink" href="#bem-vindos-ao-circo-voador-da-programacao-python" title="Permalink to this headline">¶</a></h1>
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
<li class="toctree-l1"><a class="reference internal" href="desafio_b.html">Posicionando um Personagem com Inteiros</a></li>
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