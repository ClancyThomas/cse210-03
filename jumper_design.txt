class: Director
    Responsibility: Store value for continue playing.
        continue_playing: bool

    Behaviors:
        play_game(): bool
        end_game(): bool


class: Puzzle
    Responsibility: To create a list of words and store it.
        list_words: list(str)

    Behaviors: Choose one random word from created list.
        _choose_word(): str


class: Image
    Responsibility: Create and store image of jumper and parachute.
        image: str

    Behaviors: Edit the image and print the image.
        _edit_image(): str
        _print_image(): str


class: Guess
    Responsibility: Track all guesses.
        guess_list: list(str)

    Behaviors: Prompt for guess and validate guess.
        _prompt_guess(): input(str)
        _validate_guess(): bool