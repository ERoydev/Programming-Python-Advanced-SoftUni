class NameTooShortError(Exception):
    pass

class MustCointainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = [".com", '.bg', '.org']

while True:
    command = input()
    if command == "End":
        break

    if "@" not in command:
        raise MustCointainAtSymbolError("Email must contain @")

    if len(command.split("@")[0]) <= 4:
        raise  NameTooShortError("Name must be more than 4 characters")

    if "." + command.split(".")[-1] not in ['com', 'bg', 'org']:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")