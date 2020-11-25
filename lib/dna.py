from lib.config_load import Value
from random import shuffle, sample
from random import randrange as rr


def rotate(list, number):
    return list[number:] + list[:number]


def swap(list):
    index = range(len(list))
    i1, i2 = sample(index, 2)
    list[i1], list[i2] = list[i2], list[i1]
    return list


class Individual:
    def __init__(self, gene):
        self.gene = gene
        self.phenotype = self.phenotype()
        self.score = self.score()
        self.fitness = self.fitness()

    def phenotype(self):
        return list(map(lambda tuple: rotate(Value.triangles[tuple[0]], tuple[1]), self.gene))

    def score(self):
        score_list = []
        for i in range(len(Value.letters)):
            score_list.append(
                abs(sum([self.phenotype[k[0]][k[1]] for k in Value.pos[i]]) - Value.letters[i]))
        return int(sum(score_list))

    def fitness(self):
        if self.score == 0:
            return 0
        else:
            return int(1 * 2 * 3 * 4 * 5 / (self.score))

    @classmethod
    def from_random(cls):
        random_gene = [(x, rr(0, 3)) for x in range(20)]
        shuffle(random_gene)
        return cls(random_gene)

    def __add__(self, partner):
        c = []
        for i in range(20):
            c.append((self.gene[i][0], partner.gene[i][1]))
        return Individual(c)

    def __str__(self):
        instructions = ''
        for m in range(20):
            instructions += f'''{self.phenotype[m]} ---with--- {Value.faces[m]}\n'''
        return instructions

    def __repr__(self):
        return str(self.phenotype)


class Generation:
    def __init__(self, population, elite_number=5):
        self.elite_number = elite_number
        self.population = population
        self.population_score = self.population_score()
        self.min_score = min(self.population_score)
        self.min_individual = self.population[self.population_score.index(self.min_score)]
        self.mating_pool = self.mating_pool()

    @classmethod
    def populate(cls, population_number):
        return cls([Individual.from_random() for i in range(population_number)])

    def population_score(self):
        return [i.score for i in self.population]

    def mating_pool(self):
        if self.min_score == 0:
            return None
        else:
            pool = []
            for i in range(self.elite_number):
                pool.append(self.min_individual)

            for ind in self.population:
                for i in range(ind.fitness):
                    pool.append(ind)

            return pool

    def update(self):
        for i in range(len(self.population)):
            daddy = self.mating_pool[rr(0, len(self.mating_pool))]
            mommy = self.mating_pool[rr(0, len(self.mating_pool))]
            self.population[i] = daddy + mommy
            if rr(0, Value.mutation_inverse) == 1:
                self.population[i] = Individual(swap(self.population[i].gene))
        return Generation(self.population)
