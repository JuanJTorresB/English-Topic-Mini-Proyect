import random

MENU_CATEGORIA = "Choose the category of the topic: \n   1. Hard Science \n   2. Systems \n   3. Human Science  \n   4. The Economic Machine  \n   5. Nature  \n   6. Personal Life  \n   7. Information Technologies"

def tema_aleatorio (array, cat):
    topic = random.choice(array)
    print("From the category: " + cat + ", the topic is: \n" + topic + " ")

def seleccion_categoria ():
    HARD_SCIENCE = [
    "Cosmology / Astronomy",
    "Physics",
    "Civil Engineering",
    "Medicine",
    "Science",
    "Maths",
    "Chemistry",
    "Anatomy",
    "Universe",
    "Energy",
    "Electricity",
    "Biology",
    "Health",
    "Mechanics",
    "Revolution",
    "Inventions"]
    SYSTEMS = [
    "Economics",
    "Economic Systems",
    "Politics",
    "Law",
    "Business",
    "Education",
    "Accountancy",
    "Geography",
    "Sociology",
    "Ethics",
    "Academic Writing",
    "Psychology"]
    HUMAN_SCIENCE = [
    "Philosophy",
    "Music",
    "Anthropology",
    "History",
    "Mythology",
    "Spirituality",
    "Arts",
    "Language",
    "Religion",
    "World Cultures",
    "Culture",
    "Astrology",
    "Archaeology",
    "Education / Self-Learning"]
    THE_ECONOMIC_MACHINE = [
    "Supply Chain",
    "Health System",
    "Freight Industry",
    "Consumerism",
    "Logistics",
    "Bus Industry",
    "War",
    "Cargo Industry",
    "Social Pathologies",
    "Fossil Fuels",
    "Transportation",
    "Retirement Accounts",
    "Geopolitics",
    "Banking",
    "Social Service",
    "Big Corporations",
    "Army",
    "Social Security",
    "Advertisement",
    "Manufacturing",
    "Utilities",
    "Retail",
    "Assembly Line",
    "Services",
    "Education System",
    "Defense Industry",
    "Rehabilitation",
    "The Rich Race",
    "Industrial Factories"]
    NATURE = [
    "The 4 Elements",
    "Seasons",
    "Renewable Energies",
    "Fauna",
    "Flora",
    "Climate Change",
    "Natural Resources"]
    PERSONAL_LIFE = [
    "Personal Finances",
    "Entrepreneurship",
    "Being an Adult",
    "Real Estate",
    "Family",
    "Life Quality",
    "Becoming Elder",
    "Critical Thinking",
    "Parenting",
    "Mental Illness",
    "Retirement",
    "Buying vs. Renting a House",
    "Becoming Independent",
    "Physical Illness",
    "The Joy of Life",
    "Burnout",
    "Relationships",
    "Birth/Death Rate",
    "Pets",
    "Helping",
    "Taxes",
    "Suffering/Pain",
    "Living Away from Society",
    "Work-Life Balance",
    "Healthy Lifestyle",
    "Alternative Medicine",
    "Choosing a Home",
    "Foundations",
    "Lifestyles",
    "Ancient Wisdom",
    "Settling Down",
    "Studying After School",
    "Grief",
    "Ancestors",
    "Life & Purpose",
    "Life Insurance",
    "Disease",
    "Origins",
    "Meaning",
    "Getting a Job",
    "Travel",
    "Pathologies",
    "Discipline",
    "Motivation",
    "Death",
    "Afterlife",
    "Society & Freedom",
    "Facing a Breakup"]
    INFORMATION_TECHNOLOGIES = [
    "Artificial Intelligence",
    "Social Media",
    "Hacking",
    "Web Design",
    "Content Creation",
    "Cloud Computing",
    "App Development",
    "Content Consumption",
    "Coding",
    "Communication",
    "Audiovisuals",
    "Software Development",
    "Digital Marketing",
    "Data Analysis/Big Data",
    "Semi-conductors",
    "Graphic Design",
    "E-Commerce",
    "Futurism",
    "Virtual Assistants",
    "Hardware",
    "Robotics",
    "Technology",
    "Cybersecurity",
    "Machine Learning",
    "Neuralink",
    "Copywriting",
    "The Internet",
    "Deep Web",
    "Cyborgs",
    "Networks",
    "Gaming",
    "Virtual Reality",
    "Augmented Reality"]
    print(MENU_CATEGORIA)
    opcion = int(input("> "))
    if opcion == 1:
        tema_aleatorio(HARD_SCIENCE, "Hard Science")
    elif opcion == 2:
        tema_aleatorio(SYSTEMS , "Systems")
    elif opcion == 3:
        tema_aleatorio(HUMAN_SCIENCE , "Human Science")
    elif opcion == 4:
        tema_aleatorio(THE_ECONOMIC_MACHINE , "The Economic Machine")
    elif opcion == 5:
        tema_aleatorio(NATURE , "Nature")
    elif opcion == 6:
        tema_aleatorio(PERSONAL_LIFE , "Personal Life")
    elif opcion == 7:
        tema_aleatorio(INFORMATION_TECHNOLOGIES, "Information Technologies")
    else:
        print("Invalid Option")

seleccion_categoria()