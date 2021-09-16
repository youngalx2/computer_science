# Recursion

Take a moment to Google the term “recursion.” What do you find? If you're looking for them, recursion jokes exist everywhere in the programming world. After completing this lesson, you too will come to know and love recursion.

### TOPICS

- What Is Recursion?
- Writing a Recursive Function
- When Recursion Can Help

# Learning Objectives

1 of 24

By the end of this lesson, you'll be able to:

- Define recursion.
- Write the base case and recursive case of a recursive function.
- Identify functions that use recursion and explain why it’s used.

# What Is Recursion?

2 of 24

Put simply, recursion is when a function calls itself. We know a function can call upon other functions to achieve its goal, but it can also call upon itself.

When your functions start getting too big to read clearly and test easily, you split them up into smaller functions that each perform part of the larger task. A recursive function, however, will achieve a small part of the larger task, then pass the partially completed problem to another call of itself. It’s just another way of breaking down a large problem into smaller bits.

![recursion](../pics/recursion.jpeg)

# A Useless Recursive Function

3 of 24

Let’s take a look at a function that calls itself and consider what it does. (Warning: Running this program might cause your JS console to stall or crash.)

```js
// Define the function:
function philosopher() {
  console.log('hmm...');
  // Call itself:
  philosopher();
}
// Call the function initially:
philosopher();
```

Why does this function come with a warning? When we call `philosopher()` initially, it prints out "`hmm...`". Then, the function calls `philosopher()` — as in, itself. So, it will once again print "`hmm...`" before calling itself again... forever!

# Fixing the Problem

4 of 24

Let’s look at another recursive function — one that doesn’t come with a warning label (i.e., won’t crash your computer):

```js
function countDown(num) {
  if (num < 0) {
    return;
  }
  console.log(num);
  return countDown(num - 1);
}
```

This function just counts down from a given number to zero. Notice how the last part of the function calls itself, only with a slightly different argument than the number initially given. This is what makes the function recursive and stops it from running forever into eternity.

# Three Steps to Recursion

5 of 24

We can break down the process of a recursive function into three steps:

- **Base case:** When the process can stop.
- **Action:** Put that function to work!
- **Recursive case:** The function is called again but with the assurance that progress is being made toward the base case.

Let’s break each part down by looking at our recursive countdown function if we started with 3 as the argument:

```js
function countDown(num) {
  if (num < 0) {
    return;
  }
  console.log(num);
  return countDown(num - 1);
}

countDown(3);
```

# The Base Case

6 of 24

Here’s the base case for this function:

```js
function countDown(num)
  if(num < 0){
    return;
  }
```

The base case establishes when the recursive function can finally return a specific value and no longer needs to continue calling itself to find that value. Put another way, the base case is where the function bottoms out.

In the countdown function, we first check if the number given is less than `0`. Because `3` is not less than `0`, we can proceed. Once we get below `0`, the countdown is over and the function can complete.

# The Action

7 of 24

Between the base case and recursive case, the function performs an action. In our countdown function, we simply want to count each number before proceeding to the next one, so we `console.log() 3`:

```js
function countDown(num) {
  if (num < 0) {
    return;
  }
  console.log(num);
}
```

You may see the action introduced by “else,” like below. This doesn’t change the function, it just adds in some plain language to explain what's happening in the function:

```js
function countDown(num) {
  if (num < 0) {
    return;
  } else {
    console.log(num);
  }
}
```

# he Recursive Case

8 of 24

Finally, we use recursion by calling the `countDown()` function again. Only this time, we feed it the next number in the sequence by providing `num - 1` as the argument:

```js
function countDown(num) {
  if (num < 0) {
    return;
  }
  console.log(num);
  return countDown(num - 1);
}
```

# Knowledge Check

9 of 24

In plain English, explain what happens when this function reaches the recursive case. (Remember that we've passed in `3` as the argument.)

Hint: There are six things that happen before the base case occurs.

```js
function countDown(num) {
  if (num < 0) {
    return;
  }
  console.log(num);
  return countDown(num - 1);
}

countDown(3);
```

### Answer

Here’s what the function is doing once it gets to the recursive case:

1. Count the number `3`, then call the `countDown()` function again with `2` as the given number.
2. The function makes sure that `2` is still greater than `0`. It is! Proceed.
3. Count the number `2` and call `countDown()` again with 1.
4. The function checks `1` against `0` (it’s greater), counts `1`, and calls `countDown()` with `0`.
5. The `countDown()` confirms that `0` isn’t less than `0`, counts the number `0`, and calls `countDown()` again with `-1` as the given number.
6. Finally, the base case occurs! The “if” check realizes we’ve gone past `0`, into negative numbers, and simply returns to stop the sequence, instead of continuing on with the next few steps.

# Knowledge Check

10 of 24

If a recursive function calls itself twice in the recursive case, what type of time complexity would we get?

- [ ] Linear: `O(N)`
- [ ] Exponential: `O(2^N)`
- [ ] Logarithmic: `O(Log(N))`
- [ ] Factorial: `O(N!)`

Answer:
Exponential

If each recursive call generates two more recursions, this would resilt in exponential growth, meaning that its complecity would scale at an `N^2` rate. At the first layer, it would recure twice. In the second layer, you would have four recursive calls. The third layer would have eight recursions, and so on.

# Writing Recursive Functions

11 of 24

There are four basic steps to writing a recursive function:

1. Define your function and parameters.
2. Define your base case and return the computed result.
3. Perform the action step.
4. Return the function with new arguments to make progress toward the base case.

Let’s work through these steps using a JavaScript function that will add all of the numbers in an array. Pop open [a blank CodePen](https://codepen.io/aharri64/pen/RwKbwRv?editors=0012) to follow along! (Hint: Open the console at the bottom of the CodePen to see what happens when your code runs.)

# Step 1: Function and Parameters

12 of 24

First, let’s write our function. We can use a basic sum function for this problem.

When writing recursive functions, our parameters are important. In this case, we’ll set our parameters as the array we’re in, the index we’re at, and the sum of the numbers so far:

```js
function sumArrayOfNums(arr, index, sum) {}
```

# Even Better Parameters

13 of 24

With recursive functions, it can be helpful to give your parameters default values to reduce some of the function’s calls.

In our sum function example, we might set the index and sum at `0`. When they’re defined this way, the index and sum don’t need to be provided when calling the function:

```js
function sumArrayOfNums(arr, index = 0, sum = 0) {}
```

# Step 2: Define the Base Case

14 of 24

Now that our parameters are set, we can add the base case — when the function can stop and return the computed result.

Here, the function can return the sum when the index has gone past the end of the array:

```js
function sumArrayOfNums(arr, index = 0, sum = 0) {
  if (index === arr.length) {
    return sum;
  }
}
```

# Step 3: Give ’Em Something to Do

15 of 24

Next, add the action step. Here, we’ll add the number at the current index in the array to the sum:

```js
function sumArrayOfNums(arr, index = 0, sum = 0) {
  if (index === arr.length) {
    return sum;
  }
  sum += arr[index];
}
```

# Step 4: Recursion!

16 of 24

Finally, return the function with new arguments to make progress toward the base case. Here, we indicate `index + 1` so that the function continues moving through the length of the array:

```js
function sumArrayOfNums(arr, index = 0, sum = 0) {
  if (index === arr.length) {
    return sum;
  }
  sum += arr[index];
  return sumArrayOfNums(arr, index + 1, sum);
}
```

Don’t forget to return the recursive function call! Otherwise, the final return value won’t go beyond the second-to-last recursive call. Each recursive call needs to return the value of the next call, so the end result gets passed back up the chain to the very first call of the function (the base case).

In your CodePen, test your function with the array `[2, 4, 5, 8]`. (We’ll do the math for you: You should get `19`.)

# Recursive Helper Functions

17 of 24

Sometimes, recursive functions can only get by with a little help from their friends: recursive helper functions. These come in handy when a recursive function needs to branch out in several different directions. You’ll often want a parent scope to hold onto the progress made by each recursive call.

It can be useful to include a non-recursive parent function in which you define and call a recursive function. Including a non-recursive parent function can also eliminate the need for the recursive function within it to hold onto information with parameters. This pattern is especially useful for combination problems, when each recursive function might be calling itself several times with different inputs. A parent function can hold a list of all the combinations, and each recursive call can post its end result to the list held in the parent scope.

Here’s what `sumArrayOfNums()` would look like with a helper function:

```js
function sumArrayOfNums(arr) {
  let index = 0;
  let sum = 0;
  // Notice the lack of parameters in rSum!
  function rSum() {
    if (index === arr.length) {
      return sum;
    }
    sum += arr[index];
    index++;
    return rSum();
  }
  // Once you’ve defined the helper function, make sure you call it!
  return rSum();
}
```

# Why Recursion?

18 of 24

To answer that question, we can compare recursion to something you already know and love: loops, which use iteration.

For simple problems, a `for` loop is just as good as a recursive function. In fact, almost any recursive function can be written using iteration — for example, our `countDown()` function:

```js
function countDown(num) {
  for (x = num; x > 0; x--) {
    console.log(x);
  }
}
```

In most cases, iteration is more efficient than recursion, as it uses less memory space. This begs the question: Why use recursion at all?

# Here’s Why

19 of 24

As you tackle more complex problems, some will just make more sense to solve recursively than iteratively. Recursion is written more cleanly and with less code, especially when a problem gets larger and larger.

But the bottom line is that there’s no hard and fast rule. A quick search on [Stack Overflow](https://stackoverflow.com/search?q=recursion+or+iteration&s=0d1d9bcc-2bde-484b-9316-b296211d44ca) will return myriad opinions on whether recursion or loops are better. Some programmers think recursion is easier to read, while others argue that loops are easier; some argue that loops are more concise than recursion, while others argue that recursion can be written with less code; some see more risks in writing loops than in using recursion, and vice versa.

In the end, it’s up to you and your understanding of the problem you are solving.

# When to Use Recursion

20 of 24

Recursion operates by breaking down a problem into smaller chunks. So, if you have a problem that can be broken down in this way, recursion is a natural fit.

Use recursion in any situation that requires exploring multiple possibilities or paths, such as:

- Calculating all possible combinations of elements.
- Checking all possible routes between two destinations.

Recursion provides the simplest solution to problems like these by allowing a function to continue through each possibility in a new recursive call.

# Knowledge Check

21 of 24

Which of these scenarios is best suited for a recursive function?

- [ ] A: Searching an unsorted list of users for a specific username.

- [ ] B: Determining all possible words that can be formed from a given set of values.

- [ ] C: When there's a limited amount of space in memory and we need the most efficient solution.

B, Recursion is a great solution to problems that need to explore every option - all possibilities, all cominations, etc.

# Let’s Talk About Interviews

22 of 24

Given how frequently it can be used to write algorithms and functions, recursion is a common interview topic. Here’s what you might encounter:

- Determining if a given problem is a good fit for a recursive solution and why.
- Writing a recursive function. Even if you’re not asked to code the solution, you might be asked to sketch or explain how the function would be written. [Here’s what that might look like](https://www.youtube.com/watch?v=bGC2fNALbNU).

Check out these articles for more examples of how recursion may come up in engineering interviews:

- [Hacker Noon](https://hackernoon.com/coding-interview-recursion-f0d60c9dbb60)
- [Byte by Byte](https://www.byte-by-byte.com/recursion/)

# Time to Practice

23 of 24

Let’s practice building some functions with recursion!

[This CodePen](https://codepen.io/GAmarketing/pen/oVNWjd?editors=0010#0) contains five code exercises that will help you hone your recursion chops. It also includes test scripts for each function so you can see how you did!

When using the CodePen, remember:

- Fork the Pen.
- Write your code in the JavaScript box (there’s some pseudocode to get you started).
- Don't touch the test scripts at the bottom!

Don’t feel like you have to finish all five exercises — or any of them! These functions are tricky, so see how far you can get without descending into a recursive rabbit hole.

# Recursion Review

24 of 24

Welcome: You’re now a member of recursion club. The first rule of recursion club? You can never stop making recursion club jokes. (Want to hear some? Check out the r/recursion [Subreddit](https://www.reddit.com/r/Recursion/).)

The second rule of recursion club? Don’t forget about the three components of a recursive function:

- **The base case:** When a recursive function can stop and return a specific value.
- **Action:** What the function should be doing.
- **The recursive case:** When the function calls itself and continues to run.
