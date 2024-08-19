import datetime


def commission(cost, k):
    st = 0.3  # % от покупки или продажи
    st1 = 0.01  # руб минимальная ставка комиссии
    x = 0.0
    if st * cost * k / 100 > st1:
        x = st * cost * k / 100
    else:
        x = st1
    return round(x, 2)


print("Расчет рентабельности продажи акций.")
buy = float(input("Цена акции при покупке: "))
n = int(input("Количество при покупке: "))
a = commission(buy, n)  # Расчет комиссии при покупке
c = float(input("Общая сумма дополнительной комиссии: "))
proc = float(input("Желаемый доход (%): "))
i = float(input("Инфляция (%): "))

date_in = input("Дата приобретения акций: ")
d_in = int(date_in[0] + date_in[1])
m_in = int(date_in[3] + date_in[4])
y_in = int(date_in[6] + date_in[7] + date_in[8] + date_in[9])
now = datetime.datetime.now()

day = now.day - d_in
month = now.month - m_in
year = now.year - y_in

inf = i * year + (i / 12) * month + (i / 365.25) * day

sale0 = (((a + c) / (n * 0.87)) + buy) * (1 + inf / 100) * (1 + proc / 100)
b = commission(sale0, n)
sale = (((a + b + c) / (n * 0.87)) + buy) * (1 + inf / 100) * (1 + proc / 100)
profit = (0.87 * n * (sale - buy) - a - c) * (1 + inf / 100) * (1 + proc / 100)

print("Акция должна стоить: ", sale)
print("Сумма комиссий: ", a + b + c)
print("Доход составит: ", profit)
