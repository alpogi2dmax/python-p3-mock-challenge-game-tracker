class Game:

    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            None
        elif isinstance(title, str) and len(title) > 0 and not hasattr(self, '_title'):
            self._title = title
        else:
            raise ValueError('Title must be a non-empty string')


    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        player_list = []
        for result in Result.all:
            if result.player not in player_list and result.game == self:
                player_list.append(result.player)
        return player_list


    def average_score(self, player):
        scores = [result.score for result in Result.all if result.game == self and result.player == player]
        return sum(scores) / len(scores)

class Player:

    all = []
    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        unique_games = []
        for result in Result.all:
            if result.game not in unique_games and result.player == self:
                unique_games.append(result.game)
        return unique_games

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in Result.all if result.player == self and result.game == game])

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and hasattr(self, '_score') == False:
            self._score = score
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise TypeError('Player must be an instance of the Player class')
        

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise TypeError('Game must be an instance of the Game class')