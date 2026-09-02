# .Create a recursive function count_unread_messages(messages) that takes a nested dictionary representing WhatsApp chat groups and subgroups, and returns the total number of unread messages across all groups.<br><br><em><strong>Hint:</strong> Each group can have a 'count' key for unread messages and a 'subgroups' key with a list of more groups.</em>




def count_unread_messages(messages):
    total = messages.get("count", 0)

    for subgroup in messages.get("subgroups", []):
        total += count_unread_messages(subgroup)

    return total


messages = {
    "count": 5,
    "subgroups": [
        {
            "count": 3,
            "subgroups": []
        },
        {
            "count": 2,
            "subgroups": []
        }
    ]
}

print(count_unread_messages(messages))