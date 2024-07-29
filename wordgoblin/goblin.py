def check_strings(string1, string2):
    """This is a helper function for comparing strings."""
    """It checks if the first string only contains characters that are also in the second string."""
    if set(string1) <= set(string2):
        if set(string1) < set(string2): 
                pass
        else:
            return string2


def check_dict(*args):
    """Checks a string against a .json dictionary of words."""
    match_list = []
    
    if not args:
        print('Please supply a string of letters!')
    elif len(args) < 2:
        import importlib.resources
        import os
        dict_path = os.path.join(os.path.dirname(__file__), 'data')
        dict_filename = dict_path + "/en_dict.json"

        import json
        string_to_match = args[0]

        with open(dict_filename) as f:
            sample_dict = json.load(f)

        for key in sample_dict:
            checked_var = check_strings(string_to_match, key)
            if checked_var is not None:
                match_list.append(checked_var)

        return match_list

    elif len(args) == 2:
        if isinstance(args[1], int):
            # Our second argument is the number of letters limit we set
            num_of_letters_in_word = args[1]
            import json
            string_to_match = args[0]

            import os.path
            dict_path = os.path.join(os.path.dirname(__file__), 'data')
            dict_filename = dict_path + "/en_dict.json"

            with open(dict_filename) as f:
                sample_dict = json.load(f)

            for key in sample_dict:
                checked_var = check_strings(string_to_match, key)
                if checked_var is not None:
                    if len(checked_var) == num_of_letters_in_word:
                        match_list.append(checked_var)

            return match_list
        else:
            # treat args[1] as a custom dictionary
            import json
            string_to_match = args[0]

            with open(args[1]) as f:
                sample_dict = json.load(f)

            for key in sample_dict:
                checked_var = check_strings(string_to_match, key)
                if checked_var is not None:
                    match_list.append(checked_var)

            return match_list

    elif len(args) >= 4:
        print('Please supply fewer arguments!')
    elif len(args) == 3:
        num_of_letters_in_word = args[2]
        import json
        string_to_match = args[0]

        with open(args[1]) as f:
            sample_dict = json.load(f)

        for key in sample_dict:
            checked_var = check_strings(string_to_match, key)
            if checked_var is not None:
                if len(checked_var) == num_of_letters_in_word:
                    match_list.append(checked_var)

        return match_list
        

    else:
        import json
        string_to_match = args[0]

        with open(args[1]) as f:
            sample_dict = json.load(f)

        for key in sample_dict:
            checked_var = check_strings(string_to_match, key)
            if checked_var is not None:
                match_list.append(checked_var)

        return match_list


def check_list(*args):
    match_list = []
    
    if not args:
        print('Please supply a string of letters and a list!')
    elif len(args) < 2:
        print('Please supply a string of letters and a list!')
    elif len(args) >= 4:
        print('Please supply fewer arguments!')
    elif len(args) == 3:
        num_of_letters_in_word = args[2]
        
        string_to_match = args[0]

        list_to_check = args[1]

        for entry in list_to_check:
            checked_var = check_strings(string_to_match, entry)
            if checked_var is not None:
                if len(checked_var) == num_of_letters_in_word:
                    match_list.append(checked_var)

        return match_list
        

    else:
        string_to_match = args[0]
        list_to_check = args[1]

        for entry in list_to_check:
            checked_var = check_strings(string_to_match, entry)
            if checked_var is not None:
                match_list.append(checked_var)

        return match_list