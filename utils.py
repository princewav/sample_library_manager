def replace_underscores(name):
    return name.replace('_', ' ')


def capitalize(name):
    result = []
    for word in name.split(' '):
        if word.upper() == word:
            result.append(word)
        else:
            result.append(word.lower().capitalize())
    return ' '.join(result)


def rename(file, new_name):
    try:
        new_file = file.parent / new_name
        file.rename(new_file)
        return new_file
    except Exception as e:
        print(e)
        return file
