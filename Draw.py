#Στον παρακάτω κώδικα θέλουμε να φτιάξουμε μια κλήρωση 
#Σε αυτήν την κλήρωηση ο χρήστης θα δίνει κάποια ονόματα
#Και έπειτα αν συνδεθεί με το όνομα του θα του δώσει ένα τυχαίο όνομα απο τα ονόματα που έδωσε πρίν

import random
name_list = [] # Λίστα με τα ονόματα που εισάγει ο χρήστης
draw_list = [] # Λίστα με τα ονόματα που θα δωθούν στον κάθε χρήστη μετά την κλήρωση

print('Δώστε έναν αριθμό για τα άτομα που θα συμμετέχουν στην κλήρωση:')
while True:
    number = input('')
    if number.isdigit():  # Ελέγχει αν αυτό που εισάγει είναι string που περιέχει μόνο αριθμούς
        number = int(number)  # Το μετατρέπει σε integer
        break
    else:
        print('Αυτό που δώσατε δεν είναι αριθμός. Δώστε έναν αριθμό για τα άτομα που θα συμμετέχουν στην κλήρωση:')

print (f'Τώρα δώσε το κάθε όνομα απο τα {number} άτομα που θα συμμετέχουν στην κλήρωηση:')
name_list = []
for _ in range(number):
    name = input('Δώσε όνομα: ').strip()
    name_list.append(name)

# Δημιουργούμε τη λίστα των αντιστοιχίσεων
draw_list = name_list[:]
random.shuffle(draw_list)  # Ανακατεύουμε τη λίστα

# Βεβαιωνόμαστε ότι κανείς δεν παίρνει το δικό του όνομα
while any(name_list[i] == draw_list[i] for i in range(number)):
    random.shuffle(draw_list)

# Ενημερώνουμε κάθε άτομο ξεχωριστά για το ποιον του έτυχε
assignments = {name_list[i]: draw_list[i] for i in range(number)}

print("\nΗ κλήρωση ολοκληρώθηκε! Τώρα κάθε άτομο μπορεί να δει ποιον του έτυχε.")
for name in name_list:
    input(f"\n{name}, πάτα Enter για να δεις ποιον θα πάρεις δώρο.")
    print(f'Σου έτυχε το άτομο: {assignments[name]}')
    input("Πάτα Enter για να καθαριστεί η οθόνη και να μην δεί κανένας ποιόν έτυχες!")
    print("\033[H\033[J", end="")  # Καθαρίζει την οθόνη (λειτουργεί σε πολλά terminals)

print("Καλή επιτυχία με τα δώρα σας!")

print("This is a new feature to the code!")
print("Amazing!")
