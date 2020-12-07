import re

puzzleInput = ["FBFBBBFRLR", "FBBFBBBLLR", "FFFFFBBRRL", "BBBFFFBRRL", "BFFBFBFLRL", "FBFFBFFLLR", "FBFBBBBRLR", "FBFBFBFRLL", "BFFBFFBRLR", "FBBFFFBLRR", "FBFBBBFRRR", "BFFBBFBRLR", "BFFBFBFRRL", "FFFFBBBLRL", "FBBFBFFRLL", "BBFBBFBRLR", "BFFFFBBLLR", "FBFFFFFRRR", "BFBFFBFLRR", "BBFBFFBLLL", "BFBFFFFLLR", "FBBFBBBRLL", "BBBBFFFRRL", "FFBBBFFRLR", "FFFBFFFRRL", "FFFBBBBLRL", "BFBBFBFRRL", "BFFBBFBLLL", "FBFBBFFLRL", "BFFBBBBLRL", "FFBBBFFLRL", "FFBFBFFRRL", "BBBFBFBRLR", "FBFBBBBRLL", "FBBBFBBRRR", "FBFBFBFLLL", "BBFFFFFLLR", "FBFFFBBLRR", "FFBFFFBLRR", "BBBFBFFRLR", "FFFFFFBRRL", "BFBBFFFRRR", "FBFFBFBRRR", "BFFFBBFLRL", "BBFBFFFRRR", "BBFFFBBLRL", "FFBBFFFLLL", "FFFFFBBRLR", "BFBFFFFRRL", "FFBBFBBLRR", "BFBBFBBLLR", "FFBBBBFRRL", "BBBFFFFLRL", "BFBFFBFLRL", "BFFFFBBLRL", "BBBFBBBRLL", "BFBBFBBLRR", "BFBFFBBRRL", "BBFBFFFLLL", "FFFFBFFRRL", "FFFFBBBRRR", "FBBFBBFLRL", "FBFFBFBRLR", "FBFFBBBLLL", "FBFBBBFLLR", "FBBFBFBRLL", "BBBFBFFLLL", "BBFFFFFLRL", "FFBFBFBRLL", "FBBBFFBLRL", "FBFBFFBLRL", "FFFBBFBRLR", "FBFBBFBLLR", "FBFFBBBRLL", "BBFBBFBLLL", "FBBBBFFRLL", "FBBBBBBLRR", "FFFFFBFLRR", "BFFBFBBLRR", "FBFFBFFLRR", "BBFFFFBLRL", "BBFFBFFLLR", "FFFBBBBLRR", "FBFBBBFRRL", "FBBFFFBLRL", "BBFBBFFRRL", "FFBBBFBRLR", "BBBFBFBRRR", "FBFFBFFRRR", "FFBFFBFRLR", "BFBBFFBLLL", "FFBBBFFRRL", "FFFBFFFRLL", "BBFFFBFLLR", "BFFFFFBRLL", "FFBFBBBRLL", "FFFBFBFLLL", "FBBFBBBLRR", "BFBFBFBRLL", "FFBBBBBLLL", "FFBFFFBRRR", "BBFBBFFRLL", "BFFFFFFLRL", "FBFFBFFRLR", "BFFBBBFLRR", "FFFBBFFRLR", "FBFFFFBLLL", "BBFFBBBRRR", "FFBFBFBLLR", "FBBFFBBLLR", "BBFBBFBLLR", "BBFBBFBLRL", "BBBFFBFRRL", "FBFFBBBLRL", "BFBFBFFLLR", "BFFFFFBRLR", "FBFBFFBLLR", "BFFFBFBRLL", "FBFFFFBRRR", "BFBBFBBRRL", "FBFFFBBLRL", "BFBBBBFLRL", "BBBBFFBLRL", "FFBFFBBLRL", "FFFBFFBRLR", "FBFBFFBRLR", "FBFBFBBRRR", "BFFBFBBLRL", "FBBBFBBRLR", "BFBBBFFLLL", "BFBFBBBLLR", "BBBFBBBRRR", "FFBFFFFRLR", "BBFFFBBRRR", "BBBFBBFRRL", "FFBFFBBLLL", "BBFFBFFLRR", "BBFFBFBRRL", "BBFBBBFLRR", "FBFFBFBLRL", "BFBFFFFLLL", "FFBBBFBRRR", "BBBFBBBLLL", "FBFBBFBLRL", "BBBFFFBRLL", "BFFFBBFRRL", "BBBBFFFLLR", "BBBFBFFRLL", "FFBBFBFLRR", "FBBFBFBRRR", "FBBFBBFLRR", "BBFFFBFRRL", "FBFFFBBRLL", "BBFFFFFRLR", "FBBFBBFRRL", "FBFFFBBLLL", "BFBFBBFLLL", "BFFBFFBRLL", "FFFFBBBRLR", "BBFBBBBRLR", "BFBFFFBLRR", "BFBFFFBRLL", "FBFBBBBLLR", "BFFFBFFRRR", "FFBBBFFLLR", "BFBFFFBLLL", "FFBBFFBRLR", "FBBFBBBRRL", "BBFBFFBLRR", "FBBFBBBRRR", "FFFBBFBRRL", "BFBFBFBLLR", "BBFBFFBLRL", "BBBFBFBRRL", "BFFBFBFLLR", "BFBFBBBLRR", "FBFFFBFRLL", "BFFBFFFRRL", "FBFBFFFRRR", "BFFBFFFRLL", "FFBBFFBLLL", "BBBBFFFRLR", "BBBFFBFLLR", "BFBFBFBRRL", "BBFBBBBLLR", "BFFBBFFRLR", "FFFFBBBRRL", "BFFFBBFRLR", "FFBBFBBLLL", "BBBFFFBLLR", "BBFBBBFLLL", "FFFFFBFLLR", "BBBFBBFLRL", "FFFFFBFLLL", "BBFBFFFLLR", "BFBBFBFLRL", "BFBFBBFRRL", "BBBFBFFRRL", "BFFFBBFRLL", "FFFFBFBLRL", "BFBBBBBLRR", "FFFBFFBLRL", "FFFBBBBRLL", "BBBFBFBLLR", "BBBBFFBLLR", "BFFFBBBLLR", "BBFFFBBLLR", "BBFFBBBLRR", "FBBFBFBLLR", "BBBFFFFRLL", "FBBFBFBRRL", "FFBFBFFRLR", "BFFFFBFLLL", "BBFBBBBLLL", "FBFBBBBLRR", "BBBBFFFRLL", "BFBBFBBRRR", "FFFFBBBLLL", "BBFFBFBRLL", "FBBFFBFLRL", "FFBBBFFRLL", "FFFBBBFRLR", "FFBBFBFLRL", "BBFBFBFLLR", "BFFFFFBLRR", "FBFBBBFRLL", "FBFFFFFLLR", "FBFBFFBLLL", "BFFBFBFRLR", "FFBFBFFLLL", "FFFFFBBLLR", "BBBBFFBRRR", "FBFBFBFLLR", "BBFFFBFRLR", "BBFFBFBLRR", "BFFBBFFLRR", "BFFFFBFLLR", "FBBFBFBLRL", "BFFFFBFLRL", "BBFFFFFLRR", "BBBFFFFRRR", "FFBBBFFLRR", "BFFFBFBLRL", "BBFBFBBLRR", "BBFBFFBRLR", "FFFBFBFLRR", "FBFFFFFRLL", "BBFBBBFRLR", "BBFFBBFRRL", "BFBFFBBRLR", "FFBFFFBLLR", "BFBFFFBRLR", "BBBBFFBRLR", "BFBFFBFLLR", "BBFFBBFLLR", "FBFFFFBLLR", "FFFBBFBLRR", "FFBBFFBRRR", "FBBBFBFLRL", "FBFBFBFLRR", "BFFFBFBRRL", "FBFFFFBRRL", "FBFFFBBRLR", "FBBFFBBRRL", "FBBFBFFLRL", "BFBFBBFRLL", "FBBBBFFRLR", "FFBFFFFRRL", "BFBFBBBRRR", "BFFBBBFRRR", "BBFFFFFLLL", "BFBBBBFLRR", "FBBBBBFRRL", "BBFBFBFRRL", "BFFBFFFRLR", "FBFFFBFRRR", "FFBBBBBLLR", "FBFFFBFRLR", "BFBFBFBRLR", "FFFBBBFRRR", "FBBBFFBRLL", "BBFBFBBLRL", "FFFBFBBLLL", "BFBFBFFLLL", "FFFBFFFLLL", "FBBBFBBRRL", "FBFFFBFLRL", "FBFFBFBRLL", "BBFFBBFRLL", "BFFFBFFRLL", "FFBBFBFRRR", "BBBFFBBRRL", "BBFBFBBRLR", "FFBBFFFLRR", "FFBBBBFLLR", "FFBFFBFLLR", "FBBFBBFRLL", "FBFBBFFLRR", "BBBFFFFRRL", "FFFFFBBLRR", "BFBFBFFRLR", "FFBBBBFRRR", "FFBBFFFLLR", "FFBBBBBLRR", "FBBBBFBRRR", "FBFFFBBRRR", "BFFBFFBRRR", "BFBFBBFLRR", "FBFBBBBRRL", "FBBBBFBRLR", "BFFBBFBLLR", "FBBBFBBLLL", "FFBBBBBRLL", "FBBBBBBRLL", "FFFBFBBLLR", "BFFFFFBRRL", "BFFBFBBRRL", "FBBBFFBLRR", "FFFBFFFLRR", "FFBBBBFRLR", "BFFBFFFLLL", "FBFFBFFRLL", "BFBFBFFRLL", "FBBFBBBRLR", "FBFFBBFRLL", "FFBFFFBRLR", "BFBBFBFLRR", "BFBBBBFRRL", "FBFBFBBRLL", "BFBBBFBLRL", "FFBBFFBLRR", "BBFFBBBRLR", "FBBBFBBLRL", "BBBBFBFLRL", "BBBFBBFRRR", "FFFBBFBLRL", "BFBFFBBLLR", "BBBFFFBLRL", "BBFFFFBLRR", "FFBBBBFLLL", "FBFFFBFLLL", "FFBBFBBRRL", "BFFBBBBLRR", "FBBFFBBRLR", "BFBBFBFRLL", "FFBBBBBLRL", "FBFBFFFRLR", "BFBBBFBRRR", "BFBBBFBRLL", "BBFBBBFRRR", "BFFBBFBRRR", "BBFFBBBRLL", "FFBFFBBRLR", "FFFFBBBRLL", "FFBBBFBLRL", "FFFBFBFRLL", "BFBFBBFRRR", "FBBFFFFRLL", "BBBBFBFLLL", "FBFBFFBRRR", "BFFFBBBRRR", "FFFBBFBLLL", "BBBFBBBRRL", "FBFFBFBLLR", "FBBBBBFRLL", "FBBFBFFLLL", "BFBFFFBRRR", "FBFBFBBLRL", "FBFBBBBLLL", "FFBFFFBRLL", "BFFFBFBRLR", "BFBFBBBRLL", "FFBFBBFLLL", "BBBBFFFRRR", "FFFBFBFRRR", "FFBBFFFRLL", "BFBBBBBLLR", "FBBBBFFLRL", "BFBFBBFLRL", "BFFBBBFLRL", "BBFFBFBRLR", "BBBFFBFLLL", "FBFFBFFRRL", "FFFBBBBRLR", "BBFBFFFLRR", "FBBBBBBRLR", "BBFFBBBLLL", "BBFBBFFLLL", "FBBFFBFRLR", "FFFFBFBLRR", "FFFBBFFRRR", "FBFBFBFLRL", "BBFFBBFRRR", "FFFFBFBRRR", "FFBFBBBLRR", "FBFFFBBRRL", "BFFBBFBRLL", "FFBFBFFLRR", "FFBBFBBLLR", "FBBBBBBLLR", "FFFBBBFLLL", "FFBBFFBLRL", "BBFFFBBRLR", "FFFFBFFRLR", "BBFBFFBLLR", "FFFBFBBLRR", "BBFFFFBRLR", "FBFBFFFRRL", "FBBBFBFLLL", "FFFBBBFRLL", "FFFBFBBRLL", "FFBFFBBLLR", "BFFFBBBLRR", "FFFBBFBLLR", "FFBFBBFLRL", "BFFBFBFLLL", "BFFFBBFLRR", "FBFFFBBLLR", "FBBFFBBLLL", "FFBBFFFLRL", "BBBFFBFLRL", "FBBFFFFLLL", "BFFBBFFLLR", "BBBFFFFLLL", "FBFFBBFRRR", "BFBBBBBRRR", "FBFFFFFLRL", "FFBFFBBRRL", "FBFBBFFRLL", "FFBFBBFRLR", "BBBFFBBLLL", "FFFBBBFLRL", "BBFFFBBRRL", "BFFFFFBLLR", "FBBBFFBLLR", "BBFBBFFLRR", "FBFBBFBLLL", "BFBBFBFRLR", "BFBBFFBRRL", "BBFFFBBLRR", "FBBFFBFLRR", "FFFBFFBRRR", "FBFBBBBLRL", "BBFFBBBLLR", "FFBFFFBLRL", "FBBBFFFLRR", "BBBBFFBRLL", "BFFBBBFLLR", "BFBBBBFRLL", "BFFBFFBRRL", "BFFFFBBRLR", "FFBFFFBLLL", "FBBFFBFRLL", "BFFBBBBRLR", "BFFBFBBLLL", "BBBFFBFRLR", "BBFBBFBRLL", "FFFFBBFRRL", "FFBFBFBLRR", "BFFBBBBLLR", "BFFFFBFRRL", "FBBBBFBLRL", "BBBFFBBLRR", "FBBBBFBLLL", "FFFBFBBLRL", "FFBFBBFRRR", "BFBBFFBRLR", "BBFFBBFLRR", "FBBBFBFRLR", "FBBFBFBLLL", "BFFFBBFRRR", "BFFFFBFRLR", "FFBFFBFRRR", "FFFFBBFRLR", "FBBFFFBLLL", "FBFFBBFLRR", "BFFFFFFRLL", "BFBBBFFLRR", "FBFFBFBLRR", "FBFBBFFRRR", "FFFBBBBRRL", "BFFFBFFLLR", "FBBBBFFLLR", "BFFFFFFRRR", "FFBFFFFLRR", "FBBFFFFRRL", "FBBFFFFRLR", "BBFFBBBLRL", "FBFFBBBRRR", "BFFFBBBRRL", "BFFFBBBLLL", "BFFFFBBRLL", "BFFFFFFLRR", "FBFBFBFRLR", "FFFBFFFRRR", "FFFFBBFLLL", "BBBFBFBLRR", "BBBFBBFLRR", "BBFBFBBLLL", "FFFBBBFLRR", "FBBFFFBRLL", "BFFBFFFLRR", "BFBFBBBRRL", "BFFBBBBRRR", "FBFFBBBLRR", "BFFFBBFLLL", "BBBFBFBLRL", "BFFFBFBLLR", "BBBFBFFLLR", "FFBFFBBLRR", "FBBFBFFLRR", "BBBFFBFRRR", "BFBBFFFLRL", "FFBBBFBLLR", "FBBBBFFRRR", "BFBBBBBRLR", "BBFFBFBLLR", "BFFBFBBRLR", "BFFBFFFLLR", "BFFBBBBRRL", "BBFBFBFLRL", "BFFBBBFLLL", "BBBFFBFLRR", "FBFFFFFLRR", "BFBFBFBRRR", "BBBFFBFRLL", "BFFFBBFLLR", "BBBFBBFRLR", "FFFFBBFLRR", "FBBBFBFRRL", "FFFBFFBRRL", "FFBFFBBRRR", "BFBBBBBLLL", "FFBFFBFRLL", "BFBFFFBLLR", "BFFBBFBLRL", "BBFBBFFLRL", "FFFBFBFRRL", "BFFBBBBRLL", "FBFBFFBRRL", "FFFFFBFRLR", "FBBBBFBRLL", "FFFFBFFLLL", "FBFBFBBRLR", "FBFFFFBRLR", "BFBBFFBLRR", "BFBBBFFRLL", "BBFBBFFLLR", "FBFBBBFLRR", "FFFFBFFRLL", "BFBBFFBRRR", "BBBFFFFLLR", "BBFFFBBLLL", "BFFFFFFRRL", "BFBBFFBRLL", "FFBFFFBRRL", "FBFBBFBRLL", "BFBBBFBLRR", "BBFBFBFLRR", "BBBFBBFLLL", "FBFBFFFLRR", "BBBBFFBLRR", "FFFBBFFLRR", "BFFFBFBLLL", "FFFFBFFLRL", "FFBBFBBRLR", "FFFBFBFRLR", "BFFBFBFRLL", "BBBFFFBLLL", "BBFBBFBRRR", "BFBFBBBLLL", "BFFBFFBLLR", "BFBBFBBLRL", "BBFBFFBRLL", "FBFBBFFLLR", "BFFFFFBLLL", "FBFFFFFRRL", "FFFFFFBRRR", "BBBFFFFRLR", "FBFFFBFRRL", "BFBFFBBRLL", "BBFBFFBRRR", "FFBFBBBLRL", "FFFBFFBLRR", "FFFBBBFRRL", "BFFBBFBRRL", "BFBFFFBLRL", "FBBFFBBRLL", "FFBBBBBRRL", "FBBBBFBLRR", "BBFBFBBRRL", "FBBBFFBRLR", "FFBBFBBRLL", "FFFBBBFLLR", "BFBBFFFLRR", "FBBBFFFLRL", "BFBFFFBRRL", "FFFFBBBLRR", "FFFBFFBRLL", "BFBBFBBRLR", "FFFFFBBLLL", "BFBBBFFRLR", "BFBFFFFLRR", "BFBBFFFLLR", "FFFFBFFLRR", "FFBFBFBLLL", "BFBFBBFRLR", "FBFFFBFLLR", "FFBBFFBLLR", "FBFBBBBRRR", "FBBBBBBLLL", "FFBFBBBRRR", "FBFFBBFRLR", "BFFFBFFLRL", "FFBFBFFRLL", "FBFFFFBLRR", "BFBFFFFRLR", "FBBBBBBRRL", "BFBFBFBLRR", "FFBFBBFLLR", "FFFBBFFLLL", "FFFBBFFLLR", "FBBBFBBLLR", "BFBBBFBLLL", "BFBFFBFRLL", "BFBBFFFRRL", "BFBBFFBLLR", "FBBFFBFRRL", "BBFBBBBRRR", "FBBBFFBRRR", "BFFBBBFRLR", "BBFBBBBRRL", "FBBBFBFLLR", "BFBFFFFRLL", "FBBFFFBLLR", "BBBBFFFLRL", "BFFBFBFLRR", "FBFFBFBRRL", "BFBBBFFLRL", "BBFFBFFRLL", "BFBFBBBLRL", "BBFFFBFLRR", "BBFBFFFRRL", "BFFBFBBLLR", "FFFFBFBRLR", "FFBBBBFLRR", "FBBBBBFLLL", "BFBBFBFLLL", "FBBBBFBLLR", "FBFBFFFLLL", "BBFFFBFLLL", "BBFBBBBLRL", "FFFFFBBLRL", "FFBFBBBLLR", "FFFBFFFLLR", "BFBFBFBLRL", "FFBFFBFLRL", "FBFFBBFLRL", "FFBFBBFRRL", "BFFBFFBLRR", "BFFBBFFRLL", "FFBFBFBRRL", "FBFBFBBLRR", "FBFBFBBLLL", "FFFFBBFRLL", "FBBBFFFRLR", "FBFBBFBRLR", "FBFFBBFLLL", "BBFBBBFRLL", "FBBBBBFLLR", "FBBFFBBRRR", "BFFBBBFRRL", "BBFFBFFRRR", "FFBFBBBLLL", "FBBBBFFLLL", "BBBBFBFLLR", "FBBFBFFRRL", "BBFBFBFRLR", "FFFFBFFRRR", "BFBFBFBLLL", "BBFBBBBLRR", "BBFFBFBLLL", "BFBFBFFLRL", "FFBFFFFLLR", "FFFBBFFRLL", "BBBBFFBRRL", "BBFBBFBRRL", "BBBFBFFLRL", "BFFFBBBRLR", "FBFBBBFLRL", "FFBBBFBLRR", "BFBFFFFRRR", "BBBFFFBLRR", "FFBFFFFRLL", "BFBFFBFRRR", "BFBBBFFRRL", "FFFFFBFRLL", "BBBFFBBLLR", "BBBFFFFLRR", "BFFBBFFRRL", "FFBFBFFLLR", "FBBBBFBRRL", "FBFBFBBRRL", "BBFFFFBRLL", "FFBFBBBRLR", "FBFBBFFLLL", "FFBBBBBRLR", "BFBBBBBRRL", "BBBFBFFRRR", "FFFBBFBRLL", "BFBBFFFLLL", "FFFFBFBRLL", "BBFFBBFLRL", "FFFBFBBRRL", "BBFBFBBRLL", "BFBFBBBRLR", "FFFFBBBLLR", "BFBBBBBRLL", "FBBFBFFRRR", "FBFFFBFLRR", "FBBBFFFLLL", "FFBFBFBRLR", "FFFBFFBLLL", "FFBBFBFLLL", "BFBBBFBLLR", "FFFFBFBRRL", "FFFBFFBLLR", "BBFFBBFRLR", "BFFFFFBRRR", "BFBBFFFRLR", "FFFFFBBRLL", "BBBFFBBRLL", "BFFBFBBRRR", "BFBFBFFRRL", "FBBFFFBRRL", "FFFBBFFLRL", "FBBFFBFLLL", "FBBFFFFLLR", "BBFBBFBLRR", "BBBFBBBRLR", "FFFFBFFLLR", "BFFBBFFLRL", "BBFBBBFRRL", "BBFFFFFRRL", "BFBFFBBLRR", "FFBBFFFRRL", "BBFBFBFRLL", "BFFBFFFRRR", "BBFBFFFRLR", "BFFBFBBRLL", "BFFFFBBRRR", "BFBFFBFLLL", "FFFFFBFLRL", "FBBFBBBLRL", "BFBBBFBRLR", "BFFFFFFLLL", "FFFBFFFRLR", "BFBBBFFRRR", "FBBFFBBLRL", "BBFFFFBRRL", "BFFFFBBRRL", "BBBFFFBRRR", "BFBBFBBRLL", "FBBFFBFLLR", "FFBBFBBRRR", "BBFFBFBLRL", "FFBFBFBRRR", "BFBBFFBLRL", "BFFBBFFLLL", "FFFBBBBLLR", "FFBFBBFRLL", "FBBBFFBLLL", "BFBFBFFLRR", "BFBBFFFRLL", "FFBFBBBRRL", "FFBBFBFRRL", "FBFBBFBRRL", "BFFBBBBLLL", "BFBFFBBRRR", "BBFBBBFLRL", "BFBFFBFRRL", "BFFBFFBLLL", "FFBFFBFRRL", "BBBFFFBRLR", "FBBFFFBRRR", "FFFBFFFLRL", "FFFFBFBLLL", "BBBBFFBLLL", "BBFFFFBLLL", "BBBFBBBLRL", "FBFBFBBLLR", "BFBFFFFLRL", "BFFFFFFRLR", "FFFFFFBRLR", "BFFFFFBLRL", "BBBBFFFLRR", "FBBFBFBRLR", "BFBBBBFLLR", "FBBBBBFLRL", "FFBFFFFRRR", "FBFFBBFLLR", "BBBBFFFLLL", "FBBFFFFLRR", "BBFBBFFRRR", "BFBBBBFRRR", "FBBBFFBRRL", "BBFFFFBLLR", "BBFFFFFRRR", "BBFBFFFLRL", "BFFFBFFLRR", "BBBFBFFLRR", "FFFBBFFRRL", "FFFBFBFLRL", "BFBFFBBLLL", "FFBBFBBLRL", "FBFFFFBLRL", "FFFFBBFLLR", "BFFBBFBLRR", "BFBBBFBRRL", "BBFFFBFLRL", "FFBBBBFRLL", "BFFFBFBRRR", "FBBFBFFRLR", "FBFFFFFLLL", "BBFFBFFRLR", "FBBBBFFRRL", "BFFFBBBRLL", "BBBFFBBRLR", "FBFFBBFRRL", "BBFBBBFLLR", "FFBFFBFLLL", "FBBFFFBRLR", "BBFBBBBRLL", "FBFBBBFLLL", "FBBBBFFLRR", "FBBBFBFRLL", "FFFBBFBRRR", "BBFBFBFLLL", "BFBBBBFRLR", "BBFBFFFRLL", "FBBFBFFLLR", "FFBBBFBRLL", "FBBBFBFRRR", "FBFBFBFRRR", "FBBBFFFLLR", "BBFFFBFRLL", "BBFFBBFLLL", "FFFBFBFLLR", "FFBBFBFLLR", "FBBFBBBLLL", "FBBFBBFRLR", "BFFFFFFLLR", "FBFBBFBLRR", "BBFFBFFLRL", "BFFFFBFRLL", "FBBBBBBLRL", "FFFFFBFRRR", "FBFFBBBRLR", "FBBFFFFLRL", "BBFFBFFLLL", "FFBBFFFRRR", "FFFFBBFLRL", "BBFBFBBLLR", "FBFBFFBLRR", "FBBBFFFRRL", "BFBFFBFRLR", "BFBFBFFRRR", "FBBBFBBLRR", "BBFFBFBRRR", "FFFFFBBRRR", "BBFBFBBRRR", "BFBBFBBLLL", "FFBFFBBRLL", "FBFFBFFLLL", "FFBBFBFRLR", "BBBFBBFLLR", "FBBFBFBLRR", "FFFBBBBLLL", "BBFFFFBRRR", "FBFFBBBLLR", "FBFBFBFRRL", "BBBFFBBLRL", "BBFBFFBRRL", "FBBFFBFRRR", "FBBBBBFRLR", "BFFFFBFLRR", "FBBFBBFLLL", "BFFFBFFRRL", "BBBFFBBRRR", "BBBFBFBLLL", "BFFFBFBLRR", "FBBBFFFRLL", "FBFFFFBRLL", "FBBFFBBLRR", "FFBFFBFLRR", "FBBBFFFRRR", "BFFBFBFRRR", "BBFFBFFRRL", "FFBFFFFLLL", "BFFFBBBLRL", "FBFBFFFRLL", "FBFBFFBRLL", "BBBFBBBLLR", "FFBFBFFRRR", "FBFBBFFRLR", "BBBFBFBRLL", "BFBBBFFLLR", "BBFBFBFRRR", "FBFBBFFRRL", "FFBBBFFLLL", "BBFFFBBRLL", "FBBBFBFLRR", "FBFFBFBLLL", "FFBFBFBLRL", "FFFBFBBRRR", "FBBBBBFRRR", "BFFFBFFLLL", "FFBBBBBRRR", "FFFFFBFRRL", "FBBBFBBRLL", "FBBFBBFLLR", "FBBFFFFRRR", "FFBBBFBRRL", "BFFBFFFLRL", "BFFFFBFRRR", "BFFFFBBLLL", "FBBBBBFLRR", "BFFBBFFRRR", "BFBFBBFLLR", "FFBBBFFRRR", "FFBBFFBRRL", "BFBFFBBLRL", "BFFBFFBLRL", "FFBBBBFLRL", "FFBBFFBRLL", "FBFFBFFLRL", "FFBBBFBLLL", "BBFBBFFRLR", "BBBFBBBLRR", "FFFBBBBRRR", "BFFFFBBLRR", "FFBFFFFLRL", "BFBBBBBLRL", "BBBFBBFRLL", "FBFFFFFRLR", "BBFFFFFRLL", "FBFBFFFLRL", "FFFBFBBRLR", "FBBFBBFRRR", "FBFBBFBRRR", "BBFFFBFRRR", "FFFFBBFRRR", "FFFFBFBLLR", "BFBBFBFLLR", "BBFFBBBRRL", "FFBBFBFRLL", "FBFBFFFLLR", "BFFBBBFRLL", "FBBBBBBRRR", "FBFFBBBRRL", "FFBFBBFLRR", "BFFFBFFRLR", "BFBBBBFLLL", "FFBBFFFRLR", "FFBFBFFLRL"]
#puzzleInput = ["BFFFBBFRRR"]
seatIDList = []


def getSeatID(seat):
	firstPass = re.sub("F|L", "0", seat)
	binSeat = re.sub("B|R", "1", firstPass)
	seatID = (int(binSeat[0:7],2) * 8) + int(binSeat[7:10],2)
	return seatID

for seat in puzzleInput:
	seatIDList.append(getSeatID(seat))



for rowTry in range(1,127):
	for colTry in range(0,8):
		seatTry = rowTry * 8 + colTry
		if seatTry not in seatIDList:
			if seatTry + 1 in seatIDList:
				if seatTry - 1 in seatIDList:
					print seatTry


