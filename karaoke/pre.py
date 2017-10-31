"""
Pre-process POIs from a text file to load onto the map
"""
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)

def process(raw):
    cooked = []
    for line in raw:
        log.debug("Line: {}".format(line))
        line = line.strip()
        if len(line) == 0 or line[0] == "#":
            log.debug("Skipping")
            continue
        elif len(line) != 0:
            line = line.split(",")
            print(line[0] + line[1] + line[2])
            cooked.append((line[0], line[1], line[2]))
        else:
            raise ValueError("Trouble with line: '{}'\n".format(line))
    return cooked

def main():
    f = open("data/POI.txt")
    parsed = process(f)
    print(parsed)


if __name__ == "__main__":
    main()
