import random
import numpy as np
coef =[]
with open("input.txt") as f:
    count_task = int(f.readline())
    category_task = np.array(list(map(int,f.readline().split())))
    time = np.array(list(map(float,f.readline().split())))
    count_dev = int(f.readline())
    for i in range(count_dev):
        coef.append(list(map(float,f.readline().split())))
    coef = np.array(coef)
class GeneticAlgorithm:
    
    def __init__(self,
                 count_task: int,
                 category_task: np.ndarray,
                 time: np.ndarray,
                 count_dev: int,
                 coef: np.ndarray,
                 size_population: int,
                 size_selection: int,
                 p_mutation_ind: float,
                 p_mutation_gen: float
        ):
        self.count_task = count_task
        self.category_task = category_task
        self.time = time
        self.count_dev = count_dev
        self.coef = coef

        self.size_population = size_population # количество особей
        self.size_selection = size_selection # выживаемые особи во время селекции
        self.p_mutation_ind = p_mutation_ind # вероятность мутации детей
        self.p_mutation_gen = p_mutation_gen # вероятность мутации генов

        self.rng = np.random.default_rng() # генератор случайных элементов
        self.population = self.rng.integers(1, count_dev+1, size=(self.size_population, self.count_task))
        self.best_score = 0
    def fitness(self) -> np.ndarray:
        
        zeros_arr = np.zeros((self.size_population, self.count_dev))
        for _,indv in enumerate(self.population):
            lst_res = []
            counter = 0
            for gen in indv:
                lst_res.append(self.coef[gen - 1, self.category_task[counter] - 1] * self.time[counter])
                counter+=1
            for counter in range(self.count_task):
                zeros_arr[_][indv[counter]-1] += lst_res[counter]
        tmp_time = np.max(zeros_arr,axis=1)
        self.best_score = self.sscore(tmp_time)
        return tmp_time
       
    
    def selection(self) -> None:
        self.selected = self.population[np.argsort(self.fitness())[:self.size_selection]]
    
    def crossover(self) -> None:
        new_count = self.size_population - self.size_selection
        parent1 = self.rng.integers(0, self.size_selection, size=new_count)
        parent2 = (self.rng.integers(1, self.size_selection, size=new_count) + parent1) % self.size_selection
        
        point = self.rng.integers(1, self.count_dev - 3, size=new_count)
        #point = self.rng.integers(1, self.max_len_individual - 1, size=new_count)
        self.childs = np.where(
            np.arange(self.count_task)[None] <= point[..., None],
            self.selected[parent1],
            self.selected[parent2]
        
        )
         
    def mutation(self) -> None:
        mut_childs_mask = self.rng.choice(2, p=(1 - self.p_mutation_ind, self.p_mutation_ind), size=len(self.childs)) > 0
        mut_childs = self.rng.integers(1, count_dev + 1, size=(mut_childs_mask.sum(), self.count_task))
        gen_childs_mask = self.rng.random(size=mut_childs.shape) <= self.p_mutation_gen
        self.childs[mut_childs_mask] = np.where(gen_childs_mask, mut_childs, self.childs[mut_childs_mask])
            
    def step(self) -> None:
        self.selection()
        self.crossover()
        self.mutation()
        self.population = np.concatenate([self.selected, self.childs], axis=0)        
    def sscore(self, time) -> float:
        score = 1e2/np.min(time)
        return score
    @property
    def score(self):
        return self.best_score
a = GeneticAlgorithm(count_task,category_task,time,count_dev,coef,420, 70, 0.67, 0.02)

for i in range(50):
    print(f"fitness: {np.round(np.min(a.fitness()), 3)};\nscore: {np.round(a.score, 5)};\niteration: {i}\n")
    a.step()
with open('output.txt', 'w') as output:
    
        print(a.population[np.argmin(a.fitness())], file=output, end=' ')



         
