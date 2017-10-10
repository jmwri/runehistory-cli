from cement.core.controller import CementBaseController, expose


class HighScoresController(CementBaseController):
    class Meta:
        label = 'highscores'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Fetch player highscores"
        arguments = [
            (
                ['-p', '--player'],
                dict(help='Player name', dest='player', required=True)
            ),
        ]

    @expose(hide=True)
    def default(self):
        from runehistory.highscores import get
        highscores = get(self.app.pargs.player)
        print(highscores)