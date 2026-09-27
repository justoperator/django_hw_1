from django.http import HttpResponse


def factorial(req, n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return HttpResponse(f"Факторіал числа {n}: {result}")
