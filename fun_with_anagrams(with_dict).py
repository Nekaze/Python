def remove_anagrams(array):
    result = {}
    for i in array:
        normalized_key = normalize_and_clear_numbers(i)
        if normalized_key != None and normalized_key not in result:
            result[normalized_key] = i
    return(result.values())

def normalize_and_clear_numbers(string):
    if not string.isdigit():
        return("".join(sorted(string.lower())))

def main():
    strings = ['code', 'doce', 'ecod', 'framer', 'frame', 'fraem', 'sapo', 'sOpa']
    print(sorted(remove_anagrams(strings)))

if __name__ == "__main__":
    main()
