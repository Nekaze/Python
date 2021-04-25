def remove_anagrams(array):
    result = {}
    for i in array:
        normalized_key = normalize_and_clear_numbers(i)
        if normalized_key != None and normalized_key not in result:
            result[normalized_key] = i
    return(result.values())

def normalize_and_clear_numbers(string):
    try:
        if not string.isdigit():
            return("".join(sorted(string.lower())))
    except:
        pass

def main():
    strings = [1234, "1234", 'code', 'doce', 'ecod', 'framer', 'frame', 'fraem', 'sapo', 'sOpa']
    print(sorted(remove_anagrams(strings)))

if __name__ == "__main__":
    main()
