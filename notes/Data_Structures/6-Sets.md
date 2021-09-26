# Sets

Sets are simple, easy-to-understand data structures that operate a lot like arrays, only with one important plot twist. Are you intrigued yet? Read on!

### TOPICS

- What Is a Set?
- Working With Sets

# Learning Objectives

By the end of this lesson, you'll be able to:

- Define a set and how it’s used in programming.
- Distinguish between a set, an array, and a linked list.
- Implement sets and common methods used within them

# Setting the Stage

Most of the data structures we’ve covered so far are examples of list structures: includes arrays, linked lists, stacks, and queues.

Sets — the topic of this lesson — are also list structures. What makes them different? Well, where arrays are used to hold any sequence of values, sets are reserved for **sequences of unique values**.

Here’s how sets compare to some of the data structures we’ve already met:

| List type                                                               | Description                                                        |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Array**                                                               | Any sequence of values.                                            |
| Linked list A list of values, stored in nodes, referencing other nodes. |
| **Stack**                                                               | A list of values in which the first item in is the last item out.  |
| **Queue**                                                               | A list of values in which the first item in is the first item out. |
| **Set**                                                                 | Any sequence of unique values.                                     |

# Meet the Set

You and your friend are going grocery shopping but don’t have much time. To shop faster, you want to split the items on the list and visit different parts of the store. The question here is, “Do we need to go to the dairy aisle at all? What about the bakery?”

This is where a set would come in handy. It could tell you whether or not yogurt is on the list, instead of how many containers of yogurt you need:

`set = ["loaf of bread", "yogurt", "carton of eggs", "lettuce", "scallions", "grapes", "tomato", "spaghetti"]`

When you get to the dairy aisle, you need to know exactly how many containers of yogurt to get. This is where an array would be useful:

`array = ["loaf of bread", "loaf of bread", "yogurt", "yogurt", "yogurt", "yogurt", "carton of eggs, "lettuce", "scallions", "grapes", "tomato", "tomato", "tomato", "spaghetti", "spaghetti"]`
