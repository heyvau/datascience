"""
Aufgabe Facebook Likebutton (schwer)

Das Facebook-Element "Like" besteht aus zwei Buttons: Like und Dislike
symbolisiert durch Daumen hoch, und Daumen runter.

Das System kann in einem von drei Zuständen sein:
- Empty (kein Like oder Dislike)
- Liked (Daumen hoch)
- Disliked (Daumen runter)

folglich gibt es zwei Events:
- like Button drücken
- dislike Button drücken

Empty:
+-----------------+
| Like [ ]        |
| Dislike [ ]     |
+-----------------+

Liked:
+-----------------+
| Like [X]        |
| Dislike [ ]     |
+-----------------+

Disliked:
+-----------------+
| Like [ ]        |
| Dislike [X]     |
+-----------------+

Klick auf LIKE-BUTTON:
Wenn Zustand ist empty, Zustand wird liked
Wenn Zustand ist liked, Zustand wird empty
Wenn Zustand ist disliked, Zustand wird liked

Klick auf DISLIKE-BUTTON:
Wenn Zustasnd empty, Zustand wird disliked,
Wenn Zustand liked, Zustand  wird disklike
Wenn Zustand gerade disliked, wird Zustand empty

Implementiere die zwei Events (click like und dislike) und drei Zustände
(mpty, liked, disliked).

Nutze Enum.

# ----------------------------------------------------------------------
Zusatzaufgabe: Teste das System, indem eine Folge von Klicks auf
den Button simuliert wird.

zb. "lldd" => Drücke like, Drücke like, drücke dislike, drücke dislike
und prüfe das Ergebnis.

def press_many(start_state: LikeState, actions: str) -> LikeState:
    ...

press_many(LikeState.empty, "ddll")

"""

import enum


class LikeState(enum.Enum):
    """
    der Zustand des Likebuttons (es gibt drei Zustände)
    """
    DISLIKED = -1
    EMPTY = 0
    LIKED = 1


def press_like(s: LikeState) -> LikeState:
    """
    Args:
        s: Likezustand
    Return:
        Likezustand

    """
    return (
        LikeState.EMPTY if s == LikeState.LIKED
        else LikeState.LIKED
    )


def press_dislike(s: LikeState) -> LikeState:
    """
    Args:
        s: Likezustand
    Return:
        Likezustand
    """
    return (
        LikeState.EMPTY if s == LikeState.DISLIKED
        else LikeState.DISLIKED
    )


def press_many(start_state: LikeState, actions: str) -> LikeState:
    """Simulation von vielen Klicks auf die Like/Dislike-Button

    Simuliere das System, indem eine Folge von Klicks auf den Button simuliert wird
    zb. "lldd" => Drücke like, Drücke like, drücke dislike, drücke dislike
    Args:
        start_state: LikeState
        actions: str
    Return:
        LikeState
    """
    if not set(actions).issubset({"l", "d"}):
        raise ValueError("String-Argument 'actions' kann nur 'l' und/oder 'd' enthalten.")
        
    state = start_state
    for ch in actions:
        state = press_like(state) if ch == "l" else press_dislike(state)
    return state


def test_likestate():
    assert press_many(LikeState.EMPTY, "ll") is LikeState.EMPTY  # like, like
    assert (
        press_many(LikeState.EMPTY, "dd") is LikeState.EMPTY
    )  # dislike, dislike
    assert (
        press_many(LikeState.EMPTY, "ld") is LikeState.DISLIKED
    )  # like, dislike
    assert (
        press_many(LikeState.EMPTY, "dl") is LikeState.LIKED
    )  # dislike, like
    assert (
        press_many(LikeState.EMPTY, "ldd") is LikeState.EMPTY
    )  # like, dislike, dislike
    assert press_many(LikeState.EMPTY, "lldd") is LikeState.EMPTY  #  usf
    assert press_many(LikeState.EMPTY, "ddl") is LikeState.LIKED


if __name__ == "__main__":
    test_likestate()
