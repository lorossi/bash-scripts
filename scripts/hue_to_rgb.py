# this script generates the colors array for the bash script
# it is not necessary to run this script, the colors array is already generated


def hue_to_rgb(hue: float) -> list[float, float, float]:
    kr = (5 + hue * 6) % 6
    kg = (3 + hue * 6) % 6
    kb = (1 + hue * 6) % 6

    r = int((1 - max(min(kr, 4 - kr, 1), 0)) * 255)
    g = int((1 - max(min(kg, 4 - kg, 1), 0)) * 255)
    b = int((1 - max(min(kb, 4 - kb, 1), 0)) * 255)
    return [r, g, b]


def main():
    MAX = 512
    out = "colors=( "
    for i in range(0, MAX):
        r, g, b = hue_to_rgb(i / MAX)
        out += f'"\\033[38;2;{r};{g};{b}m" '
    out += f")\nmax_colors={MAX}"

    print(out)


if __name__ == "__main__":
    main()
