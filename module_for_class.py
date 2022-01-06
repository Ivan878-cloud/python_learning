#=============class worker=============


class brigada():
    """Class to create vacation for brigada"""
    def __init__(self, name, education, experience):
        """Initate our workers"""
        self.name = name
        self.education = education
        self.experience = experience
        self.health = 100

    def show_worker(self):
        """Print parametres of workers"""
        discription = (self.name + " education is " + self.education + " experience: " + str(self.experience) + " helth is " + str(self.health)).upper()
        print(discription)

    def experience_up(self):
        """Upgrade experience"""
        self.experience += 1

    def move(self):
        """Start work"""
        print("Worker " + self.name + " start working...")

    def set_health(self, new_health):
        self.health = new_health

#===========HEAD WORKER================


class head_worker(brigada):
    """"Class to create head_worker"""
    def __init__(self, name, education, experience, meneg_skills):
        """Initiate meneg_skills"""
        super().__init__(name,education,experience)
        self.meneg_skills = meneg_skills
        self.meneg = 10

    def learning(self):
        """Learning skills"""
        self.meneg += 20

    def show_worker(self):
        discription = (self.name + " education is " + self.education + " experience: " + str(
            self.experience) + " helth is " + str(self.health) + " meneger skills: " + str(self.meneg)).upper()
        print(discription)
