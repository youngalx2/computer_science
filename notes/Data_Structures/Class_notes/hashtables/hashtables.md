```js
let arr = ['James', 'Roger', 'Doug', 'Henry'];
```

If I didn't know if James was in there

    Iterare, arr.length = n, it's gonna take O(N)

```js
let names = {
  James: True,
  Roger: True,
  Doug: True,
  Henry: True,
};
// TIME COMPLEXITY = O(1)
if (names['James']) {
  console.log('I found James');
}
```

# hash-tables

## Hash-Tables Application

### Objectives

- [ ] Describe some of the benefits of using a hash-table over working with lists, arrays
- [ ] Understand and articulate the difference in time complexity when using a hash-table vs nested loop
- [ ] Use hash-table to write faster more efficient code

Let's put this knowledge into code with a couple coding challenges. These can be solved without using a hash, with nested loops but we can decrease the time complexity using hash-tables.

We are going to look at two problems that can be solved naively with 0(n^2), but if we implement a hash-table we can solve it more efficiently.

## Problem 1 Two-Sum

Given an array of numbers and a target sum, check if there exist two integers inside the array, such that the sum is equal to the target. If so print the two numbers.

Ex: arr =[1, 4, 2, 8, 9], target = 11
Output: "Yes, 2 and 9 sum to the target"

Let's look at the inefficient solution:

```js
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
};
```

What is the time complexity of the above code?

---

This will check all possible combinations but when we have a nested loop that depends on the input size we have a 0(n^2) complexity.

Instead let't think of another way to look at this. When you are given the array [1, 4 ...] and the target = 11, what do you think about when you first look at the 1? What do you start to search for in the array?

Let's store this value in an object, so that we can have direct access to it, O(1),

<details><summary>Our begginings</summary>

```js
var twoSum = function (nums, target) {
  //define an object holder
  const holder = {};
  for (let i = 0; i < nums.length; i++) {
    // make each value a key in our holder
    holder[target - nums[i]] = i;
  }
  // now our lookup time will be O(1) to look for those values
};
```

</details>

So if we have 0(1) lookup time for each difference, then we can now do another simple loop, which is _not nested_, so it doesn't become 0(n^2) time complexity.

<details><summary>The finished up code</summary>

```js
var twoSum = function (nums, target) {
  //define an object holder
  const holder = {};
  for (let i = 0; i < nums.length; i++) {
    // make each key the 2nd number needed, and the value the 1st number
    holder[target - nums[i]] = nums[i];
  }
  // now our lookup time will be O(1) to look for those values
  for (let i = 0; i < nums.length; i++) {
    // easy look up with {} vs []array
    if (holder[nums[i]]) {
      // we must have a pair, since these were
      // created as the difference
      console.log(`Yes, ${nums[i]} and ${holder[nums[i]]} sum to the target`);
      break;
    }
  }
};
```

</details>

This results in linear time complexity O(n), so knowing that using a hash-table to look things up is faster than an array allowed us to solve this problem more efficiently.

## Problem 2 SubArray?

Given two arrays where arr1.length > arr2.length, check if arr2 is a subarray. Order not mattering.

Input:
arr1 =['hey', 'is', 'what', 'is', 'up', 'with', 'hashmap']
arr2 =['hashmap', 'is', 'what', 'is', 'up']
return >> true //arr2 is a subarray of arr1.

Step1. Think about how you can use a hash-table as you go through the first array, and store keys and values.

Step2. Then can you do another loop, which is not nested to check if values are there?

<details><summary>Step 1 finished up</summary>

```js
function checkSubArray(arr1, arr2) {
  //let's create an object that stores the values of arr1 as keys
  //and the value is  how many times, they occur
  const holder = {};
  //I want each of the words from the array arr1
  //as properties in the magazineHolder, and how many times they occur
  for (let i = 0; i < arr1.length; i++) {
    //how can I add each word as a property to arr1 holder
    //does the property already exist?
    if (!holder[arr1[i]]) {
      //if in this code block magazineHolder[*arr1*[i]] was false
      //we didn't have the property yet, so want make it exist
      holder[arr1[i]] = 1;
    } else {
      //it already existed
      //so add one to the count
      holder[arr1[i]] = holder[arr1[i]] + 1;
    }
  }
}
```

</details>

Alright now we can loop through the second array and use our awesome lookup power O(1) to check values against our holder as we go through

<details><summary>Step 2 finished up</summary>

```js
function checkSubArray(arr1, arr2) {
  //let's create an object that stores the values of arr1 as keys
  //and the value is  how many times, they occur
  const holder = {};
  //I want each of the words from the array arr1
  //as properties in the magazineHolder, and how many times they occur
  for (let i = 0; i < arr1.length; i++) {
    //how can I add each word as a property to arr1 holder
    //does the property already exist?
    if (!holder[arr1[i]]) {
      //if in this code block magazineHolder[*arr1*[i]] was false
      //we didn't have the property yet, so want make it exist
      holder[arr1[i]] = 1;
    } else {
      //it already existed
      //so add one to the count
      holder[arr1[i]] = holder[arr1[i]] + 1;
    }
  }
  let isSubArray = true;
  for (let i = 0; i < arr2.length; i++) {
    if (!holder[arr2[i]]) {
      // we have an element in arr2 we didn't in arr1, not a subarray
      isSubArray = false;
    } else {
      //it's in there let's decrement
      holder[arr2[i]] = holder[arr2[i]] - 1;
      // this will go to zero potentially which would evaluate to false
    }
  }
  return isSubArray;
}
```

</details>

<details><summary>Python solution credit: Andrew Bith</summary>

```python
def sub_check(arr1, arr2):
    hash_table = {}
    for word in arr1:
        if not (word in hash_table):
            hash_table[word] = 1
        else:
            hash_table[word] += 1
    for word in arr2:
        if not (word in hash_table):
            return False
        else:
            hash_table[word] -= 1
            if hash_table[word] < 0:
                return False
    return True
```

</details>

Want some more practice? Here is another good one you could use a hash-map for. https://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/
. Hopefully you can see some value to understanding this data structure and how it can help you write efficient code, and decrease time complexity for some of your functions.
