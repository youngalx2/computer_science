// Given an array of numbers and a target sum, check if there exist two integers inside the array, such that the sum is equal to the target. If so print the two numbers.

// Ex: arr =[1, 4, 2, 8, 9], target = 11 Output: "Yes, 2 and 9 sum to the target"

// Let's look at the inefficient solution:
/* !
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length-1; i++) {
        for (let j = i+1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target)
                return [i,j];
        }
    }
  };
*/
//? What is the time complexity of the above code?
