# PRACTICAL 12: Demonstrating Inheritance and Encapsulation

# Base class
class University:
    def __init__(self, name, year_of_estd, city):
        self.__name = name                # encapsulated (private) attribute
        self.__year_of_estd = year_of_estd
        self.__city = city

    # Getter methods to access encapsulated attributes
    def get_name(self):
        return self.__name

    def get_year_of_estd(self):
        return self.__year_of_estd

    def get_city(self):
        return self.__city


# Derived class: Professor
class Professor(University):
    def __init__(self, name, year_of_estd, city,
                 designation, highest_qualification, area_of_research,
                 year_of_joining, years_of_experience, name_of_institute):
        super().__init__(name, year_of_estd, city)
        self.designation = designation
        self.highest_qualification = highest_qualification
        self.area_of_research = area_of_research
        self.year_of_joining = year_of_joining
        self.years_of_experience = years_of_experience
        self.name_of_institute = name_of_institute

    def display(self):
        print("\n--- Professor Details ---")
        print("University:", self.get_name(), "| Established:", self.get_year_of_estd(), "| City:", self.get_city())
        print("Designation:", self.designation)
        print("Qualification:", self.highest_qualification)
        print("Research Area:", self.area_of_research)
        print("Year of Joining:", self.year_of_joining)
        print("Experience:", self.years_of_experience, "years")
        print("Institute:", self.name_of_institute)


# Derived class: Lab Assistant
class LabAssistant(University):
    def __init__(self, name, year_of_estd, city,
                 highest_qualification, additional_skills,
                 year_of_joining, name_of_institute):
        super().__init__(name, year_of_estd, city)
        self.designation = "Lab Assistant"
        self.highest_qualification = highest_qualification
        self.additional_skills = additional_skills
        self.year_of_joining = year_of_joining
        self.name_of_institute = name_of_institute

    def display(self):
        print("\n--- Lab Assistant Details ---")
        print("University:", self.get_name(), "| Established:", self.get_year_of_estd(), "| City:", self.get_city())
        print("Designation:", self.designation)
        print("Qualification:", self.highest_qualification)
        print("Skills:", self.additional_skills)
        print("Year of Joining:", self.year_of_joining)
        print("Institute:", self.name_of_institute)


# Derived class: Office Assistant
class OfficeAssistant(University):
    def __init__(self, name, year_of_estd, city,
                 highest_qualification, year_of_joining, name_of_institute):
        super().__init__(name, year_of_estd, city)
        self.designation = "Office Assistant"
        self.highest_qualification = highest_qualification
        self.year_of_joining = year_of_joining
        self.name_of_institute = name_of_institute

    def display(self):
        print("\n--- Office Assistant Details ---")
        print("University:", self.get_name(), "| Established:", self.get_year_of_estd(), "| City:", self.get_city())
        print("Designation:", self.designation)
        print("Qualification:", self.highest_qualification)
        print("Year of Joining:", self.year_of_joining)
        print("Institute:", self.name_of_institute)


# Derived class: Peon
class Peon(University):
    def __init__(self, name, year_of_estd, city,
                 qualification, year_of_joining, name_of_institute):
        super().__init__(name, year_of_estd, city)
        self.job_role = "Office Peon"
        self.qualification = qualification
        self.year_of_joining = year_of_joining
        self.name_of_institute = name_of_institute

    def display(self):
        print("\n--- Peon Details ---")
        print("University:", self.get_name(), "| Established:", self.get_year_of_estd(), "| City:", self.get_city())
        print("Job Role:", self.job_role)
        print("Qualification:", self.qualification)
        print("Year of Joining:", self.year_of_joining)
        print("Institute:", self.name_of_institute)


# -------------------------------
# Menu-driven choice
print("Choose role to create:\n1. Professor\n2. Lab Assistant\n3. Office Assistant\n4. Peon")
choice = int(input("Enter choice (1-4): "))

if choice == 1:
    prof = Professor("ABC University", 1990, "Surat",
                     "Professor", "PhD", "AI & ML", 2010, 15, "Engineering Dept")
    prof.display()

elif choice == 2:
    lab = LabAssistant("ABC University", 1990, "Surat",
                       "M.Sc", "Electronics, Networking", 2015, "Science Dept")
    lab.display()

elif choice == 3:
    office = OfficeAssistant("ABC University", 1990, "Surat",
                             "B.Com", 2018, "Admin Dept")
    office.display()

elif choice == 4:
    peon = Peon("ABC University", 1990, "Surat",
                "High School", 2020, "General Services")
    peon.display()

else:
    print("Invalid choice!")