KQ = "KQ"; KJ = "KJ"; QK = "QK"; QJ = "QJ"; JK = "JK"; JQ = "JQ"
CARDS_DEALINGS = [KQ, KJ, QK, QJ, JK, JQ]

CHANCE = "CHANCE"

CHECK = "CHECK"
CALL = "CALL"
FOLD = "FOLD"
BET = "BET"
NEXT = "NEXT"
WIN = "WIN"
DEFEAT = "DEFEAT"


RESULTS_MAP = {}
RESULTS_MAP[QK] = -1
RESULTS_MAP[JK] = -1
RESULTS_MAP[JQ] = -1
RESULTS_MAP[KQ] = 1
RESULTS_MAP[KJ] = 1
RESULTS_MAP[QJ] = 1

A = 1
B = -A