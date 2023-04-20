list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    """
    Steps invloved to solve:
    1. Initialise global empty array for storing merged list.
    2. Iterate through list_1 and make a copy of dict (nameed it as temp_dict) so that original list_1 is not modified.
    3. Iterate through list_2 and check if the id from list_1 matches with any ids from list_2.
    4. If matches, update the temproary dict. Break the second loop.
    5. Add the temp_dict into global merged list
    6. Return the merged list
    """
    
    merged_list = []
    
    for person_dataset_1 in list_1:
        temp_dict = dict(person_dataset_1)
        for person_dataset_2 in list_2:
            if person_dataset_1["id"] == person_dataset_2["id"]:
                temp_dict.update(person_dataset_2)
                break
        merged_list.append(temp_dict)
            
    return merged_list

# list_3 = merge_lists(list_1, list_2)
print(merge_lists(list_1, list_2))
