# Bei der Körpergröße handelt es sich um ein annähernd
# normalverteiltes Merkmal. Das bedeutet: Misst man die
# Körpergröße einer größeren Zahl erwachsener deut-
# scher Männer, so beträgt der Mittelwert ca. 178 cm. Um
# diesen Mittelwert herum verteilen sich die meisten
# Messwerte. Häufig findet sich die Angabe, wieviel Pro-
# zent der Messwerte innerhalb einer bestimmten Stan-
# dardabweichung liegen. Die Standardabweichung gibt
# dabei an, wie stark die Messwerte von dem Mittelwert
# abweichen und berechnet sich anhand feststehender
# mathematischer Formeln.

# Frauen:
# Mittelwert: 166
# Sigma: 9

# Männer:
# Mittelwert: 177,8
# Sigma: 6.1

# Aufgabe: Erstelle zwei Listen von 10000 zufälligen männlichen sowie weiblichen Körpergrößen.
# Schreibe dazu die nötigen Funktionen und plotte die Histogramme.
# Berechne jeweils Median und Mittelwert. Nutze dazu das statistics Modul


import random
import matplotlib.pyplot as plt
import statistics


N = 10000

MU_WOMEN = 166
SIGMA_WOMEN = 9

MU_MEN = 177.8
SIGMA_MEN = 6.1


def get_normal(mu, sigma):
    """Return random sample of gaussian distribution with given mu and sigma"""

    return random.gauss(mu, sigma)


def get_sizes(n, mu, sigma):
    """Call get_normal n times for mu and sigma."""

    return [get_normal(mu, sigma) for _ in range(n)]


def get_data(n, mu, sigma):
    """Return dict with random samples, median and average"""

    rand_samples = get_sizes(n, mu, sigma)

    return {
        "rand_samples": rand_samples,
        "median": statistics.median(rand_samples),
        "average": statistics.mean(rand_samples)
    }


def create_histogram(data, label, text_x_coord):
    rand_samples = data.get("rand_samples")
    median = data.get("median")
    average = data.get("average")

    plt.hist(rand_samples, bins=200, alpha=0.7, label=label)

    plt.axvline(median, color="#000", linewidth=1)
    plt.axvline(average, color="#000", linestyle='dashed', linewidth=1)
    
    plt.text(
        text_x_coord, 140,
        f"Mittelwert ({label}): {median:3.2f} \
        \nMedian ({label}): {average:3.2f}")


def main():

    data_women = get_data(N, MU_WOMEN, SIGMA_WOMEN)
    data_men = get_data(N, MU_MEN, SIGMA_MEN)

    plt.subplots(figsize=(12, 8))

    create_histogram(data_women, "Frauen", 185)
    create_histogram(data_men, "Männer", 140)

    plt.xlabel("Körpergröße")
    plt.ylabel("Menschenanzahl")

    plt.legend()
    plt.show()

main()
