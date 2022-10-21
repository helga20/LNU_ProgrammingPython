from Urna_func import Experiments, Urna, Sample


urna1 = Urna(3, 4)
print("Урна 1:", urna1)
urna2 = Urna(2, 5)
print("Урна 2:", urna2)
print("Додавання до 1 урни білої кульки:",urna1)
urna1.add_black_ball()
print("Додавання до 1 урни чорної кульки:", urna1)
urna2.remove_white_ball()
print("Вилучення з 2 урни білої кульки:", urna2)
urna2.remove_black_ball()
print("Вилучення з 2 урни чорної кульки:", urna2)
urna1 + urna2
print("Додавання до 1 урни усі кульки з 2:", urna1)
urna1.add_white_ball()
print("---------------------------------------")

s1 = Sample(3, 4, 2)
print("Вибірка:", s1)
print("Ймовірність отримання хоча б однієї білої:",s1.probability_white())
s2 = Sample(1, 5, 3)
print("Вибірка:", s2)
print("Ймовірність отримання хоча б однієї білої:", s2.probability_white())
s3 = Sample(4, 9, 4)
print("Вибірка:", s3)
print("Ймовірність отримання хоча б однієї білої:",s3.probability_white())
print("---------------------------------------")

sample_list = Experiments()
for item in [s1, s2, s3]:
    sample_list + item
print(sample_list)

sample_list.max_probability()
print("Топ-N вибірок: \n", sample_list)


