
def students_credits(*args):
    NEEDED_CREDITS = 240
    earned_credits = 0
    course_info = {}
    for el in args:
        course_name, credits, max_test_points, diyan_points = [int(x) if x.isdigit() else x for x in el.split("-")]
        credits_earned = credits * (diyan_points / max_test_points * 100) / 100
        earned_credits += credits_earned

        course_info[course_name] = course_info.get(course_name, credits_earned)

    result = ""
    if earned_credits >= NEEDED_CREDITS:
        result += f"Diyan gets a diploma with {earned_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {NEEDED_CREDITS - earned_credits:.1f} credits more for a diploma.\n"


    for key, value in sorted(course_info.items(), key=lambda x: -x[1]):
        result += f"{key} - {value:.1f}\n"
        earned_credits += value


    return result.strip()

