
def team_lineup(*args):
    final = {}
    for name, country in args:
        final[country] = final.get(country, [])
        final[country].append(name)

    result = ("")
    for key, value in sorted(final.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{key}:"
        for i in value:
            result += f"\n  -{i}"

        result += "\n"

    return result.strip()



print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))



from unittest import TestCase, main


class Test(TestCase):
    def test_example_input(self):
        result = team_lineup(
            ("Harry Kane", "England"),
            ("Manuel Neuer", "Germany"),
            ("Raheem Sterling", "England"),
            ("Toni Kroos", "Germany"),
            ("Cristiano Ronaldo", "Portugal"),
            ("Thomas Muller", "Germany")
        )
        expected = """Germany:
  -Manuel Neuer
  -Toni Kroos
  -Thomas Muller
England:
  -Harry Kane
  -Raheem Sterling
Portugal:
  -Cristiano Ronaldo"""

        self.assertEqual(result.strip(), expected)


if __name__ == '__main__':
    main()