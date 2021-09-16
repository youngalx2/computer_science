# Basic Sorting Algorithms

Ah, bubble sort. Unused, unloved, and the butt of so many jokes. It tries so hard, but it’s just... so... slow. And insertion sort isn’t too much better. In this lesson, we’ll cover the two most basic sorting algorithms, their complexity classes, and their implementations.

### TOPICS

- Bubble Sort
- Insertion Sort

# Learning Objectives

1 of 17

By the end of this lesson, you'll be able to:

- BubbleDescribe the time and space complexities of bubble and insertion sorts.
- Implement bubble and insertion sorts.

# Back to Basics

2 of 17

Remember when you learned long division in middle school? Not to knock math teachers, but long division was a slow, painful way to get to an answer — even though, eventually, you did. Then in high school, your math teacher finally said it was OK to just use a calculator. You probably grabbed your calculator and never looked back. All that time you spent carrying numbers and finding the remainder? Sayonara!

And if you ever bugged your teachers to explain why you’d spent so many hours learning long division when you could have just used a calculator, they probably told you how important it was to learn the basics so you’d understand more complicated functions down the road.

The same logic applies when we learn sorting algorithms.

# Where We’re Going

3 of 17

This lesson covers the “long division” of basic sorts: **bubble sorts** and **insertion sorts**.

Your math teachers would agree that they’re like long division because:

- They’re slow, inefficient, and infrequently used.
- They’ll prepare you to tackle more complex sorting algorithms.

Bubble and insertion sorts are almost never used in programming. You’re much more likely to use quick or merge sorts in the programs and languages you work with — they’re kind of like the calculators of algorithms.

We learn these basic sorts, however, because they’re simple and intuitive. And by learning these algorithms, you’ll understand the more complicated sorts we’ll describe in a future lesson.

# Meet Bubble Sort

4 of 17

Bubble sorts put values in order by iterating through a data set and comparing neighboring numbers. When the sort encounters a smaller value before a greater value, it swaps the values. The sort continues through the data set, value by value, swapping them until the array is properly sorted.

Here’s the basic process of the bubble sort algorithm:

1. Start at the beginning of an array of items.
2. Compare the item you’re looking at to the next item in the list.
3. If this item is smaller than the next one, keep it in place. If it’s greater, swap them.
4. Move on to the next item.
5. Repeat Steps 1–4 until you can go through the whole list without making any swaps.

![bubble-sort](../pics/bubble-sort.gif)

# How Bubble Sort Works

5 of 17

(video)

Let’s use a bubble sort to sort this array of playing cards from smallest to largest. We’ll start at the beginning.

10 is bigger than the Queen, so we’ll keep them. Then we’ll move on to the next one. The Queen is bigger than the 7, so we can swap them.

We’ll keep moving across the cards, swapping cards, so that the larger cards move to the right and the smaller ones to the left.

# Knowledge Check 1

6 of 17

Is bubble sort a stable or unstable sort?

Stable - The cards remained sorted, even as we completewd more iterations through the set.

That means it's a stable sort

# Knowledge Check 2

7 of 17

What’s the Big O worst case space complexity for bubble sort?

- [x] `O(1)`
- [ ] `O(N)`
- [ ] `O(log(N))`

We didn't have to find a new space for any of our cards while we were sorting them. That makes the space efficienct `O(1)`, because the amount of space used doesn't change as the inputs increase.

# Knowledge Check 3

8 of 17

What is the Big O worst case time complexity for bubble sort?

- [ ] `O(1)`
- [ ] `O(N)`
- [x] `O(N^2)`
- [ ] `O(log(N))`

Bubble sort has a quadratic runtime - the worst one! Think about how many iterations we had to make to sort just our array of eight cards. Even President Barack Obama knows how slow bubble sort is. Check this out on the next page.

# Obama on the Bubble Sort

9 of 17

![Barack Obama - Computer Science Question](https://www.youtube.com/watch?v=k4RRi_ntQc8)

# Meet Insertion Sort

10 of 17

Next up is insertion sort. Basically, an insertion sort takes each item and inserts it into the right place in the array.

Like bubble sort, insertion sort isn’t terribly efficient — it ends up traversing over and over the array many times. However, it’s definitely faster than bubble sort and works more efficiently in a wider variety of circumstances. It’s mainly used in real life in conjunction with bucket sort, which we’ll learn about soon.

![insertion-sort](../pics/insertion-sort.gif)

# Insertion Sort, Visualized

11 of 17

(video)

One way to visualize insertion sort is to think of playing a game of cards.

Imagine you’re playing poker. As the dealer hands you your cards, you’re picking up them one by one and ordering them numerically as you go.

The first card you pick up is sorted by the fact that it’s the only card you have. Any subsequent cards you pick up can be ordered according to how they fit into your existing hand. Each time you pick up a new card, you can simply insert it into the proper location.

The next card is 2. It’s lower than your existing cards, so you can move it to the left. You’ll continue sorting cards this way as you pick them up.

# Knowledge Check 4

12 of 17

Is insertion sort a stable or unstable sort?

Stable - Like bubble sort, the cards in your hand remain sorted as you pick them up. That means it's a stable sort.

# Knowledge Check 5

13 of 17

What’s the Big O worst case space complexity for insertion sort?

- [x] `O(1)`
- [ ] `O(N)`
- [ ] `O(Log(N))`

The space you're using in an insertion sort remains constant, leading to the `O(1)` complexity.

# Knowledge Check 6

14 of 17

What’s the Big O worst case time complexity for insertion sort?

- [ ] `O(1)`
- [ ] `O(N)`
- [x] `O(N^2)`
- [ ] `O(log(N))`

Insertion sort is a lot like bubble sort in terms of time efficiency: lousy. Even though insertion sort works a bit faster, we still talk about both in the same Big O classification.

# Let’s Talk About Interviews

15 of 17
Despite bubble sorts being virtually unusable, interviewers love to ask about them. It’s the simplest sorting algorithm to explain and shows that you understand sorting conceptually. You might be asked to sketch out how bubble sort works or answer some basic questions about the algorithm, [like these ones here](https://hoven-in.appspot.com/Home/Data-Structures/Data-Structure-Interview-Questions/interview-questions-on-bubble-sort-01.html). Similarly, you might be asked to sketch or explain how insertion sort works. [Here’s a nice recap](https://hackernoon.com/programming-with-js-insertion-sort-1316df8354f5).

Luckily, the internet is full of fun visualizations on how sorting algorithms work! Check out a few:

This one from the [University of San Francisco](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html).
A similar visualization on YouTube: [bubble sort](https://www.youtube.com/watch?v=Cq7SMsQBEUw) and [insertion sort](https://www.youtube.com/watch?v=8oJS1BMKE64).
Last but certainly not least: folk dancing for [bubble sort](https://www.youtube.com/watch?v=lyZQPjUT5B4&t=53s) and [insertion sort](https://www.youtube.com/watch?v=ROalU379l3U).

# Time to Practice

16 of 17

Ready to start coding these algorithms?

Check out this [CodePen](https://codepen.io/GAmarketing/pen/xMeqaN?editors=0010#0), where you can practice implementing bubble and insertion sorts. For each algorithm, there’s pseudocode to get you started and a test script so that you can check your work.

Remember:

- Fork the Pen before you start making edits.
- Don’t touch the test scripts at the bottom.
  These algorithms are sneakily difficult to write! Try to get as far as you can, but don’t worry about completing both.

# Basic Sorting Algorithms Review

Let’s recap bubble and insertion sorts! Because of their inefficiency, they’re rarely used in programming, but they’re basic, fundamental algorithms with which to start.

**Bubble sort** works by iterating through a list, swapping neighboring values, and repeating this process until the set is sorted.

- Runtime: O(N^2)
- Space complexity: O(1)
- Stable

**Insertion sort** works by taking a value in an array and inserting it into its proper position.

- Runtime: O(N^2)
- Space complexity: O(1)
- Stable

### TOPICS

- Bubble Sort
- Insertion Sort
