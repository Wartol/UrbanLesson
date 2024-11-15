call = 0
def count_calls():
    global call
    call = call + 1
def string_info(ThatString):
    info_tuple = len(ThatString), ThatString.upper(), ThatString.lower()
    count_calls()
    return info_tuple
def is_contains(issring,list_to_search):
    count_calls()
    lowerlist = list(map(str.lower, list_to_search))
    while list_to_search:
        if issring.lower() == lowerlist[len(list_to_search)-1]:
            return True
        else:
            return False
print(string_info("Capybara"))
print(string_info("PanamaNaGolovyNaglovo"))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('Jopa', ['jOPA', 'NeJopa', 'jopaBolb']))
print(call)