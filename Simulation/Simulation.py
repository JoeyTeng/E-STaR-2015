#Simulation via formula, parameter of vectors and matrixes.
#--coding:utf-8--
#Vectors:
Population = [] #n
IntrinsicGrowthRate = [] #µ
MaxPopulation = [] #N
DeathRate = [] #λ
ConversionRate = [] #s, σ
#Matrixes:
HistoryPopulation = [] #n(t)
PredationEfficiency = [] #A, α

#Formula:
#n[i][t + 1] = n[i][t] - lambda[i]*n[i][t] + mu[i] * n[i][t] * (1 - n[i][t]/N[i]) 
#   + sigma[i] * SUM(1, j, lambda(i, j): alpha[i][j] * n[i][t] * n[j][t]) 
#   - SUM(i, j, lambda(i, j): alpha[j][i] * n[j][t] * n[i][t])
def Step(Population):
    NewPopulation = []
    for i in range(0, len(Population)):
        NewPopulation[i] = Population[i] - DeathRate[i] * Population[i] + IntrinsicGrowthRate[i] * Population[i] * (1 - Population[i] / MaxPopulation[i])\
            + ConversionRate[i] * Sum(i, (lambda(j): PredationEfficiency[i][j] * Population[i] * Population[j]))\
            - Sum(len(Population), (lambda(j): PredationEfficiency[j][i] * Population[j] * Population[i]))

    return NewPopulation

def Sum(maximum, expression):
    Ans = 0
    for j in range(0, maximum):
        Ans += expression(j)

    return Ans

def Calculation(Steps):
    for t in range(0, Steps):
        Population = HistoryPopulation[t]
        HistoryPopulation.append(Step(Population))

    return HistoryPopulation

def main():
    Calculation(int(raw_input('Please input steps of simulation:')))

    return 0

#--main--

if __name__ == '__main__':
    main()
