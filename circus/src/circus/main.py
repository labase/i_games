from random import random


class Main:
    def __init__(self, Game, Phaser):
        self.ph = Phaser
        self.game = Game(800, 600, Phaser.AUTO, 'phaser-example',
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

    def update(self, *arg):
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


def main(Game, auto):
    Main(Game, auto)
