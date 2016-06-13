from random import random, shuffle
from braser import Braser
# noinspection PyUnresolvedReferences
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
        self.hero = Hero(self)
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
        self.sprite = None
        self.direction = 0
        self.first = True

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
        player = self.sprite
        player.angle = (self.direction*45+270) % 360
        if self.sprite.alive and int(random() + 0.02) or self.first:
            player.body.velocity.x, player.body.velocity.y = self.redirect(player, self.direction)
        player.animations.play('mon')

    def redirect(self, play, dd):
        self.first = False
        vx, vy = DIR[dd]
        self.direction = d = int(random() * 8.0)
        x, y = play.body.position.x, play.body.position.y
        if vx or vy:
            Magic(self.masmorra, x + 30, y + 30, vx * 150, vy * 150, (dd * 45 + 180) % 360)
        x, y = DIR[d]
        return x * 150, y * 150


class Magic:
    def __init__(self, masmorra, x, y, vx, vy, d):
        self.masmorra, self.x, self.y, self.d = masmorra, x, y, d
        self.v = vx * 1.5, vy * 1.5
        masmorra.gamer.subscribe(self)
        self.game = masmorra.gamer.game
        self.sprite = None
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
        self.gamer = gamer.gamer
        self.gamer.subscribe(self)
        self.game = self.gamer.game
        self.sprite = self.cursors = None

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
ORDERED_KEYS = [['Coycol', 'Cauha', 'Tetlah'],
                ['Huatlya', 'Zitllo', 'Micpe'],
                ['Nenea', 'Cahuitz', 'Pallotl']]
PLAIN_KEYS = ['Coycol', 'Cauha', 'Tetlah'] +\
                ['Huatlya', 'Zitllo', 'Micpe'] +\
                ['Nenea', 'Cahuitz', 'Pallotl']
SHUFFLE_KEYS = PLAIN_KEYS[:]
shuffle(SHUFFLE_KEYS)
SHUFFLE_DIRS = list("NLSO")
DIRS = list("NLSO")
shuffle(SHUFFLE_DIRS)


def desafio3(mmap):
    marray = []
    for line in ORDERED_KEYS:
        mline = []
        for key in line:
            mline.append(mmap[key])
        marray.append(mline)
    desafio0(marray)


def desafio4(mmap):
    marray = []
    keys = [SHUFFLE_KEYS[cel:cel+3] for cel in range(9)[::3]]
    for line in keys:
        mline = []
        for key in line:
            mline.append(mmap[key])
        marray.append(mline)
    desafio0(marray)
    shuffle(SHUFFLE_KEYS)


def desafio6(mmap):
    marray = []
    keys = [SHUFFLE_KEYS[cel:cel+3] for cel in range(9)[::3]]
    for line in keys:
        mline = []
        for key in line:
            code = mmap[key]
            rotate = (SHUFFLE_KEYS.index(key) + SHUFFLE_DIRS.index(code[1])) % 4
            mline.append(code[0] + DIRS[rotate])
        marray.append(mline)
    desafio0(marray)
    shuffle(SHUFFLE_KEYS)
    shuffle(SHUFFLE_DIRS)


def desafio5(mmap):
    marray = []
    keys = [SHUFFLE_KEYS[cel:cel+3] for cel in range(9)[::3]]
    print(keys)
    for line in keys:
        mline = []
        for key in line:
            code = mmap[key]
            mline.append(code[0] + DIRS[SHUFFLE_DIRS.index(code[1])])
        marray.append(mline)
    desafio0(marray)
    shuffle(SHUFFLE_KEYS)
    shuffle(SHUFFLE_DIRS)


def main(_=None):
    from browser import doc
    doc["pydiv"].html = ""
    Masmorra()


DES = [main, desafio0, desafio0, desafio3, desafio4, desafio5, desafio6]


def posiciona_monstro(m, x, y):
    masmorra = Masmorra.created()
    masmorra.posiciona_monstro(m, x, y)


def circus(desafio=1, param=MASMORRA):
    # desafio6({'Coycol':'AN', 'Cauha':'BN', 'Tetlah':'CN',
    #              'Huatlya':'DN', 'Zitllo':'EN', 'Micpe':'FN',
    #              'Nenea':'GN', 'Cahuitz':'HN', 'Pallotl':'IN'})
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
PAGE = [""]*10

PAGE[0] = '''
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
PAGE[1] ="""
  <div class="section" id="criando-uma-camara-com-constantes">
<span id="desafio-a"></span><h1>Criando uma Câmara com Constantes<a class="headerlink" href="#criando-uma-camara-com-constantes" title="Permalink to this headline">¶</a></h1>
<p>Uma constante é um valor que não se modifica ao longo de um programa.
Em Python a constante é escrita com todas as letras maiúsculas como no nome TOPO_ESQUERDA abaixo.</p>
<p>Use os ladrilhos nomeados de A a L para montar a câmara mostrada à direita.</p>
<img alt="_images/desafio_a.png" src="http://s19.postimg.org/del9469xv/desafio_a.png" />
<div class="highlight-python"><div class="highlight"><pre><span class="kn">from</span> <span class="nn">circus.circus</span> <span class="kn">import</span> <span class="n">circus</span>

<span class="n">TOPO_ESQUERDA</span> <span class="o">=</span> <span class="s">&quot;AN&quot;</span>
<span class="n">TOPO_DIREITA</span> <span class="o">=</span> <span class="s">&quot;AN&quot;</span>
<span class="n">TOPO_CENTRO</span> <span class="o">=</span> <span class="s">&quot;AN&quot;</span>
<span class="n">MEIO_ESQUERDA</span><span class="p">,</span> <span class="n">CENTRO</span><span class="p">,</span> <span class="n">MEIO_DIREITA</span> <span class="o">=</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span>
<span class="n">FUNDO_ESQUERDA</span><span class="p">,</span> <span class="n">FUNDO_CENTRO</span><span class="p">,</span> <span class="n">FUNDO_DIREITA</span> <span class="o">=</span>  <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span>

<span class="c"># O comando abaixo voce vai entender no próximo desafio</span>
<span class="n">circus</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="p">[[</span><span class="n">TOPO_ESQUERDA</span><span class="p">,</span> <span class="n">TOPO_CENTRO</span><span class="p">,</span> <span class="n">TOPO_DIREITA</span><span class="p">],</span> <span class="p">[</span><span class="n">MEIO_ESQUERDA</span><span class="p">,</span> <span class="n">CENTRO</span><span class="p">,</span>
        <span class="n">MEIO_DIREITA</span><span class="p">],</span> <span class="p">[</span><span class="n">FUNDO_ESQUERDA</span><span class="p">,</span> <span class="n">FUNDO_CENTRO</span><span class="p">,</span> <span class="n">FUNDO_DIREITA</span><span class="p">]])</span>
</pre></div>
</div>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">No texto &#8220;AN&#8221; a primeira letra determina o ladriho e a segunda se está girada para Norte, Leste, Sul ou Oeste.</p>
</div>
</div>


          </div>
        </div>
      </div>
"""
PAGE[2] ="""

    <div class="related">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="genindex.html" title="General Index"
             accesskey="I">index</a></li>
        <li class="right" >
          <a href="desafio_c.html" title="Posicionando um Personagem com Inteiros"
             accesskey="N">next</a> |</li>
        <li class="right" >
          <a href="desafio_a.html" title="Criando uma Câmara com Constantes"
             accesskey="P">previous</a> |</li>
        <li><a href="index.html">Flying Circus 0.1.0 documentation</a> &raquo;</li> 
      </ul>
    </div>  

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body">
            
  <div class="section" id="criando-uma-camara-com-listas">
<span id="desafio-b"></span><h1>Criando uma Câmara com Listas<a class="headerlink" href="#criando-uma-camara-com-listas" title="Permalink to this headline">¶</a></h1>
<p>Uma lista é um conjunto de coisas, pode ser um conjunto de números, letras, palavras ou qualquer outro objeto.
Em Python a lista é escrita assim: <em>[&lt;uma coisa&gt;, &lt;outra coisa&gt;]</em>.</p>
<p>Use os ladrilhos nomeados de A a L para montar a câmara mostrada abaixo, consulte o exercício anterior.</p>
<img alt="_images/masmorra.jpg" src="_images/masmorra.jpg" />
<div class="highlight-python"><div class="highlight"><pre><span class="kn">from</span> <span class="nn">circus.circus</span> <span class="kn">import</span> <span class="n">circus</span>

<span class="n">MASMORRA</span> <span class="o">=</span> <span class="p">[[</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">],</span>
            <span class="p">[</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">],</span>
            <span class="p">[</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">],</span>
            <span class="p">[</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">],</span>
            <span class="p">[</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">,</span> <span class="s">&quot;AN&quot;</span><span class="p">]</span>
            <span class="p">]</span>

<span class="n">circus</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">MASMORRA</span><span class="p">)</span>
</pre></div>
</div>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">No texto &#8220;AN&#8221; a primeira letra determina o ladriho e a segunda se está girada para Norte, Leste, Sul ou Oeste.</p>
</div>
</div>


          </div>
        </div>
      </div>
      <div class="sphinxsidebar">
        <div class="sphinxsidebarwrapper">
  <h4>Previous topic</h4>
  <p class="topless"><a href="desafio_a.html"
                        title="previous chapter">Criando uma Câmara com Constantes</a></p>
  <h4>Next topic</h4>
  <p class="topless"><a href="desafio_c.html"
                        title="next chapter">Posicionando um Personagem com Inteiros</a></p>
  <h3>This Page</h3>
  <ul class="this-page-menu">
    <li><a href="_sources/desafio_b.txt"
           rel="nofollow">Show Source</a></li>
  </ul>
<div id="searchbox" style="display: none">
  <h3>Quick search</h3>
    <form class="search" action="search.html" method="get">
      <input type="text" name="q" />
      <input type="submit" value="Go" />
      <input type="hidden" name="check_keywords" value="yes" />
      <input type="hidden" name="area" value="default" />
    </form>
    <p class="searchtip" style="font-size: 90%">
    Enter search terms or a module, class or function name.
    </p>
</div>
<script type="text/javascript">$('#searchbox').show(0);</script>
        </div>
      </div>
      <div class="clearer"></div>
    </div>
    <div class="related">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="genindex.html" title="General Index"
             >index</a></li>
        <li class="right" >
          <a href="desafio_c.html" title="Posicionando um Personagem com Inteiros"
             >next</a> |</li>
        <li class="right" >
          <a href="desafio_a.html" title="Criando uma Câmara com Constantes"
             >previous</a> |</li>
        <li><a href="index.html">Flying Circus 0.1.0 documentation</a> &raquo;</li> 
      </ul>
    </div>
    <div class="footer">
        &copy; Copyright 2016, Carlo E. T. Oliveira.
      Created using <a href="http://sphinx-doc.org/">Sphinx</a> 1.2.3.
    </div>
"""
PAGE1 ="""

    <div class="related">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="genindex.html" title="General Index"
             accesskey="I">index</a></li>
        <li class="right" >
          <a href="desafio_g.html" title="Dar Nomes para os Monstros com string"
             accesskey="N">next</a> |</li>
        <li class="right" >
          <a href="desafio_e.html" title="Matar o monstro com if"
             accesskey="P">previous</a> |</li>
        <li><a href="index.html">Flying Circus 0.1.0 documentation</a> &raquo;</li> 
      </ul>
    </div>  

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body">
            
  <div class="section" id="criando-varios-monstros">
<span id="desafio-f"></span><h1>Criando Vários Monstros<a class="headerlink" href="#criando-varios-monstros" title="Permalink to this headline">¶</a></h1>
<p>O comando <em>for</em> caminha em uma lista e executa o conjunto de comandos indicado para cada elemento.
Em Python o for é escrito assim: <em>for &lt;elemento&gt; in &lt;lista&gt;:</em>.
Se cada elemento da lista for outra lista, você pode colocar vários elementos separados por vírgualas, veja:</p>
<p><em>for &lt;elemento0&gt;, &lt;elemento1&gt; in &lt;lista com listas&gt;:</em></p>
<dl class="docutils">
<dt>Complete a lista de elementos com coordenadas para diversos monstros</dt>
<dd>e chame a função <em>posiciona_monstro()</em> para cada um deles.</dd>
</dl>
<div class="highlight-python"><div class="highlight"><pre><span class="kn">from</span> <span class="nn">circus.circus</span> <span class="kn">import</span> <span class="n">posiciona_monstro</span>

<span class="c"># lista_de_posições = [(0, 0, 0), (&lt;&gt;), &lt;&gt;]</span>

<span class="c"># for &lt;&gt; :</span>
<span class="c">#     &lt;&gt;</span>
</pre></div>
</div>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">Na tripla ordenada (0, 1, 2) o 0 serve para usar a figura de monstro 0, o 1 para colocar o monstro na posição x=1 e o 2 na posição y=2.</p>
</div>
</div>


          </div>
        </div>
      </div>
      <div class="sphinxsidebar">
        <div class="sphinxsidebarwrapper">
  <h4>Previous topic</h4>
  <p class="topless"><a href="desafio_e.html"
                        title="previous chapter">Matar o monstro com if</a></p>
  <h4>Next topic</h4>
  <p class="topless"><a href="desafio_g.html"
                        title="next chapter">Dar Nomes para os Monstros com string</a></p>
  <h3>This Page</h3>
  <ul class="this-page-menu">
    <li><a href="_sources/desafio_f.txt"
           rel="nofollow">Show Source</a></li>
  </ul>
<div id="searchbox" style="display: none">
  <h3>Quick search</h3>
    <form class="search" action="search.html" method="get">
      <input type="text" name="q" />
      <input type="submit" value="Go" />
      <input type="hidden" name="check_keywords" value="yes" />
      <input type="hidden" name="area" value="default" />
    </form>
    <p class="searchtip" style="font-size: 90%">
    Enter search terms or a module, class or function name.
    </p>
</div>
<script type="text/javascript">$('#searchbox').show(0);</script>
        </div>
      </div>
      <div class="clearer"></div>
    </div>
    <div class="related">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="genindex.html" title="General Index"
             >index</a></li>
        <li class="right" >
          <a href="desafio_g.html" title="Dar Nomes para os Monstros com string"
             >next</a> |</li>
        <li class="right" >
          <a href="desafio_e.html" title="Matar o monstro com if"
             >previous</a> |</li>
        <li><a href="index.html">Flying Circus 0.1.0 documentation</a> &raquo;</li> 
      </ul>
    </div>
    <div class="footer">
        &copy; Copyright 2016, Carlo E. T. Oliveira.
      Created using <a href="http://sphinx-doc.org/">Sphinx</a> 1.2.3.
    </div>
"""
PAGE1 ="""
"""


def desafio(desafio=1):
    from browser import doc
    doc["pydiv"].html = PAGE[desafio]
