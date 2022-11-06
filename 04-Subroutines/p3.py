def f(amount_to_pay):
    a=amount_to_pay

    piec=a//5
    reszta=a%5
    dwa=reszta//2
    jeden=reszta%2

    c=(piec+dwa+jeden)
    return c