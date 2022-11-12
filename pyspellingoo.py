
from dataclasses import field, dataclass
from os import listdir
from os import getcwd
import uuid


@dataclass(frozen=False)
class Environment:
    word_path: str = 'resources/words/'
    sound_path: str = "resources/sounds/"
    _extensions: list[str] = field(default_factory=list)
    _file_list: list[str] = field(default_factory=list)
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=uuid.uuid4)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.word_path} {self.sound_path}"
        self._extensions.append(".m4a")
        self._extensions.append(".mp3")
        for file in listdir(self.word_path):
            self._file_list.append(file)


class Results:
    def __init__(self):
        self.results = []

    def add_result(self, result):
        word_found = False
        for i in self.results:
            if i.word == result.word:
                i.score += result.score
                word_found = True
        if not word_found:
            self.results.append(result)

    def get_results(self):
        self.results.sort()
        return self.results


class Result:
    def __init__(self, word, score):
        self.word = word
        self.score = score

    def __lt__(self, value):
        if not isinstance(value, Result):
            raise ValueError("Can't compare a Result to a non-result")
        return self.score < value.score


class Score:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, value):
        if not isinstance(value, Score):
            raise ValueError("Can't compare a Score to a non-score")
        return self.score < value.score


class LeaderBoard:
    def __init__(self):
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_scores(self):
        self.scores.sort(reverse=True)
        return self.scores


class Word:
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return f"{self.word}"

    def get_word_file(self):
        return self.word + ".m4a"


class Dictionary:
    def __init__(self):
        self.dictionary = []

    def add_word(self, word):
        self.dictionary.append(word)

    def list_words(self):
        return self.dictionary

    def get_first_word(self):
        return self.dictionary[0].get_word_file()


print(getcwd())


leader_board = LeaderBoard()
leader_board.add_score(Score("Andrew", 324))
leader_board.add_score(Score("Oliver", 999))
leader_board.add_score(Score("Matthew", 938))
leader_board.add_score(Score("Becky", 332))

print([score.name for score in leader_board.get_scores()])
print([score.score for score in leader_board.get_scores()])


results = Results()
results.add_result(Result("when", 1))
results.add_result(Result("one", 1))
results.add_result(Result("could", 0))
results.add_result(Result("should", 0))
results.add_result(Result("one", 1))

print([result.word for result in results.get_results()])
print([result.score for result in results.get_results()])


d = Dictionary()
env = Environment()
print(Environment())
