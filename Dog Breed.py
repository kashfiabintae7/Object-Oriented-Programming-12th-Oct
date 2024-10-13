class DogBreed: 

    
    def __init__ (self, characteristics, anger_level, origin, height, weight, known_for):
        self.characteristics = characteristics
        self.angerlevel = anger_level 
        self.origin = origin
        self.height = height
        self.weight = weight
        self.knownfor = known_for
        


Bloodhound = DogBreed("(Hounds) large-sized; loose skin with folds around head and neck; eyes set deep in orbits",
                     "9 out of 10", "Belgium/France", "25–27 (23–25)", "90–110 (80–100)",
                     "Bloodhounds are known for their tracking abilities; first recorded use by organized law enforcement, England, 1805.")


Fox_Terrier = DogBreed("(Terriers) folded ears; white with black or black-and-tan markings",
                     "5 out of 10", "England", "maximum 15 (slightly smaller)", "18(16)",
                     "noted for its remarkable eyesight and keen nose; also wire-coat variety.")


Doberman_Pinscher = DogBreed("(Working Dogs) medium-sized; sleek, muscular body; typically erect ears",
                     "8 out of 10", "Germany", "26–28 (24–26)", "60–88",
                     "Doberman Pinschers are known for being a intelligent breed; quick learners.")


Australian_Shepherd = DogBreed("(Herding Dogs) medium-sized; lithe and agile; moderate-length coat; bobbed tail",
                     "7 out of 10", "United States", "20–23 (18–21)","35–70",
                     "they're known for being descended from shepherd dogs of Basque region (Spain/France).")


Papillon = DogBreed("(Toys) fine-boned and dainty; long, silky coat",
                     "2 out of 10", "France/Belgium", "8–11", "maximum 11",
                     "Papillons were known for and named after ears that resemble butterfly wings.")



print(f"The Characteristics of Bloodhounds: {Bloodhound.characteristics}\n\nAnger Level: {Bloodhound.angerlevel}\n\nPlace of Origin: {Bloodhound.origin}\n\nHeight (inches): {Bloodhound.height}\n\nWeight (pounds): {Bloodhound.weight}\n\nKnown for: {Bloodhound.knownfor}\n\n\n")

print(f"The Characteristics of Fox Terrier: {Fox_Terrier.characteristics}\n\nAnger Level: {Fox_Terrier.angerlevel}\n\nPlace of Origin: {Fox_Terrier.origin}\n\nHeight (inches): {Fox_Terrier.height}\n\nWeight (pounds): {Fox_Terrier.weight}\n\nKnown for: {Fox_Terrier.knownfor}\n\n\n")

print(f"The Characteristics of Doberman Pinscher: {Doberman_Pinscher.characteristics}\n\nAnger Level: {Doberman_Pinscher.angerlevel}\n\nPlace of Origin: {Doberman_Pinscher.origin}\n\nHeight (inches): {Doberman_Pinscher.height}\n\nWeight (pounds): {Doberman_Pinscher.weight}\n\nKnown for: {Doberman_Pinscher.knownfor}\n\n\n")

print(f"The Characteristics of Australian Shepherd: {Australian_Shepherd.characteristics}\n\nAnger Level: {Australian_Shepherd.angerlevel}\n\nPlace of Origin: {Australian_Shepherd.origin}\n\nHeight (inches): {Australian_Shepherd.height}\n\nWeight (pounds): {Australian_Shepherd.weight}\n\nKnown for: {Australian_Shepherd.knownfor}\n\n\n")

print(f"The Characteristics of Papillon: {Papillon.characteristics}\n\nAnger Level: {Papillon.angerlevel}\n\nPlace of Origin: {Papillon.origin}\n\nHeight (inches): {Papillon.height}\n\nWeight (pounds): {Papillon.weight}\n\nKnown for: {Papillon.knownfor}\n\n\n")
