"""
Pre-process POIs from a text file to load onto the map
"""
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)

def process(raw):
   """
   Add pertinent info here
   """
    field = None
    entry = {}
    cooked = []
    for line in raw:
        log.debug("Line: {}".format(line))
        line = line.strip()
        if len(line) == 0 or line[0] == "#":
            log.debug("Skipping")
            continue
        parts = line.split(':')
        if len(parts) == 1 and field:
            entry[field] = entry[field] + line + " "
            continue
        if len(parts) == 2:
            field = parts[0]
            content = parts[1]
        else:
            raise ValueError("Trouble with line: '{}'\n".format(line) +
                             "Split into |{}|".format("|".join(parts)))

	if entry:
            cooked.append(entry)

	return cooked

def main():
    f = open("data/POI.txt")
    parsed = process(f)
    print(parsed)


if __name__ == "__main__":
    main()
