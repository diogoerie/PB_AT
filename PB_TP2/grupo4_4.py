def permutations(candidate, remaining, seen=None):
    if seen is None:
        seen = set()

    if remaining == "":
        print(candidate)
        return

    for i in range(len(remaining)):
        if remaining[i] in seen:
            continue
        seen.add(remaining[i])

        new_candidate = candidate + remaining[i]
        new_remaining = remaining[:i] + remaining[i+1:]
        permutations(new_candidate, new_remaining)


permutations("", "AAB")
