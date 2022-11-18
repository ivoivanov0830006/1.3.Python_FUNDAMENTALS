force_side_dictionary = {}

command = input()
while command != "Lumpawaroo":

    # first is the force / second is the user
    if "|" in command:
        split_command = command.split(" | ")
        force_side, force_user = split_command
        user_is_part_of_the_force = False

        # checks if user is in this force
        for value in force_side_dictionary.values():
            if force_user in value:
                user_is_part_of_the_force = True
                break

        # when user is not in this force
        if not user_is_part_of_the_force:
            if force_side not in force_side_dictionary.keys():  # dark side exists, but light - not
                force_side_dictionary[force_side] = [force_user]
            else:
                force_side_dictionary[force_side].append(force_user)

    # first is the user / second is the force
    elif "->" in command:
        split_command = command.split(" -> ")
        force_user, force_side = split_command

        # checks if user is in this force
        for key, value in force_side_dictionary.items():
            if force_user in value:
                force_side_dictionary[key].pop(value.index(force_user))
                break

            # adding previously removed user if it not exist
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = [force_user]
            else:
                force_side_dictionary[force_side].append(force_user)  # if the force exist append the user
            print(f"{force_user} joins the {force_side} side!")
    command = input()

for force_side, force_users in force_side_dictionary.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_user)}")
        for user in force_users:
            print(f"! {user}")
