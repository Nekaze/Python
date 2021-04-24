def remove_anagrams(array):
    normalized_array = []
    for i in array:
        normalized_array.append("".join(sorted(i.lower())))

    for j in range(len(array)):
        for k in range(len(array)):
            if (j != k) and normalized_array[j] == normalized_array[k]:
                del array[k]
                return

def main():
    strings = ['code', 'doce', 'ecod', 'framer', 'frame', 'fraem', 'poop', 'ppoo', 'sapo', 'sOpa']
    print(strings)

    for i in range(len(strings)):
        remove_anagrams(strings)

    print(sorted(strings))


if __name__ == "__main__":
    main()
