#ArtUnBlocker
import random
#make colour bank
print("ArtUnBlocker by JakeDaSpud [@conor on Artfol]")
print("Feel free to pick and choose what you like! This is just a guide to help with your ArtBlock :)")
colours=("Black", "Blue", "Brown", "Green", "Grey", "Off White", "Orange", "Pink", "Purple", "Red", "White", "Yellow")
adjective=("Light", "Normal", "Dark")
prompt=("Rustic", "Ruined", "Observe", "Spiral", "Clang", "Pillar", "Key", "Chained", "Blocked", "Passage", "Continued", "Vision", "Strength", "Vintage",
        "Love", "Rest", "Pool", "Fountain", "Technology", "Advancement", "Wild", "Toxic", "Destroy", "Festive", "Smooth", "Match", "Spectral", "Frail",
        "Cord", "Shine", "Stars", "Phased", "Disaster", "Layered", "Translucent", "Ethereal", "Particles", "Pipe", "Smoke", "News", "Replacement",
        "Maps", "Aproximation", "Duo", "Humongous", "Rotating", "Ecstasy", "Childhood Candy", "Royalty", "New Heights", "Two Masks", "Boxed",
        "Trapped", "Noise", "Omnipotence", "Puppetmaster", "Down to the wire", "Yearning", "Reluctant", "Failed Plans", "Plant Growth",
        "Yet to meet expectations", "Restraint", "Giant Jar", "Problem", "Addiction", "Collection", "Enabling", "Happy Place", "Beliefs", "Belittle",
        "Six-Legged", "Dialogue", "Dismember", "Ugly Scarf", "Persistance", "Bagged", "Reuse", "Half-Dead", "Afterlife", "Thieved Eggs", "Thief",
        "Sacrifice", "Denied", "Haunted", "Greed", "Evolution", "Sloth", "Death", "Bucket-Hat", "Personalised", "Lust", "Gluttony", "Wrath", "Collision",
        "Depleted", "Indecisive", "Carousel", "Arousal", "Absurd", "Obnoxious", "Basket", "Silver Lining", "Bittersweet", "Sonder", "Suspended", "Spider",
        "Dissociation", "Button", "Serene", "Nonchalant", "Pretty", "Photogenic", "Mechanical", "Tired", "Sleepy", "Smokey", "Underlying", "Captured",
        "Explosion", "Compact", "Expanded", "Trained", "Damaged", "Deranged", "Dissolved")
#Count how many elements are in Prompt
prompt_count=len(prompt)
print("Prompt count:", prompt_count)
print()
print("Your primary colour is", random.choice(adjective), random.choice(colours))
print("Your secondary colour is", random.choice(adjective), random.choice(colours))
print("Your tertiary colour is", random.choice(adjective), random.choice(colours))
print("Your prompt is", random.choice(prompt))