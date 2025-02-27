import re

# 1
def match_a_b(s):
    return re.fullmatch(r'ab*', s) is not None

# 2
def match_a_b2_3(s):
    return re.fullmatch(r'ab{2,3}', s) is not None

# 3
def find_lowercase_with_underscore(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)

# 4
def find_upper_followed_by_lower(s):
    return re.findall(r'[A-Z][a-z]+', s)

# 5
def match_a_anything_b(s):
    return re.fullmatch(r'a.*b', s) is not None

# 6
def replace_with_colon(s):
    return re.sub(r'[ ,.]', ':', s)

# 7
def snake_to_camel(s):
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(s.split('_')))

# 8
def split_at_uppercase(s):
    return re.findall(r'[A-Z][^A-Z]*', s)

# 9
def insert_spaces(s):
    return re.sub(r'([A-Z])', r' \1', s).strip()

# 10
def camel_to_snake(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()


if __name__ == "__main__":
    test_strings = ["ab", "a", "abb", "abbb", "a_b", "HelloWorld", "CamelCaseString", "this_is_snake_case"]
    print(match_a_b("ab"))  # True
    print(match_a_b2_3("abb"))  # True
    print(find_lowercase_with_underscore("this_is_a_test"))  # ['this_is', 'a_test']
    print(find_upper_followed_by_lower("HelloWorld"))  # ['Hello', 'World']
    print(match_a_anything_b("axxxb"))  # True
    print(replace_with_colon("Hello, world. This is a test"))  # "Hello:world:This:is:a:test"
    print(snake_to_camel("this_is_snake_case"))  # "thisIsSnakeCase"
    print(split_at_uppercase("SplitAtUppercaseLetters"))  # ['Split', 'At', 'Uppercase', 'Letters']
    print(insert_spaces("InsertSpacesBetweenWords"))  # "Insert Spaces Between Words"
    print(camel_to_snake("CamelCaseString"))  # "camel_case_string"
