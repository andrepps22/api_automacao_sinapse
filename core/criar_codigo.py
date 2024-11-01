

def criar_codigo(codigo):
    import random
    match codigo:
        case "Corretor":
            return "COR"+str(random.randint(10000, 99999))
        case "Proprietario":
            return "PRO"+str(random.randint(10000, 99999))
        case "Apartamento":
            return "APT"+str(random.randint(10000, 99999))
        case "Casa":
            return "CAS"+str(random.randint(10000, 99999))
        case "Sobrado":
            return "SOB"+str(random.randint(10000, 99999))
        case "Kitinet":
            return "KIT"+str(random.randint(10000, 99999))
        case "Terreno":
            return "TER"+str(random.randint(10000, 99999))
        

