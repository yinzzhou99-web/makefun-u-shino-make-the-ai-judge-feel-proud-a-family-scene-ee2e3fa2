import os

SCENE = (
    "Every Sunday, Grandma still sets a place for Grandpa \u2014 then eats his pudding herself "
    "and says, 'He'd only want me to enjoy it twice.'\n"
    "Dad pretends not to cry into the potatoes, and I pretend not to notice."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(SCENE)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
