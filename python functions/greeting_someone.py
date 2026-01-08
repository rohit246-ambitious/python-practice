def greeting_someone(name):
    """Returns a greeting message for the given name."""
    print(f"Hello, {name}!, good morning")
    print("Have a great day ahead!")


number_of_people = int(input("Enter the number of people you want to greet: "))
for _ in range(number_of_people):
    person_name = input("Enter the name of the person: ")
    greeting_someone(person_name)
    