from math import factorial as f


class Urna:
    def __init__(self, white_ball, black_ball):
        self.white_ball = white_ball
        self.black_ball = black_ball

    def __str__(self) -> str:
        return f"{self.white_ball * 'Б'} {self.black_ball * 'Ч'}"

    def __add__(self, other):
        self.white_ball += other.white_ball
        self.black_ball += other.black_ball
        return self

    def add_white_ball(self):
        self.white_ball += 1

    def add_black_ball(self):
        self.black_ball += 1

    def remove_white_ball(self):
        self.white_ball -= 1
    
    def remove_black_ball(self):
        self.black_ball -= 1


class Sample(Urna):
    def __init__(self,  white_ball, black_ball, removed_ball):
        Urna.__init__(self, white_ball, black_ball)
        self.removed_ball = removed_ball
    
    def __str__(self) -> str:
        return Urna.__str__(self) + f' (вийнято: {self.removed_ball})'

    def all_balls(self):
        return self.black_ball + self.white_ball

    def probability_white(self):
        p = 0
        if (self.removed_ball > self.black_ball):
           return p
        else:
            a = f(self.black_ball) / (f(self.black_ball - self.removed_ball)\
                 * f(self.removed_ball))
            b = f(self.all_balls())/ (f(self.all_balls() - self.removed_ball)\
                 * f(self.removed_ball))
            p = a / b
            return p

    def __lt__(self, other): 
        return self.probability_white() < other.probability_white()


class Experiments():
    def __init__(self, samp_list = []):
        self.samp_list = samp_list
    
    def __add__(self, elem):
        self.samp_list.append(elem)

    def __str__(self) -> str:
        s = 'Експерименти:\n'
        for elem in self.samp_list:
            s += str(elem) + '\n'
        return s
     
    def max_probability(self):
        self.samp_list.sort(reverse = True)


